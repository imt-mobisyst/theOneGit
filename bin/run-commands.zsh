autoload bashcompinit                    
bashcompinit
complete -C "python3 -c 'from oneProject.__main__ import commandComplete; commandComplete()'" op
