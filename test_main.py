import unittest
from game import Game
from qlearning import QLearningAgent

class TestIntegration(unittest.TestCase):
    def test_training_runs(self):
        agent = QLearningAgent()
        game = Game()
        for _ in range(50):
            state = game.reset()
            done = False
            while not done:
                action = agent.choose_action(state)
                state, reward, done = game.step(action)
                agent.update(state, action, reward, state)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
