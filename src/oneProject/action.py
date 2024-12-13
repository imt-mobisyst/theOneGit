import os, pathlib
from . import git, cmd

def doList( arguments ):
    target= []
    if len( arguments ) > 1 :
        target= arguments[1:]
    gits= git.makeList(target)
    print( git.stringList(gits) )

def doStatus(arguments):
    RED= '\033[0;31m'
    LIGHT= '\033[1;34m'
    NC= '\033[0m' # No Color

    rootPath= pathlib.Path().absolute()
    gits= git.makeList()
    command= 'git status -sb'

    for depot in gits :
        os.chdir( depot.path )
        print( RED + '> ' + LIGHT + depot.path + NC)
        cmd.execute( command, verbose=False )
        os.chdir( rootPath )

