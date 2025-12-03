import unittest
from qlearning import QLearningAgent

class TestQLearning(unittest.TestCase):
    def test_q_initialization(self):
        agent = QLearningAgent()
        q = agent.get_q(0, 1)
        self.assertEqual(q, 0)

    def test_q_update(self):
        agent = QLearningAgent(lr=0.5, gamma=0.9, epsilon=0)
        agent.update(0, 1, 1, 1)
        q = agent.get_q(0, 1)
        self.assertNotEqual(q, 0)

    def test_choose_action_exploit(self):
        agent = QLearningAgent(epsilon=0)
        agent.q_table[(0,0)] = 1
        agent.q_table[(0,1)] = 0
        action = agent.choose_action(0)
        self.assertEqual(action, 0)

    def test_choose_action_explore(self):
        agent = QLearningAgent(epsilon=1)
        actions = set(agent.choose_action(0) for _ in range(20))
        self.assertTrue(0 in actions and 1 in actions)

if __name__ == "__main__":
    unittest.main()
