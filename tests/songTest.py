import unittest
import musicalLake.song as ts

class TestSong(unittest.TestCase):
	def testBrrSong(self):
		test_song = ts.singsong("brr")
		self.assertEqual(test_song,"fiu, cric-cric, brrah, \n")
		
class TestSong(unittest.TestCase):
	def testPepSong(self):
		test_song = ts.singsong("pep")
		self.assertEqual(test_song,"birip, trri-trri, croac, \n")

class TestSong(unittest.TestCase):
	def testBriBriSong(self):
		test_song = ts.singsong("bri-bri")
		self.assertEqual(test_song,"plop, cric-cric, brrah, \n")

if __name__ == '__main__':
	unittest.main()
		
