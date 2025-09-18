"""
Iteratively update the action-value function Q(s, a) using the Bellman equation,
to find the optimal action-value function Q*(s, a),
until convergence (|Q(s, a) - Q*(s, a)| < epsilon).
"""

import numpy as np

def q_value_iteration(P, R, GAMMA=0.85, epsilon=1e-4, max_iterations=1000):
    n_states, _ = P.shape
    # 단일 행동 가정: (n_states, 1) 크기의 Q
    Q = np.zeros((n_states, 1))

    for i in range(max_iterations):
        delta = 0.0
        Q_new = np.zeros_like(Q)

        for s in range(n_states):
            Q_new[s, 0] = R[s] + GAMMA * np.dot(P[s], Q[:, 0])
            delta = max(delta, abs(Q_new[s, 0] - Q[s, 0]))

        Q = Q_new
        if delta < epsilon:
            break
    
    return Q, i + 1 # Q*(s, a), number of iterations