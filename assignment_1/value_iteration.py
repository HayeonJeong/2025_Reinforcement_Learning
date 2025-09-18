"""
Iteratively update the value function V(s) using the Bellman equation,
to find the optimal value function V*(s),
until convergence (|V(s) - V*(s)| < epsilon).
"""

import numpy as np

def value_iteration(P, R, GAMMA=0.85, epsilon=1e-4, max_iterations=1000):
    n_states = len(R)
    V = np.zeros(n_states)

    for i in range(max_iterations):
        delta = 0.0
        V_new = np.zeros(n_states)
        for s in range(n_states):
            # Bellman optimality for MRP (no explicit actions):
            # V(s) = R(s) + gamma * sum_{s'} P(s, s') * V(s')
            V_new[s] = R[s] + GAMMA * np.dot(P[s], V)
            delta = max(delta, abs(V_new[s] - V[s]))
        V = V_new
        if delta < epsilon:
            break

    return V, i + 1 # V*(s), number of iterations