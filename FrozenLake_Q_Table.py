import gym 
import torch

environment_name = 'FrozenLake-v0'
env = gym.make(environment_name)

number_of_states = env.observation_space.n
number_of_actions = env.action_space.n

steps_total = []
rewards_total = []
egreedy_total = []

gamma = 0.95
learning_rate = 0.9

egreedy = 0.7
egreedy_final = 0.1
egreedy_decay = 0.999

Q = torch.zeros([number_of_states, number_of_actions])
print(f"The Q table before updation is:\n {Q}")

print(" ")

episodes = 1000
score = 0

for i_episode in range(episodes):
    
    # resets the environment
    state = env.reset()
    step = 0

    while True:
        
        step += 1
        
        random_for_egreedy = torch.rand(1)[0]
        

        if random_for_egreedy > egreedy:      
            random_values = Q[state] + torch.rand(1,number_of_actions) / 1000      
            action = torch.max(random_values,1)[1][0]  
            action = action.item()
        else:
            action = env.action_space.sample()
            
        if egreedy > egreedy_final:
            egreedy *= egreedy_decay
        
        new_state, reward, done, info = env.step(action)

        # Filling the Q Table
        Q[state, action] = reward + gamma * torch.max(Q[new_state])

        score += reward
        
        # Setting new state for next action
        state = new_state
        
        # env.render()
        # time.sleep(0.4)
        
        if done:
            steps_total.append(step)
            rewards_total.append(reward)
            egreedy_total.append(egreedy)
            if reward == 1.0:
                print('Episode: {} Reward: {} Steps Taken: {}'.format(i_episode,reward, step))
            break

print(f"The score for {episodes} episodes is :{score}")
env.close()

print(" ")

print(f"The Q table after updation is:\n {Q}")