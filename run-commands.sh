# Ring Parameters :

# ring features
if [ ! -d "${RING_HOME}/tmp" ]; then
  mkdir ${RING_HOME}/tmp
fi

# tunned environment
export PATH=$PATH:$RING_HOME/bin

if [ -n "${PYTHONPATH}" ]; then
  export PYTHONPATH=$PYTHONPATH:$RING_HOME/lib
else 
  export PYTHONPATH=$RING_HOME/lib
fi

# Basic alias
alias ls='ls --color=auto -h'
alias backup='rsync --iconv=utf8 -azv'

# Git alias:
alias status='git status -sb .'
alias log='git log -n 4'
alias log-all='git log --all --decorate --oneline --graph'
alias diff='git difftool -t meld'

# Auto Completiopn
#autoload bashcompinit                    
#bashcompinit

#complete -C ~/Ring/bin/ring-complete ring
