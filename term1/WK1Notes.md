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

## HTML

`<!--comment-->` and  is a comment

Some elements in HTML are inline - appearing one beside the other and others are in block (one below the other). This can be changed using CSS

### What is HTML
* Is markup language used to tell browser how to display content
* Tags are the way content is marked up
* A forward slash indicate a closing tag however not all have closing tabs `<tag>content</tag>`

### Doc Structure
* When right clicking and inspecting a website it can show you how a website is structured
* `<head>` is used for styling and interacting
* `<body>`contains the content of the page
* Using browser inspects can use to do some debugging as it won't be updated due to it being on server when refreshed

#### Doctype Declaration
* All HTML docs must start with a `<!DOCTYPE>` Declaration as it is info to the browser about what doc to expect. Indicates type of HTML doc
* HTML5 decs are simple: `<!DOCTYPE HTML>`
* `<html><head><body>` are the three main tags in a HTML doc

`<head>`
* Contains data that is not shown on the page, however it has metadata, title and styling info

`<body>`
* represents the contenty that is visible on the web page

### Basic HTML Tags

`<heading>`
* Shows headings and goes up to `<h7></h1>`

`<p>`
* Paragraph or text content

`<img src="link"/>`
* Used for images and `src` is an additional attribute for whhere to source image

`<a href="link">Text linked to hyperlink</a>`
* link tag a meaning attribute `href` meaning hyperlink reference

`<br><br>`
* Essentially a double space or enter

`<ul></ul>` and `<ol></ol>`
```html
<ul> 
    <li>coding<li>
    <li>gaming<li>
</ul>
```
* `<ul>` meaning unordered list and `<ol>` meaning ordered list (numbered)

### Absolute and Relative Path

**Absolute Path** Points to the complete path, could be ony link from the internet or for a local file all the way from root directory.
e.g. `<a href = "htpps://www.google.com/">Google</a>` directly to google or 

**Relative Path** Points to another file location with respect of current file through directories etc. Always navigates to a relative folder then to file
e.g. `<img src = "img/kitty.jpg">`

Can add `alt` as an alternate attribute which means if image or link is broken it will show as the alt text. e.g. `<img src="img/kitty.jpg" alt ="kitten"/>`

### Link Different Pages

**ID** Used to anchor to different secions of the same page. Usually represented with a # at the front e.g. `#page title` and within the tag itself `<h1 id="heading">Heading 1</h1>`

Below Shows footer linking to below footer and heading linking to heading.

````html
        <h1 id="heading">Heading 1</h1>
        <a href="#footer">footer</a>

        <h1 id = "footer">Footer</h1>
        <a href ="#heading">back to Top</a>

````
**Relative Paths** Used to link different html pages. 

* Relative pathing means need to show path but can use . as a shortcut

```` 
<a href="./contact.html">Contact page</a>
````

### Semantic Tags

Clearly describle its meaning to bnoth browser and developer. INstead of `<div>` and `<span>` saying nothing about the content while `<form>`, `<table>` and `<article>` clearly define the content.

In html there are several semantic tags check [cheat sheet](https://www.w3schools.com/html/html5_semantic_elements.asp).