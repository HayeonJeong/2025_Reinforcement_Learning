## Assignment 1: Value Iteration and Q-Value Iteration

This assignment implements Value Iteration and Q-Value Iteration in a discrete MDP environment and computes the converged optimal value functions V* and Q*.

### Files
- `mdp_env.py`: Simple MDP environment defining transition probabilities `P`, rewards `R`, and discount factor `GAMMA`
- `value_iteration.py`: Implementation of `value_iteration(P, R, gamma)`
- `q_value_iteration.py`: Implementation of `q_value_iteration(P, R, gamma)`
- `main.py`: Runs both algorithms and saves results to a file
- `results.txt`: Summary of results generated after running

### Requirements
- Python 3.9+
- NumPy

Installation example:
```bash
pip install numpy
```

### How to Run
From the project root, execute the following to run the code under `assignment_1`:
```bash
python 2025rl/assignment_1/main.py
```

### Output
- A `results.txt` file will be generated containing:
  - Converged `V*(s)` and the number of iterations for Value Iteration
  - Converged `Q*(s, a)` (showing one action column, e.g., `a=0`) and the number of iterations for Q-Value Iteration

Example (format):
```text
Value Iteration (gamma=...):
V*(s) = [...]
iterations = ...

Q-Value Iteration (gamma=...):
Q*(s) = [...]
iterations = ...
```

### Notes
- Convergence criteria and initialization are defined in each implementation file.
- You can modify the environment (`P`, `R`, `GAMMA`) to explore convergence under different settings.
