import unittest
import animal_sounds

class  TestAnimalSounds(unittest.TestCase):
	
	def test_cow_sounds(self):
		'''What does the cow say'''
		utterance = animal_sounds.cow_say()
		expect = 'moo'
		msg = 'expected %s, got %s'
		msg %= (expected, utterance)
		self.assertEqual(expected, utterance, msg)

