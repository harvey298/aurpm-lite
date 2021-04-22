#!/bin/python3
# Copyright harvey298 2021 GPL
#import git

from git import Repo

git = git.Repo.Git
git.clone("https://github.com/harvey298/aurpm.git")

clone_from("https://github.com/harvey298/aurpm.git", "./test")