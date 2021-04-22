#/bin/python3
# Copyright harvey298 2021 GPL

# Imports
import os, sys, subprocess, time, threading
from sys import argv
from subprocess import run, PIPE, STDOUT, Popen

# Vars
installdir_name = ".aurpm-test"
help = """\npython setup.py -m Installs aurpm \npython setup.py -l Installs aurpm-lite \npython setup.py -r Removes aurpm/aurpm-lite\npython setup.py -s Installs Aurpm server"""
homedir = os.environ['HOME']
install_path = homedir + '/' + installdir_name
global is_lite
global is_server
global need
global am_root


print("Welcome to the aurpm installer!")
# Functions

# Checking for root
def root_check(need):
    if need == False:
        if os.getuid() == 0:
            print("Oh No! I've been given super powers! Do Not run any AURPM component as root!")
            sys.exit(1)
    elif need == True:
        if os.getuid() == 0:
            am_root = True
        else:
            print("\naurpm-lite server needs to be installed as root since it will sit in the root's user home")
            sys.exit(1)

# Function for updating
def update(homedir, install_path):
    print("Attempting to update aurpm! This action may repair broken installs!")
    os.chdir(install_path)
    os.system("git pull")
    os.chdir(homedir)
    print("\nDone!")

# Remove function to uninstall
def remove(homedir, install_path):
    need = False
    root_check(need)
    print("removing aurpm!")
    os.chdir(homedir)
    aurpm_work_dir = install_path + '/work'
    #os.rmdir()
    os.system("rm -rf " + installdir_name)

# Main Function for installing
def main(homedir, install_path):
    os.chdir(homedir)
    if is_server == False:
        need = False
        root_check(need)
        if is_lite == False: # Main install
            print("Installing AURPM from the main repo")
            try:
                os.mkdir(installdir_name)
            except FileExistsError:
                print("aurpm directory already exsits!")
                update(homedir, install_path)
                sys.exit(1)
            os.system("git clone https://github.com/harvey298/aurpm.git " + install_path)
            
        elif is_lite == True: # Lite Install
            print("Installing AURPM from the lite repo")
            try:
                os.mkdir(installdir_name)
            except FileExistsError:
                print("aurpm directory already exsits!")
                update(homedir, install_path)
                sys.exit(1)
            tmp_dir = install_path + '/work/aurpm'
            os.chdir(install_path)
            os.mkdir('work')
            os.system("git clone https://github.com/harvey298/aurpm-lite.git " + tmp_dir)
            os.system(f"cp -r {tmp_dir}/client/* ./")
            os.rename("README.md", "Client_Readme.md")
            os.system(f'cp {tmp_dir}/README.md ./')
            os.system(f'cp {tmp_dir}/LICENSE ./')
            os.system('rm -rf '+ tmp_dir)

    elif is_server == True: # Server install
        need = True
        root_check(need)
        print("Installing aurpm Server!")
    
# Argument Handling
try:
    if argv[1] == '-m':
        print("Installing aurpm")
        is_lite = False
        is_server = False
        main(homedir, install_path)
    elif argv[1] == '-r':
        remove(homedir, install_path)
    elif argv[1] == '-l':
        is_lite = True
        is_server = False
        main(homedir, install_path)
    elif argv[1] == '-s':
        is_server = True
        main(homedir, install_path)
    elif argv[1] == '-h':
        print(help)
except IndexError:
    print(help)    

print("\nDone!")