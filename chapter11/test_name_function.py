# -*- coding: utf-8 -*-
'''
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""测试name_function.py"""

	def test_first_last_name(self):
		"""能够正确处理像Jains Joplin这样的姓名吗?"""

		formatted_name = get_formatted_name('jains', 'joplin')
		self.assertEqual(formatted_name, 'Jains Joplin')

unittest.main()

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('jains', 'joplin')
		self.assertEqual(formatted_name, 'Jains Joplin')

unittest.main()
'''
print('''This is a very long string. It continues here.
	And it's not over yet. "Hello.world!"
	Still here.''')
print("This is a very long string. It continues here.\
And it's not over yet. \"Hello.world!\"\
Still here.")

print("This is a very long string. It continues here." + \
	"And it's not over yet. \"Hello.world!\"" + \
	"Still here.")

print('Hello,\
 world!')