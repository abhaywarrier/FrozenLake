# FrozenLake

## Level 1: 
### The FrozenLake: (GYM ENVIRONMENT)
The agent navigates a grid-like frozen lake and tries to reach a goal tile without falling into holes. The observation
space in this environment is discrete. The observation space consists of a single discrete variable representing the
current tile the agent is on. The tiles can have the following discrete values:
1. Frozen (F): The tile is frozen and safe to step on.
2. Hole (H): The tile is a hole, and if the agent steps on it, it falls into the hole and fails.
3. Start (S): The tile is the starting point for the agent.
4. Goal (G): The tile is the goal, and if the agent reaches it, it succeeds.

The agent receives one of these discrete observations at each time step, indicating the current tile it is occupying. It
can use this information to determine its position in the environment and make decisions on which action to take.

## Level 2: 
## The FrozenLake: Building Custom Environment
In this level we are extending frozen lake problem to 8 * 8 challenge, where in the number of pot holes is increased to 8.
The pot holes are randoly generated but the starting and ending stay the same as level 1. 
The tiles can have the following discrete values:

1. Frozen (F): The tile is frozen and safe to step on.
2. Hole (H): The tile is a hole, and if the agent steps on it, it falls into the hole and fails.
3. Start (S): The tile is the starting point for the agent
4. Goal (G): The tile is the goal, and if the agent reaches it, it succeeds.
