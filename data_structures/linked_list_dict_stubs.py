"""
Collection of key-value pair records, implemented as a linked list.
"""
from inspect import isgeneratorfunction
# Name of class MUST be Dictionary
class Dictionary:
	
	"""
	Represents a single item within the linked list.
	"""
	class Node:
		# Initialize dictionary
		def __init__(self, key=None, value=None, next=None):
			self._key = key 
			self._value = value 
			self._next = next

		def getKey(self):
			return self._key

		def getValue(self):
			return self._value

		def insert(self, key, value):
			if self._next == None or key < self._next._key:
				self._next = Dictionary.Node(key, value,self._next)
			elif key > self._next._key:
				self._next.insert(key,value)
			else:
				pass

		def get(self,key):
			if key == self._key:
				foundvalue = self._value
				return foundvalue
			elif key > self._key:
				return self._next.get(key)
			else:
				pass

		def delete(self, head, key):
			if not head:
				return None
			head._next = self.delete(head._next,key)
			if head._key == key:
				return head._next
			else: 
				return head

		def getNext(self):
			return self._next

		def setValue(self,new_value):
			self._value = new_value

		def setNext(self,new_next):
			self._next = new_next

		
		def __iter__(self): #Should iterats over the Nodes in the list
			f = Dictionary()._head
			while f != None:
				yield self
				self = self.getNext()

		def __str__(self):
			return (f'{self.getKey()}:{self.getValue()}')

	# Dictionary methodes start here:
	def __init__(self):
		self._head = None
		self._tail = None
		self._length = 0

	"""
	Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
	"""
	def insert(self, key, value):
		key=str(key)
		if self._head == None or key < self._head._key: 
			self._head = self.Node(key, value, self._head)
			return True
		elif key > self._head._key: 
			self._head.insert(key,value)
			return True
		else:
			return False 

	"""
	Returns value that is identified by `key`, or None if no such key exists.
	"""
#	def get(self, key):
#		self.Node.get(self._head,key)

	def get(self, key):
		key=str(key)
		current=self._head
		foundvalue = None
		while current != None:
			if current.getKey()==key:
				foundvalue = current.getValue()
				break
			else:
				current=current.getNext()
		return foundvalue

	"""
	Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
	"""
	def delete(self, key):
		key=str(key)
		if self._head._key==key:
			self._head=self._head._next
			return True
		elif not self.get(key):
			return False
		else:
			self.Node.delete(self._head,self._head,key)
			return True

	def delete_iter(self, key):
		key=str(key)
		current = self._head
		pre = None
		while current!=None:
			if current.getKey() == key:
				if not pre:
					self._head = current.getNext()
					return True
				else:
					pre.setNext(current.getNext())
					return True
				break
			else:
				pre = current
				current = current.getNext()
		return False
	
	"""
		Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
	"""
	def __iter__(self):
		f=self._head
		while f != None:
			yield (f.getKey(),f.getValue())
			f=f.getNext()
	
	""" Returns a string representation of the key, values in the linked list from the start to the end (sorted).
	"""
	def __str__(self):
		result=[]
		for i in self:
			result.append(str(i))
		return ','.join(result)


if __name__ == "__main__":
	d = Dictionary()
	print(d.insert('b2','3'))
	print(d.insert('c1','2'))
	print(d.insert('a3','4'))

#	print(d.delete('b2'))
	print(d.get('b2'))
#	print(next(d))
	for i in d:
		print(i,end=',')