# The One Git-project: A project to rule them all

_The One Git_ is mainly designed to manage recursivelly a collection of git repos.

## Get-stated:

```bash
git clone https://github.com/imt-mobisyst/theOneGit
theOneGit/bin/instal.sh
# in a fresh new shell:
tog help
```

## Manual install...

Install commands tools with pip.

We recommand to set set an environnement variable `$ONE_PROJECT` with the path to your `oneProject` directory and to source the `bin/run-commands` in your favorit shell' run-commands file (`~/.bashrc` for bash).

`bash` for instance:

```bash
echo """
# The One Git
export ONE_GIT=/home/you/path/to/theOneProject
source \$ONE_PROJECT/run-commands.bash
""" >> ~/.bashrc
source ~/.bashrc
```
