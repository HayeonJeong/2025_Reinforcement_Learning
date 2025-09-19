import numpy as np
from env import RandomWalkEnv

def q_evaluation(env, V):
    """
    Action-value evaluation: Q(s, a)
    """
    Q = np.zeros((env.n_states, 2)) # actions: 0=left(-1), 1=right(+1)

    for s in range(env.n_states):
        if env.is_terminal(s):
            continue
        
        for action in [-1, +1]:
            next_state, reward, done = env.get_next_states(s, action)
            action_idx = 0 if action == -1 else 1  # -1 -> 0 (left), +1 -> 1 (right)
            Q[s, action_idx] = reward + env.gamma * V[next_state]
    return Q