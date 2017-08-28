import collections

class PyEventEmitter:
	
	def __init__(self):
		self._arr=collections.defaultdict(list)

	def on(self,event):
		def _on(evthandler):
			self._arr[event].append(evthandler)
			print (len(self._arr[event])," listeners for this event")
		return _on


	def emit(self,event,data=None):
		for f in self._arr[event]:
			f(data)
		
	def getListeners(self,event):
		return self._arr[event]

	def getEventsList(self):
		return list(self._arr.keys())

	def getEventsCount(self):
		return len(self._arr)

	def delListenerByName(self,event,fname):
		eventscopy=self._arr[event]
		for i in eventscopy:
			if i.__name__==fname:
				self._arr[event].remove(i)	
	def delAllListeners(self,event):
		del self._arr[event]



