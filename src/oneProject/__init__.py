from . import action
import sys, os

def doHelp( arguments ):
	print( "help" )

actions= {
	"help":doHelp,
	"list":action.doList,
	"status":action.doStatus
}
