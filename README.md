# Python Notepad

A notepad app made using python. The objective is for it to use a personal Google Drive to store the written notes (in markdown) and a "data" folder to store object information, all through a graphical user interface.

Keywords: OOP, Python, Google Drive API, GUI, docker, docker-compose

## Prerequisites:

* Docker version 18.09.7
* docker-compose version 1.23.2

## Installing && Using

The program is dockerized, as such, you only have to run "notepad":

* `sudo chmod +x ./notepad` unless "notepad" is already executable
* `./notepad`

## Debugging

If you get an error in the likes of `_tkinter.TclError: couldn't connect to display ":0"`, make sure that X11 allows all users to print. `xhost +` solves the problem on Ubuntu 18.04.