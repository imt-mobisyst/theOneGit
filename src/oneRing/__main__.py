import sys
from . import actions

def commandHandler():
    action= "help"
    arguments= ["help"]
    if len(sys.argv) > 1 :
        action= sys.argv[1]
        arguments= sys.argv[1:]
    
    if action not in actions.keys() :
        action= "help"
    
    actions[action]( arguments )
    
    return 1

def commandComplete():
    print( " ".join( actions.keys() ) )
    return 1

if __name__ == '__main__':
    commandHandler()
