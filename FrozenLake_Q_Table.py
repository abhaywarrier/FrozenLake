import numpy as np
import pickle
import gymnasium as gym
import matplotlib.pyplot as plt

def run_q(episodes, is_training= True, render=False):

    env = gym.make('FrozenLake-v1', map_name='4x4' , is_slippery=False, render_mode='human' if render else None)

    if(is_training):
        q = np.zeros((env.observation_space.n, env.action_space.n))
    else: 
        f = open('frozen_lake4x4_qTable.pkl', 'rb')
        q = pickle.load(f)
        f.close()

    learning_rate = 0.9
    discount_factor = 0.9

    epsilon = 1
    epsilon_decay = 0.001
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
    plt.savefig('frozen_lake4x4.png')

    if is_training:
        f = open('frozen_lake4x4_qTable.pkl', "wb")
        pickle.dump(q, f)
        f.close()


if __name__ == '__main__':
    run_q(1500 ,is_training= False)