import numpy as np

class QLearningAgent:
    def __init__(self, lr=0.1, gamma=0.9, epsilon=0.2):
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0)

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice([0, 1])
        qs = [self.get_q(state, a) for a in [0, 1]]
        return int(np.argmax(qs))

    def update(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        next_max = max(self.get_q(next_state, a) for a in [0, 1])
        new_q = old_q + self.lr * (reward + self.gamma * next_max - old_q)
        self.q_table[(state, action)] = new_q
