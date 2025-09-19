from env import RandomWalkEnv
from value_iteration import value_iteration
from q_evaluation import q_evaluation

import os
import numpy as np

if __name__ == "__main__":
    env = RandomWalkEnv(n_states=6)

    # Q2.1: Value Iteration
    V = value_iteration(env)
    
    # Q2.2: Action Value Evaluation
    Q = q_evaluation(env, V)
    
    # Save results to file
    with open("results.txt", "w") as f:
        f.write("Final State Values V(s):\n")
        for s in range(env.n_states):
            f.write(f"V({s}) = {V[s]:.2f}\n")
        
        f.write("\nAction-Value Function Q(s,a):\n")
        for s in range(env.n_states):
            if env.is_terminal(s):
                f.write(f"State {s}: Left=N/A, Right=N/A (Terminal)\n")
            else:
                f.write(f"State {s}: Left={Q[s,0]:.2f}, Right={Q[s,1]:.2f}\n")