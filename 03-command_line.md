# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
* show current working directory path - pwd
* creating a directory - mkdir Name
* deleting a directory - rmdir Name
* creating a file using `touch` command - touch file.txt
* deleting a file - rm file.txt
* renaming a file - mv file1 file2
* listing hidden files - ls -a
* copying a file from one directory to another - cp file1 direct1
* find things inside a file - grep things file.txt
* substitute A with B globally - sed 's/A/B/g' file.txt

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls`: list files and directories in the current directory
`ls -a` : list files and directories including the hidden ones in the current directory
`ls -l`: list files in the long format as a table
`ls -lh` : list files in the long format as a table and display file sizes with units (human readable formats)
`ls -lah` : list files including the hidden ones in the long format as a table and disply file sizes with units
`ls -t`: list and order files by time of the latest modification
`ls -Glp`: list files in the long format and put "/" after directories 
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
ls -1
ls -d
ls -c
ls -h
ls -R

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > "xargs" as "excute arguments"reads data from standard input (stdin) and executes the command (supplied to it as argument) one or more times based on the input read. It is useful and conveninent to excute orders, like at times when you don't need to define a new funtcion to do stuff. 

Ex. The following xargs takes stdin from the echo and displays the numbers in two columns:
echo 1 2 3 4 | xargs -n 2

 

