import unittest
from game import Game

class TestGame(unittest.TestCase):
    def test_reset(self):
        g = Game()
        state = g.reset()
        self.assertEqual(state, 0)

    def test_step_forward(self):
        g = Game()
        g.reset()
        state, reward, done = g.step(1)
        self.assertEqual(state, 1)
        self.assertEqual(reward, 0)
        self.assertFalse(done)

    def test_step_backward_out_of_bounds(self):
        g = Game()
        g.reset()
        state, reward, done = g.step(0)
        self.assertEqual(state, -1)
        self.assertEqual(reward, -1)
        self.assertTrue(done)

    def test_goal_reached(self):
        g = Game()
        g.position = 9
        state, reward, done = g.step(1)
        self.assertEqual(state, 10)
        self.assertEqual(reward, 1)
        self.assertTrue(done)

if __name__ == "__main__":
    unittest.main()
