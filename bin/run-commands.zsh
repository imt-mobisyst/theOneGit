autoload bashcompinit                    
bashcompinit
complete -C "python3 -c 'from oneRing.__main__ import commandComplete; commandComplete()'" ring
