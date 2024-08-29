from . import action

def doHelp( arguments ):
	print( "help" )

actions= { "help":doHelp, "list":action.doList, "status":action.doStatus }
