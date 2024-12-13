#!/usr/bin/env bash
ONEPATH="$( cd -- "$(dirname "$0"/..)" >/dev/null 2>&1 ; pwd -P )"

# Go at the root directory of the project 
cd `dirname $0`/..

# Install...
pip install .

# setup shell environment

echo """
# OneProject
export ONE_PROJECT=$ONEPATH
source \$ONE_PROJECT/bin/run-commands.bash
""" >> ~/.bashrc

echo """
# OneProject
export ONE_PROJECT=$ONEPATH
source \$ONE_PROJECT/bin/run-commands.zsh
""" >> ~/.zshrc
