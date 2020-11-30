# https://docs.python.org/3/library/unittest.html
import unittest
# To test if object is iterable
from collections.abc import Iterable

# Import exactly one implementation of Dictionary:
#from linked_list_dict_stubs import Dictionary
from search_tree_dict_stubs import Dictionary

# Test the expected Dictionary API using Python"s built-in unittest system
class DictionaryTest(unittest.TestCase):
	def testEmpty(self):
		d = Dictionary()
		self.assertIsNone(d.get("foo"), "get for non-existent key should return None")

	def testInsertGet(self):
		d = Dictionary()
		d.insert("key1", "value1")
		d.insert("key2", "value2")
		d.insert("key3", "value3")
		self.assertEqual(d.get("key1"), "value1", "get first key should return correct value")
		self.assertEqual(d.get("key2"), "value2", "get second key should return correct value")
		self.assertEqual(d.get("key3"), "value3", "get third key should return correct value")
		self.assertIsNone(d.get("foo"), "get for non-existent key should return None")

	def testDelete(self):
		d = Dictionary()
		d.insert("key1", "value1")
		d.insert("key2", "value2")
		d.insert("key3", "value3")
		r1 = d.delete("key2")
		self.assertTrue(r1, "delete should return True when successful")
		self.assertIsNone(d.get("key2"), "get for deleted key should return None")
		self.assertEqual(d.get("key1"), "value1", "get first key should return correct value")
		self.assertEqual(d.get("key3"), "value3", "get third key should return correct value")
		self.assertFalse(d.delete("keyMissing"), "delete should return False for non-existent key")

	def testDeleteFirst(self):
		d = Dictionary()
		d.insert("key1", "value1")
		d.insert("key2", "value2")
		d.insert("key3", "value3")
		d.delete("key1")

		self.assertIsNone(d.get("key1"), "get for deleted key should return None")
		self.assertEqual(d.get("key2"), "value2", "get second key should return correct value")
		self.assertEqual(d.get("key3"), "value3", "get third key should return correct value")

	def testInsertDuplicateKey(self):
		d = Dictionary()
		r1 = d.insert("key1", "value1 - try 1")
		r2 = d.insert("key1", "value1 - try 2")
		self.assertTrue(r1, "insert should return True if successful")
		self.assertFalse(r2, "insert should return False for duplicate key")
		self.assertEqual(d.get('key1'), "value1 - try 1", "get should return correct value")
		d.delete("key1")
		self.assertIsNone(d.get("key1"), "get for deleted key should return None")

	def testStr(self):
		d = Dictionary()
		d.insert("key1", "value1")
		s = str(d)
		self.assertIn("key1", s, "string representation includes key")
		self.assertIn("value1", s, "string representation includes value")

	def testIter(self):
		d = Dictionary()
		d.insert("key1", "value1")
		d.insert("key2", "value2")
		d.insert("key3", "value3")
		self.assertIsInstance(d, Iterable, "Dictionary instance should be iterable (did you implement __iter__ method?)")
		count = 0
		for item in d:
			count += 1
		self.assertEqual(count, 3, "Iterating over dictionary gives correct number of iterations")

	def testIterOrder(self):
		d = Dictionary()
		d.insert("key3", "value3")
		d.insert("key2", "value2")
		d.insert("key1", "value1")
		prevKey = None
		for (key, value) in d:
			if prevKey:
				self.assertGreater(key, prevKey, "iterating over Dictionary should be ascending key order")
				prevKey = key

if __name__ == "__main__":
	unittest.main()
