#this script scrapes the wikipedia page for list of episodes of certain shows
#then lets you play hangman with a randomly chosen episode title

printf "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to Episode Hangman!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n1. Play Hangman with TV show episode titles\n2. Play 2-player Hangman\n\nEnter your choice : "
read x

if [ $x -eq 1 ]
then
    python3 ScrapeAnyShow.py
else
    x=2
fi

printf "x = $x\n"

python3 EpisodeHangman.py --a $x
