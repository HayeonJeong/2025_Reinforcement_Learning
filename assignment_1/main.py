import os
import numpy as np
from mdp_env import P, R, GAMMA, states
from value_iteration import value_iteration
from q_value_iteration import q_value_iteration

# Use a shared epsilon for both algorithms so we can report a consistent bound
EPSILON = 1e-4

V, v_iters = value_iteration(P, R, GAMMA, epsilon=EPSILON)
Q, q_iters = q_value_iteration(P, R, GAMMA, epsilon=EPSILON)

# Build human-readable lines with state names
lines = []
lines.append(f"Problem 1 — Value Iteration (gamma={GAMMA}, epsilon={EPSILON}):")
for s_name, v in zip(states, V.tolist()):
    lines.append(f"  V*({s_name}) = {v:.6f}")
lines.append(f"iterations = {v_iters}")

# Theoretical upper bound on iterations using contraction mapping bound
# k >= log( epsilon*(1-gamma)/R_max ) / log(gamma)
R_max = float(np.max(np.abs(R)))
if 0 < GAMMA < 1 and R_max > 0:
    bound_raw = np.log(EPSILON * (1.0 - GAMMA) / R_max) / np.log(GAMMA)
    k_upper_bound = int(np.ceil(bound_raw))
    # Guard against negative due to already-tight initial V
    k_upper_bound = max(0, k_upper_bound)
else:
    k_upper_bound = 0

lines.append(f"upper_bound ≲ {k_upper_bound}\n")

# Separator between problems
lines.append("-" * 60)
lines.append("")

lines.append(f"Problem 2 — Q-Value Iteration (gamma={GAMMA}, epsilon={EPSILON}):")
# Single-action assumption: Q has shape (n_states, 1)
for s_name, q in zip(states, Q[:, 0].tolist()):
    lines.append(f"  Q*({s_name}, a=0) = {q:.6f}")
lines.append(f"iterations = {q_iters}\n")

# Separator between problems
lines.append("-" * 60)
lines.append("")

# Problem 3 — Analysis: iteration counts vs. theoretical upper bound
# Epsilon sweep: run for multiple epsilons and report iterations and bounds
lines.append("Problem 3 — Analysis (epsilon sweep):")
EPSILONS = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]

lines.append("  Epsilon sweep (Value Iteration):")
for eps in EPSILONS:
    _, vi = value_iteration(P, R, GAMMA, epsilon=eps)
    if 0 < GAMMA < 1 and R_max > 0:
        bound = int(np.ceil(np.log(eps * (1.0 - GAMMA) / R_max) / np.log(GAMMA)))
        bound = max(0, bound)
    else:
        bound = 0
    lines.append(f"  epsilon={eps:.0e} -> iterations={vi}, upper_bound≈{bound}")

lines.append("\n  Epsilon sweep (Q-Value Iteration):")
for eps in EPSILONS:
    _, qi = q_value_iteration(P, R, GAMMA, epsilon=eps)
    lines.append(f"  epsilon={eps:.0e} -> iterations={qi}")

output = "\n".join(lines)
# print(output)

results_path = os.path.join(os.getcwd(), "results.txt")

with open(results_path, "w") as f:
    f.write(output)

print(f"Results saved to: {results_path}")
