# FrozenLake

## Level 1: 
### The FrozenLake: (GYM ENVIRONMENT)
The space current in agent tile this the navigates agent environment a is on. grid-like is The discrete. tiles frozen can The lake have and the obseryation tries to following space reach a discrete consists goal tile of values: a Without single falling discrete into variable holes. The representing observation the
1. Frozen (F): The tile is frozen and safe to step on.
2. Hole (H): The tile is a hole, and if the agent steps on it, it falls into the hole and fails.
3. Start (S): The tile is the starting point for the agent
4. Goal (G): The tile is the goal, and if the agent reaches it, it succeeds.
The agent receives one of these discrete observations at each time step, indicating the current tile it is occupying. It
can use this information to determine its position in the environment and make decisions on which action to take.
