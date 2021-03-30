import sys
import os
import math
import numpy as np
import pickle
#from agents.policy_search import PolicySearch_Agent
#from agents.basic_agent import Basic_Agent
from agents.agent import DDPG_Agent
from tasks.task import Task
import argparse

def get_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('num_episodes', nargs='?', type=int, default=500,
                        help='Number of episodes to train')

    return parser.parse_args()

def main():
    in_args = get_input_args()

    exportPath = './data/'
    if not os.path.exists(exportPath):
        os.makedirs(exportPath)

    # z axis is up
    init_pose = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0]) 
    target_pos = np.array([0.0, 0.0, 10.0])
    task = Task(init_pose=init_pose, target_pos=target_pos, runtime=15.0)
    #agent = PolicySearch_Agent(task) 
    #agent = Basic_Agent(task) 
    agent = DDPG_Agent(task)

    # before training
    resultsAll = []
    high_score = -1000000.0
    low_score = 1000000.0

    # do this in each episode

    for i_episode in range(1, in_args.num_episodes+1):
        # start a new episode
        state = agent.reset_episode() 
        score = 0

        episode_results = {
            'time': [],
            'x': [],
            'y': [],
            'z': [],
            'phi': [],
            'theta': [],
            'psi': [],
            'vx': [],
            'vy': [],
            'vz': [],
            'reward': [],
        }

        while True:
            action = agent.act(state)  
            next_state, reward, done = task.step(action)

            agent.step(action, reward, next_state, done)
            state = next_state
            score += reward
            high_score = max(high_score, score)
            low_score = min(low_score, score)

            # track the results for offline analysis
            episode_results['time'].append(task.sim.time)
            episode_results['x'].append(state[0])
            episode_results['y'].append(state[1])
            episode_results['z'].append(state[2])
            episode_results['phi'].append(state[3])
            episode_results['theta'].append(state[4])
            episode_results['psi'].append(state[5])
            episode_results['vx'].append(state[6])
            episode_results['vy'].append(state[7])
            episode_results['vz'].append(state[8])
            episode_results['reward'].append(reward)
            
            if done:
                print("\rEpisode = {:4d}, score = {:7.3f}, low score = {:7.3f}, high score = {:7.3f}".format(i_episode, score, low_score, high_score), end="")
                break

        resultsAll.append(episode_results)

        sys.stdout.flush()

    # save results for later analysis
    with open("{}results0.bin".format(exportPath), 'wb') as pickleFile:
        pickle.dump(resultsAll, pickleFile)

    print("\n")

# Call to main function to run the program
if __name__ == "__main__":
    main()