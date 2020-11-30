## Dictionary ADT ##
## Implemented with BS Tree
"""
Collection of key-value pair records, implemented as a binary search tree.
"""
# Name of class MUST be Dictionary
class Dictionary:
	class Node:
		def __init__(self, key, value, left=None, right=None):
			self._key	= key
			self._value  = value
			self._lchild   = left
			self._rchild  = right

		def getKey(self):
			return self._key

		def getValue(self):
			return self._value
			
		def insert(self, root, key, data):
			if not root:
				return Dictionary.Node(key,data)
			if key < root._key:
				root._lchild = root.insert(root._lchild, key, data)
			elif key > root._key:
				root._rchild = root.insert(root._rchild, key, data)
			return root

		def get(self):
			return (self._value[0],self._value[1])

		def delete(self,key,node,tree):
			if tree._root._key==key:
				if not tree._root._lchild:
					tree._root=tree._root._rchild
				elif not tree._root._rchild:
					tree._root=tree._root._lchild
				else:
					self._delete(key,node)
			else:
				self._delete(key,node)

		def _delete(self,key,node):
			if not node:
				print('can\'t find')
			else:
				if key < node._key:
					node._lchild = self._delete(key, node._lchild)
				elif key > node._key:
					node._rchild = self._delete(key, node._rchild)
				else:
					# 2 nodes
					if node._lchild and node._rchild:  
						tmp = self._find_extremum(node._lchild)
						node._key = tmp._key
						node._value = tmp._value
						node._lchild = self._delete(tmp._key, node._lchild)
					# 1 or 0 nodes
					else:
						if node._lchild is None:
							node = node._rchild
						else:
							node = node._lchild
			return node

		def _find_extremum(self, node, by='max'):
			if by=='max':
				while node._rchild:
					node = node._rchild
			elif by=='min':
				while node._lchild:
					node = node._lchild
			return node

		def search(self, node, key):
			if node is None:
				return None
			elif node._key > key:
				return self.search(node._lchild, key)
			elif node._key < key:
				return self.search(node._rchild, key)
			else:
				return (node._value, node._key, node)

		def inorder_trav(self,node,tree):
			if not node:
				return
			node.inorder_trav(node._lchild,tree)
			tree._nodesList.append(node)
			node.inorder_trav(node._rchild,tree)
		
		def getNext(self,tree):
			return next(tree._nodesList)

		def __iter__(self): #Should iterats over the Nodes in the tree
			if self._lchild:
				for x in self._lchild:
					yield x
			yield self
			if self._rchild:
				for x in self._rchild:
					yield x

		def __str__(self):
			return (f'{self.getKey()}:{self.getValue()}')
		

		
		def __getSmallest(self):	  # Method used by __delete (optional)
			pass   # Abstract method, add your own
		
# Dictionary methods start here:
	def __init__(self,root=None):
		self._root = root
		self._nodesCount = 0
		self._nodesList=[]

	"""
	Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
	"""
	def insert(self, key, value):
		key=str(key)
		if self.get(key) != None:
			return False
		if self._nodesCount == 0:
			self._root=self.Node.insert(self._root,self._root,key,value)
		else:
			self.Node.insert(self._root,self._root,key,value)
		self._nodesCount +=1
		self._nodesList.clear()
		self.Node.inorder_trav(self._root,self._root,self)
		return True

	"""
	Returns value that is identified by `key`, or None if no such key exists.
	"""
	def get(self, key):
		key=str(key)
		t=self.Node.search(self._root, self._root, key)
		if t!=None:
			return t[0]
		else:
			return None


	"""
	Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
	"""
	def delete(self, key):
		key=str(key)
		t=self.Node.search(self._root, self._root, key)
		if t!=None:
			self._root.delete(key,self._root,self)
			delnode=t[2]
			del delnode
			self._nodesCount -=1
			self._nodesList.clear()
			self.Node.inorder_trav(self._root,self._root,self)
			return True
		else:
			return False
	
	"""
		Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
	"""
	def __iter__(self):
		for x in self._root:
			yield (x._key,x._value)

			

	""" Returns a string representation of the key, values in the tree in order after key value (smallest to largest)
	"""
	def __str__(self):
		result=[]
		for i in self._nodesList:
			result.append('{'+str(i)+'}')
		return ','.join(result)	

if __name__ == "__main__":
	d = Dictionary()
	d.insert("key1", "value1")
	d.insert("key2", "value2")
	d.insert("key3", "value3")
	d.insert("key4", "value4")
	print(d.delete("key1"))
	print(d.get('key1'))

#	print(d)

	for i in d:
		print(i)