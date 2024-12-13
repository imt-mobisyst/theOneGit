# The One Project: A project to rule them all

_One Project_ is mainly designed to manage recursivelly a collection of git repos.

## Get-stated:

```bash
git clone https://github.com/imt-mobisyst/oneProject
oneProject/bin/instal.sh
# in a fresh new shell:
one help
```

## Manual install...

Install commands tools with pip.

We recommand to set set an environnement variable `$ONE_PROJECT` with the path to your `oneProject` directory and to source the `bin/run-commands` in your favorit shell' run-commands file (`~/.bashrc` for bash).

`bash` for instance:

```bash
echo """
# The One Project
export ONE_PROJECT=/home/you/path/to/oneProject
source \$ONE_PROJECT/run-commands.bash
""" >> ~/.bashrc
source ~/.bashrc
```
