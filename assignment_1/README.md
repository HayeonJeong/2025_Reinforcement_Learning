## Assignment 1: Value Iteration and Q-Value Iteration

This assignment implements Value Iteration and Q-Value Iteration in a discrete MDP environment and computes the converged optimal value functions V* and Q*.

### Files
- `mdp_env.py`: Simple MDP environment defining transition probabilities `P`, rewards `R`, and discount factor `GAMMA`
- `value_iteration.py`: Implementation of `value_iteration(P, R, gamma)`
- `q_value_iteration.py`: Implementation of `q_value_iteration(P, R, gamma)`
- `main.py`: Runs both algorithms and saves results to a file
- `results.txt`: Summary of results generated after running

### How to Run
From the project root, execute the following to run the code under `assignment_1`:
```bash
python 2025rl/assignment_1/main.py
```

### Output
- A `results.txt` file is generated with:
  - Problem 1 — Value Iteration (gamma, epsilon), `V*(s)` and iterations, plus an iteration upper bound
  - Problem 2 — Q-Value Iteration (gamma, epsilon), `Q*(s,a)` and iterations
  - Problem 3 — Analysis (epsilon sweep): iterations vs. theoretical upper bound

Example (abridged):
```text
Problem 1 — Value Iteration (gamma=..., epsilon=...):
  V*(...) = ...
iterations = ...
upper_bound ≲ ...
------------------------------------------------------------
Problem 2 — Q-Value Iteration (gamma=..., epsilon=...):
  Q*(..., a=0) = ...
iterations = ...
------------------------------------------------------------
Problem 3 — Analysis (epsilon sweep):
  Epsilon sweep (Value Iteration):
    epsilon=1e-04 -> iterations=..., upper_bound≈...
  Epsilon sweep (Q-Value Iteration):
    epsilon=1e-04 -> iterations=...
```

### Notes
- Convergence criteria and initialization are defined in each implementation file.
- You can modify the environment (`P`, `R`, `GAMMA`) to explore convergence under different settings.
