import numpy as np
from game import Game
from qlearning import QLearningAgent

episodes = 5000
agent = QLearningAgent()
game = Game()

for episode in range(episodes):
    state = game.reset()
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = game.step(action)
        agent.update(state, action, reward, next_state)
        state = next_state

game.play(agent)
