import unittest

import guessing_game

class TestGuessing(unittest.TestCase):

    def test_guessing3(self):
        guess = 5
        answer = 5
        result = guessing_game.guessing_game(guess, answer)
        self.assertTrue(result)


    def test_guessing2(self):
        guess = 11
        answer = 5
        result = guessing_game.guessing_game(guess, answer)
        self.assertFalse(result)


   # def test_guessing(self):
    #    result = guessing_game.guessing_game('11', 5)
     #   self.assertFalse(result)

  #  def test_guessing1(self):
   #     result = guessing_game.guessing_game(None,5)
    #    self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()