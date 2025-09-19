import numpy as np
from env import RandomWalkEnv

def value_iteration(env, theta=1e-6, max_iterations=1000):
    """
    State-value function using value iteration
    """
    V = np.zeros(env.n_states)
    # fixed reward for terminal states
    V[0] = env.rewards[0]
    V[-1] = env.rewards[-1]

    for i in range(max_iterations):
        delta = 0.0
        new_V = V.copy()

        for s in range(env.n_states):
            # skip terminal states
            if env.is_terminal(s):
                continue 
            
            # random policy: left(-1), right(+1) -> both 0.5 probability
            v = 0
            for action in [-1, +1]:
                next_state, reward, done = env.get_next_states(s, action)
                if done:
                    v += 0.5 * reward  # 터미널 상태: 미래 보상 없음
                else:
                    v += 0.5 * (reward + env.gamma * V[next_state])  # 비터미널 상태: 미래 보상 포함
            
            new_V[s] = v
            delta = max(delta, abs(new_V[s] - V[s]))

        V = new_V
        if delta < theta:
            break
    return V