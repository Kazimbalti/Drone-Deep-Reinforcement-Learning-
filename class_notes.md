# Reinforcement Learning Framework

## Definitions
- Action ($A$): All the possible moves that the agent can take
- State ($S$): Current situation returned by the environment
- Reward ($R$): An immediate return send back from the environment to evaluate the last action.
- Policy ($\pi$): The strategy that the agent employs to determine next action based on the current state
- Value ($V$): The expected long-term return with discount, as opposed to the short-term reward $R$. $V\pi(s)$ is defined as the expected long-term return of the current state sunder policy π
- Q-value or action-value ($Q$): Q-value is similar to Value ($V$), except that it takes an extra parameter, the current action a. Qπ(s, a) refers to the long-term return of the current state s, taking action a under policy π

## Markov Decision Process (MDP)

- a (finite) set of state $S$
- a (finite) set of actions $A$
- a set of rewards $R$
- one-step dynamics of the environment
- a discount rate $\gamma$

## Policy

- $pi: S -> A$
- A deterministic policy maps a state to an action
- $pi: S \times A -> [0, 1]$
- A stochastic policy maps a state to the probability that the agent takes an action

## State-Value Function

- For each state the state-value function yields the expected return if the agent started in that state and then followed the policy for all time steps
- A state-value function always corresponds to a particular policy
- The state-value function is denoted by $v _\pi$

## Optimality

- A policy $\pi'$ is better than or equal to a policy $\pi$ only if its state value function is better than or equal to the state value function for $\pi'$ for all states
- An optimal policy $\pi_*$ satisfies $\pi _* \geq \pi$ for all policies $\pi$
- An optimal policy is guaranteed to exist but may not be unique
- All optimal policies have the same state-value function called the optimal state-value function denoted by $v_*$

## Action-Value Function

- For each state $s$ and action $a$ the action-value function yields the expected return if the agent started in state $s$ then chooses action $a$ and then uses the policy to choose its actions for all time steps
- A action-value function always corresponds to a particular policy
- The action-value function is denoted by $q _\pi$
- All optimal policies have the same action-value function called the optimal state-value function denoted by $q_*$

## Iterative Policy Evaluation

- Updates the Bellman Expectation Equation to work as an iterative function which is then used to estimate the state-value function $v_\pi$
- Takes an MDP environment and a policy $\pi$ outputs a state-value function $v_\pi$

## Policy Improvement

1. Start with random policy $\pi$ from action state
2. Use iterative policy evaluation to get the value function $v _\pi$
3. Construct the action-value function $q _\pi$ from the value function $v _\pi$
4. Use the action-value function $q _\pi$ to get a policy $\pi'$ that is at least as good as policy $\pi$
5. Repeat

## Policy Iteration

TBA

## Episodes

- AN episode is a finite sequence $S_0,A_0,R_1,S_1,A_1,R_2,...,S_T$
- For any episode the agents goal is to find policy $\pi$ to maximise expected cumulative reward

## The Prediction Problem

- Given a policy $\pi$, determine the value function $v_\pi$ by interacting with the environment
- Basis for Monte Carlo Prediction algorithm

## Monte Carlo Methods

### Prediction

- Algorithms that solve the prediction problem determine the value function $v_\pi$ corresponding to a policy $\pi$
- On-policy methods have the agent interact with the environment by following the same policy $\pi$ that it seeks to evaluate
- Off-policy methods have the agent interact with the environment by following a policy $b$ (where $b\neq\pi$) that is different from the policy that it seeks to evaluate

### Generalized Policy Iteration

- Algorithms designed to solve the control problem determine the optimal policy $\pi_*$ from interaction with the environment
- Generalized policy iteration (GPI) refers to the general method of using alternating rounds of policy evaluation and improvement in the search for an optimal policy

### Exploration vs. Exploitation

- All reinforcement learning agents face the Exploration-Exploitation Dilemma, where they must find a way to balance the drive to behave optimally based on their current knowledge (exploitation) and the need to acquire knowledge to attain better judgment (exploration)
- In order for MC control to converge to the optimal policy, the Greedy in the Limit with Infinite Exploration (GLIE) conditions must be met

## Temporal Difference Methods

- Whereas Monte Carlo (MC) prediction methods must wait until the end of an episode to update the value function estimate, temporal-difference (TD) methods update the value function after every time step
- For any fixed policy, one-step TD is guaranteed to converge to the true state-value function, as long as the step-size parameter $\alpha$ is sufficiently small
- In practice, TD prediction converges faster than MC prediction

### Sarso(0)

- Sarsa(0) (or Sarsa) is an on-policy TD control method
- It is guaranteed to converge to the optimal action-value function $q_*$ as long as the step-size parameter $\alpha$ is sufficiently small and \epsilon is chosen to satisfy the Greedy in the Limit with Infinite Exploration (GLIE) condition
- Q-values affected by exploration

### Sarsamax (or Q-Learning)

- Sarsamax is an off-policy TD control method
- Sarsamax is guaranteed to converge to the optimal action value function $q_*$ under the same conditions that guarantee convergence of the Sarsa control algorithm

### Expected Sarsa

- Expected Sarsa is an on-policy TD control method
- Expected Sarsa is guaranteed to converge to the optimal action value function $q_*$ under the same conditions that guarantee convergence of Sarsa and Sarsamax

### Performance

- On-policy TD control methods (like Expected Sarsa and Sarsa) have better online performance than off-policy TD control methods (like Q-learning)
- Expected Sarsa generally achieves better performance than Sarsa

## Deep Q-Learning

- Deep Q-Learning is an algorithm uses deep neural networks to solve reinforcement learning problems
- Especially this with large and continuous state spaces

### Q-Learning

- Q-Learning is an off-policy TD control method that uses one policy to take actions while optimising a seperate policy
- Online performance is poor compared to Sarsa
- Q-values unaffected by exploration

## RL in Continuous Spaces

### Discretisation

- Discretisation can be done by a constant grid, tile coding or coarse coding
- Discretisation leads to an approximation of the value function

### Function Approximation

- Linear function approximation
- Kernel functions
- Non-linear function approximation

## Reference
[Introduction to Various Reinforcement Learning Algorithms. Part I (Q-Learning, SARSA, DQN, DDPG)](https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-i-q-learning-sarsa-dqn-ddpg-72a5e0cb6287)

