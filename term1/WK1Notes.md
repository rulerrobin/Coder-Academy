# Week 1 Notes

## Terminal Basics

Terminal is an application that allows users to access computers and files without having to use GUI and access to things that are only accessible to CLI. Most code will be executed and run through terminal.

### Commands List

| Command | Use | Examples |
| ------- | ------ | ------ |
| `pwd `| shows the current location (print working directory) |
| `mkdir` | creates a folder (mkdir 'folder name') |
| `cd `| change directory |
| `cd .` | . is placeholder for current directory | 
| `cd ..` | .. is to previous directory |
| `ls `| lists out folders and files in the current directory |
| `touch` | makes a file | touch filename.txt |
| `more `| shows contents of file | more filename.txt
| `mv `| moves file contents from 1 file name to another essentially moving | can move files into folders e.g. mv file folder
| `clear` | clears out the terminal |
| `cp `| is a copy function | cp filename.txt newfilename.txt |
| `rm `| deleting files function | rm filename.txt |
| `rm - rf` | delete directories/folders | rm - rf folder |
| `man `| shows user manual for terminal | 
| `echo `| outputs on terminal | echo text |  
| `nano `| can be used to view/edit contents of a file | 
| `cat `| prints content of file |

* Example with . and .. you are able to use . to say current directory e.g. cd ./folder/folder. You are also able to combine . and .. cd ./../..

* mv you.txt ../ moves file up one for example

* When moving between files and folders if there is a space must use quotation marks either singele or double

* echo can also be used to output the text into a new file

* when using echo if >> is put in front the content will be appended on

## Git Basics

Topics
* Version Control
* Git vs GitHub
* Core Git Concepts
* Demo

### Version Control
Due to the nature of work it ends up being that there will be many files and many versions of files. Version control solves the problem of people working on files at the same time and multiple versions. It keeps track of who is making what changes and resolve conflicts between conflicting changes.

It's more of a tool that keeps code organised.

* Keeps track of large groups of files
* Popular systems (Git, SVN, Mercurial)

#### Git and GitHub

| Git | GitHub |
| ----------- | ---------- |
| Version Control System | Web app owned by MS |
| Runs locally on your computer | Wraps useful functionality around Git | 
| Open Source | A Cloud repository | 

Git is the system that is used and GitHub is the web app that allows collaboration.

#### Core Git Concepts

##### Repository

A folder where all the files are stored. 

##### Staging Area

A container where we store files we want to change or are making changes to. Where the files from the repository go that are pulled to make changes.

##### Commit

A bookmark where all changes to files in the staging are stored and saved. Commit takes snapshot and puts changes into a log.

##### Pull from repository -> Stage -> Commit to go back to repository

### Commands List

| Command | Use | Examples |
| ------- | ------ | ------ |
| `git init` | initialises git in the directory |  |
| `git status` | shows what branch, commits, files in staging area or not |
| `git add` | adds file to staging area | git add filename |
| `git commit -m` | makes changes -m is a message about the changes made | If you forgot the -m you should be able Ctrl X or Q to get out out NANO |
| `git log` | logs of all changes that have been made |
| `git diff` | shows changes made |

* can still use . for current directory as a shortcut e.g. git add .

## General Notes

Origin means the local working repository, however when it says `origin/main` it means that it is being worked on the remote repo.
Working tree clean means there is nothing staged to commit any changes. 
fork - create own remote repo from someone else's with all of the hjistory up tht etime of the fork
clone - coipy of the contents of a remote repo to your local repo and working directory
master/main- default branch on a repo
origin - default name of the connection the remote repo
## Markdown

Markdown is a mark up language that is highly compatible with HTML and is a major part of how websites and apps are actually seen.

* in VS Code can use CTRL SHIFT V as a preview window
* using ! before a link turns the link into viewer for images 

### Commands List

Use Markdown cheatsheet as not too much too search through

