import numpy as np
import pickle
import gymnasium as gym
import matplotlib.pyplot as plt

def generate_custom_map(size, num_potholes):
    assert size >= 4, "Size must be at least 4"
    assert num_potholes < (size ** 2) - 3, "Too many potholes for the given size"

    # Create a map with all frozen tiles
    custom_map = np.full((size, size), 'F')

    # Set the starting point and the goal
    custom_map[0, 0] = 'S'
    custom_map[size - 1, size - 1] = 'G'

    # Randomly place potholes
    pothole_indices = np.random.choice(range(size*size), num_potholes, replace=False)
    row_indices, col_indices = np.unravel_index(pothole_indices, (size, size))
    custom_map[row_indices, col_indices] = 'H'

    return custom_map.tolist()

def run_q_custom_env(episodes, custom_map, is_training= True, render=False):

    env = gym.make('FrozenLake-v1', desc=custom_map , is_slippery=False, render_mode='human' if render else None)

    if(is_training):
        q = np.zeros((env.observation_space.n, env.action_space.n))
    else: 
        f = open('frozen_lake8x8Custom_qTable.pkl', 'rb')
        q = pickle.load(f)
        f.close()

    learning_rate = 0.1
    discount_factor = 0.9

    epsilon = 1
    epsilon_decay = 0.0001
    rng = np.random.default_rng()

    rewards_per_episode = np.zeros(episodes)

    for episode in range(episodes):
        state = env.reset()[0]
        truncated = False
        terminated = False

        while (not truncated and not terminated):
            if is_training and  rng.random() < epsilon:
                action = env.action_space.sample()  # A random action is being taken

            else:
                action = np.argmax(q[state, :])

            new_state, reward, terminated, truncated, _ = env.step(action)

            if is_training:
                q[state, action] = q[state, action] + learning_rate * (
                        reward + discount_factor * np.max(q[new_state, :]) - q[state, action]
                )

            state = new_state

        epsilon = max(epsilon - epsilon_decay, 0)

        if epsilon == 0:
            learning_rate = 0.0001

        if reward == 1:
            rewards_per_episode[episode] = 1

    env.close()

    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        sum_rewards[t] = np.sum(rewards_per_episode[max(0, t-100):(t+1)])
    plt.plot(sum_rewards)
    plt.savefig('frozen_lake8x8Custom.png')

    if is_training:
        f = open('frozen_lake8x8Custom_qTable.pkl', "wb")
        pickle.dump(q, f)
        f.close()

if __name__ == "__main__":
    custom_map = generate_custom_map(8, 8)
    print(custom_map)
    run_q_custom_env(15000, custom_map)
    run_q_custom_env(1,custom_map, is_training= False, render=True)