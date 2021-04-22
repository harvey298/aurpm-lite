#/bin/python3
# Copyright harvey298 2021 GPL

# Imports
import os, sys, subprocess, time
from sys import argv
from subprocess import run, PIPE, STDOUT, Popen

# Var init
workdir = "/home/marco/etc/aurpm-lite/test"
debug = True
server = "IP:Port"
pkg = "null"


os.chdir(workdir)


if debug == True:
    print("aurpm-lite is in debug mode!")
    print("working directory: " + workdir)

# Functions
def install():
    try:
        pkg = argv[2]
    except IndexError:
        print("You haven't told me what package you want!")
        print("Please tell me the package!")
        pkg = input("Package Name: ")


try:
    arg = argv[1]
    if arg == "-i":
        install()
    elif arg == "-s":
        print("tmp")
except IndexError:
    print("You haven't told me what todo!")
    print("Assuming you want to install a package!")
    install()
