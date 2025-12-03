import numpy as np

class Game:
    def __init__(self):
        self.position = 0
        self.goal = 10

    def reset(self):
        self.position = 0
        return self.position

    def step(self, action):
        if action == 1:
            self.position += 1
        else:
            self.position -= 1

        if self.position == self.goal:
            return self.position, 1, True

        if self.position < 0:
            return self.position, -1, True

        return self.position, 0, False

    def play(self, agent):
        state = self.reset()
        done = False

        while not done:
            action = agent.choose_action(state)
            state, _, done = self.step(action)
            print("Position:", state)
