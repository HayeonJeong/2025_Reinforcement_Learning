import numpy as np

class RandomWalkEnv:
    def __init__(self, n_states=6):
        self.n_states = n_states
        self.terminal_states = [0, n_states - 1]
        self.rewards = np.zeros(n_states)
        self.rewards[0] = 100
        self.rewards[n_states - 1] = 50
        self.gamma = 1.0 # discount factor
    
    def is_terminal(self, state):
        return state in self.terminal_states

    def get_next_states(self, state, action):
        """
        action: -1 (left), +1 (right)
        returns: next_state, reward, done
        """
        # if the state is a terminal state, return the state and reward
        if self.is_terminal(state):
            return state, self.rewards[state], True
        
        next_state = state + action # move to the next state
        if next_state < 0: # out of left
            next_state = 0 # stay at the leftmost state
        elif next_state >= self.n_states: # out of right
            next_state = self.n_states - 1 # stay at the rightmost state
        
        reward = self.rewards[next_state]
        done = self.is_terminal(next_state)
        return next_state, reward, done
        