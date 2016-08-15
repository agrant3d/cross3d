##
#   :namespace  cross3d.maya
#
#   :remarks    The cross3d.maya package contains the necessary classes to control Maya.
#
#   :author     mikeh
#   :author     Blur Studio
#   :date       09/10/14
#

import external

def test():
	try:
		import maya.cmds
	except ImportError:
		return False
	return True

def init():

	# Importing the layer's classes.
	import mayaexceptionrouter
	import mayauserprops
	import mayaapplication
	import mayascene
	import mayascenewrapper
	import mayasceneobject
	import mayagroup
	import mayascenemodel
	import mayascenecamera
	import mayasceneviewport
	import mayascenematerial
	import collection
