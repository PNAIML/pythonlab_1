import numpy as np
import random

# Define the environment
states = ['A', 'B', 'C', 'D']  # Example states
actions = ['left', 'right']    # Possible actions
rewards = {'A': {'left': 1, 'right': 1},
           'B': {'left': 1, 'right': 0},
           'C': {'left': 0, 'right': 1},
           'D': {'left': 0, 'right': 0}}

# Initialize Q-table
Q = {}
for state in states:
    Q[state] = {}
    for action in actions:
        Q[state][action] = 0

# Hyperparameters
alpha = 0.1   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.1 # exploration rate

# Training loop
for episode in range(100):
    state = random.choice(states)
    
    while True:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)  # explore
        else:
            action = max(Q[state], key=Q[state].get)  # exploit

        reward = rewards[state][action]
        next_state = random.choice(states)

        # Q-learning update
        old_value = Q[state][action]
        next_max = max(Q[next_state].values())
        Q[state][action] = old_value + alpha * (reward + gamma * next_max - old_value)

        state = next_state
        if state == 'D':  # terminal condition for simplicity
            break

# Print learned Q-values
for state in Q:
    print(f"{state}: {Q[state]}")



    #Here's a simple example of a reinforcement learning algorithm
    #using Q-learning. We'll simulate a basic environment—a grid
    #world where an agent learns to reach a goal:

#This example is intentionally minimal to illustrate the core idea:
        #learning optimal actions by updating value estimates through
        #trial and error.
