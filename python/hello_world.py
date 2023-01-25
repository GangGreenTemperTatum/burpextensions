from burp import IBurpExtender

class BurpExtender(IBurpExtender):
	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		callbacks.setExtensionName("Hello World")
		print( "Hello World extension loaded." )
		return
