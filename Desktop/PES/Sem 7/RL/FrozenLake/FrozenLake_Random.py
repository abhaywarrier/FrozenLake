import gym

environment_name = 'FrozenLake-v1'
env = gym.make(environment_name, render_mode= 'ansi')

episodes = 1000
score = 0

for episode in range(episodes):
    state = env.reset()
    done = False
    path_taken = []  # List to store states for the current episode

    while not done:
        env.render()

        action = env.action_space.sample()

        next_state, reward, done, _, _ = env.step(action)

        path_taken.append(state)  # Record the current state

        score += reward

        state = next_state
    if reward == 1.0:
        # Convert byte strings to regular strings and extract state information from tuples
        readable_path = [
            state[1].decode('utf-8') if isinstance(state, tuple) and isinstance(state[1], bytes) else
            env.desc[state // env.ncol, state % env.ncol].decode('utf-8') if isinstance(state, int) else
            state for state in path_taken
        ]
        readable_path.append("G")
        print("Path taken during the episode with reward 1:", readable_path)

print(f"The score for {episodes} episodes is :{score}")
env.close()
