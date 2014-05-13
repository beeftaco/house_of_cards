import os, sys
print sys.path
print os.path.join(__file__,"../..")
import unittest
from cards.common.card_deck import Card

class TestCard(unittest.TestCase):

	def test_fail(self):
		self.assertEqual(True,True)

	def test_constructor(self):
		card = Card()
		self.assertIsInstance(card,Card)


if __name__ == "__main__":
	unittest.main()