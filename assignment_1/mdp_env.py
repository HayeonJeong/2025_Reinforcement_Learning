import numpy as np

states = ["Facebook", "Class1", "Class2", "Class3", "Pub", "Sleep", "Pass"]
n_states = len(states)

# Transition probabilty matrix P[s,s']
P = np.zeros((n_states, n_states))
# Reward vector R[s]
R = np.zeros(n_states)

# --- Transition Probabiltiy ---
# Facebook (0)
P[0, 0] = 0.9
P[0, 1] = 0.1
R[0] = -1

# Class1 (1)
P[1, 0] = 0.5
P[1, 2] = 0.5
R[1] = -2

# Class2 (2)
P[2, 3] = 0.8 # Class3
P[2, 5] = 0.2 # Sleep
R[2] = -2

# Class3 (3)
P[3, 6] = 0.6 # Pass
P[3, 4] = 0.4 # Pub
R[3] = -2

# Pub (4)
P[4, 3] = 0.4 # Class3
P[4, 1] = 0.2 # Class1
P[4, 4] = 0.4 # Stay in Pub
R[4] = +1

# Sleep (5)
P[5, 0] = 1.0 # back to Facebook
R[5] = 0

# Pass (6)
P[6, 5] = 1.0 # go to Sleep
R[6] = +10

# Discount factor
GAMMA = 0.85