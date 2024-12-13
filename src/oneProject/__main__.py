import sys
from . import actions
from .complete import doComplete

def commandHandler():
    action= "help"
    arguments= ["help"]
    if len(sys.argv) > 1 :
        action= sys.argv[1]
        arguments= sys.argv[1:]
    
    if action == 'complete' :
        doComplete( arguments )
    elif action in actions.keys() :
        actions[action]( arguments )
    else :
        actions["help"]( arguments )
    return 1

def commandComplete():
    print( " ".join( actions.keys() ) )
    return 1

if __name__ == '__main__':
    commandHandler()
