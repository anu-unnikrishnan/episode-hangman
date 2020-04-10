import urllib.request
import string
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_"
show = input("Enter any TV show : ")

#construct the url of the list of episodes wikipedia page
show = show.split()

mclist = []
partlist = []
showname = []

for word in show:
    #don't capitalise if word is one of the following words
    if word == "and" or word == "of" or word == "by" or word == "to" or word == "with" or word == "in":
        showname.append(word)
    #if the word is 'the' but it's not the first word of the title, don't capitalise
    elif word != show[0] and word == "the":
        showname.append(word)
    #if the word contains two hyphenated words, capitalise both of them
    elif '-' in word:
        word = word.split('-')
        for part in word:
            part = part.capitalize()
            partlist.append(part)
        new = '-'.join(partlist)
        showname.append(new)
    #if the word is something like McGuire
    elif 'mc' in word:
        word = word.split('mc')
        #mclist.append('Mc')
        for part in word:
            part = part.capitalize()
            mclist.append(part)
            new = 'Mc'.join(mclist)
            showname.append(new)
    else:
        showname.append(word.capitalize())

showname = ' '.join(showname)
linkshow = showname.replace(' ', '_')
linkshow = linkshow.replace("'", '%27') #apostrophes must be converted before adding to url
url = url + linkshow + "_episodes"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")

A = []

#the episode titles we want are stored under the class 'summary'
for right_table in soup.find_all(class_='summary'):
    
    #for episode titles which are not links
    #we just extract the text
    if right_table.find('a') == None:
        cells = right_table.find(text = True)
        print(cells)
    
    #for episode titles which are links (indicated by <a> tags in HTML)
    #we extract the text between the <a> tags using contents[0]
    else:
        cells = right_table.find('a').contents[0]

    #get rid of speech marks
    cells = cells.replace('"', '')
    #get rid of episode titles with Part 1, Part 2 etc
    cells = cells.replace('(Part 1)', '')
    cells = cells.replace('(Part 2)', '')
    cells = cells.replace(': Part 1', '')
    cells = cells.replace(': Part 2', '')
    cells = cells.replace(': Part 3', '')
    cells = cells.replace(', Part 1', '')
    cells = cells.replace(', Part 2', '')
    #remove whitespace at end of episode titles
    cells = cells.rstrip()
    #remove any episode titles that don't have any alphabets eg [45], 2017
    if any(c.isalpha() for c in cells) == False:
        continue
    A.append(cells)

#create a pandas dataframe df with a column for the episode titles
df = pd.DataFrame(A, columns = ['Episode title'])
df = df.mask(df.eq('')).dropna() #get rid of blank episode titles
df.drop_duplicates(inplace = True) #get rid of duplicate episode titles

#write episode titles to csv file
df.to_csv('EpisodeList.csv', sep = ' ', index = False, header = False)
print("Scraped!")

