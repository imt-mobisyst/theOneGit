# Ring: A project to rule them all

_Ring_ is mainly designed to manage a collection of git repos.

## Get-stated:

```bash
sudo apt install git git-lfs python3 python3-pip
git clone git@github.com:imt-mobisyst/ring.git Ring
```

We recommand to source your `run-commands` in your favorit shell.

`bash` for instance:

```bash
echo """
# Ring
export RING_HOME=~/Ring
source \$RING_HOME/run-commands.sh
""" >> ~/.bashrc
source ~/.bashrc
```
