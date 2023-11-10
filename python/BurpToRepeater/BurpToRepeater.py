from burp import IBurpExtender
from burp import IHttpListener


class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        # Keep a reference to the callbacks object
        self._callbacks = callbacks

        # Obtain an instance of IExtensionHelpers
        self._helpers = callbacks.getHelpers()

        # Set the extension name
        callbacks.setExtensionName("RepeaterHistoryToProxy")

        # Register for HTTP events to capture repeater history
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # Check if the tool is the Repeater
        if toolFlag == self._callbacks.TOOL_REPEATER:
            # Check if it's a response message
            if not messageIsRequest:
                # Get the proxy history and add the repeater history to it
                proxyHistory = self._callbacks.getProxyHistory()
                proxyHistory.addEntry(messageInfo)


# Instantiate the extension
burp_extender = BurpExtender()
