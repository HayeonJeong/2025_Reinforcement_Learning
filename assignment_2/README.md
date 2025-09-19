# Value Iteration in Random Walk

## Overview
This assignment implements **Dynamic Programming** methods in a simple **Random Walk environment**.  
The task is divided into two parts:  

1. **State Value Evaluation (V(s))**  
   - Given a random policy (equal probability of moving left or right).  
   - Compute the expected return for each state using **iterative policy evaluation**.  
   - Terminal states give rewards: `100` (left end) and `50` (right end).  
   - Discount factor is set to γ = 1.0.  

2. **Action Value Evaluation (Q(s,a))**  
   - After obtaining the converged state values `V(s)`, compute the action-value function.  
   - `Q(s,a)` is derived from the Bellman expectation equation:  
     \[
     Q(s,a) = \sum_{s'} P(s'|s,a) \big( R(s,a,s') + \gamma V(s') \big)
     \]  
   - This requires no further iteration once `V(s)` is known.  

## Files
- `env.py`: Random Walk environment implementation.  
- `value_iteration.py`: Iterative evaluation of state values.  
- `q_evaluation.py`: Action-value computation using the final `V(s)`.  
- `main.py`: Entry point to run the experiments and print results.  

## Goal
- Understand the difference between **state value iteration** and **action-value evaluation**.  
- Practice implementing Dynamic Programming methods in a simple MDP.  
