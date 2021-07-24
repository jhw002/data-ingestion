# data-ingestion

## Misc
Markdown: https://www.markdownguide.org/cheat-sheet/

`python3 script.py` Run the code from command line

## ClI
`--help` most cli programs have this option

`man X` where X is the thing you want more info on

`history` : list all commands you have run so far

## Git
`git status` : what files are staged / unstaged

`git branch -l` list the local branches

`gid add --all` : adds all files to be commited (not the actual commit)

`git commit -m "Cool Message"` : Actually commit

`git diff` : Whats different from staged and current

`git diff --cached` : Whats differrent including what is staged

`git log` : list commits

`git push` : push up commits to remote branch

`git reset --hard` : resets files to last commit

`git clean -df`: remove all unversioned files (great for removing temporary files)

## Visual Studio Code

`⌘ + shift + p` : omniwindow

`⌘ + p` : jump to file

## Pip  / dependancy managment

1. `pip install pandas`
2. `pip freeze > requirements.txt`

## TODO

Add pandas as a proper dependency 

## Getting Set up

# Virtual Env
https://realpython.com/python-virtual-environments-a-primer/
https://pypi.org/project/virtualenv/

`python3 -m venv .env`

`source .env/bin/activate`

`python3 -m pip install -r requirements.txt`

# Actual Code

# Practice data: "PracticeData.xlsx"
# Read xlsx
# write to Sqlite
# sql gui 