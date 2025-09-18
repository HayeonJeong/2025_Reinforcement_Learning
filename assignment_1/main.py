import numpy as np
from mdp_env import P, R, GAMMA
from value_iteration import value_iteration
from q_value_iteration import q_value_iteration

V, v_iters = value_iteration(P, R, GAMMA)
Q, q_iters = q_value_iteration(P, R, GAMMA)

lines = []
lines.append(f"Value Iteration (gamma={GAMMA}):\nV*(s) = {V.tolist()}\niterations = {v_iters}\n")
lines.append(f"Q-Value Iteration (gamma={GAMMA}):\nQ*(s) = {Q[:,0].tolist()}\niterations = {q_iters}\n")

with open("results.txt", "w") as f:
    f.write("\n".join(lines))
