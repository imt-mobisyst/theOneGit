from . import actions

def doComplete( arguments ):
	if len(arguments) < 3:
		return 0
	cmd= arguments[1]
	toComplete= arguments[2]
	if cmd == 'one' :
		for a in actions :
			print( a )