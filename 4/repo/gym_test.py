import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import gym

env = gym.make('CartPole-v0')
# env = gym.make('MsPacman-v0')
# env = gym.make('MountainCar-v0')
# env = gym.make('FrozenLake-v0')
env.reset()
# print env.action_space.sample()
for _ in range(1000):
	env.render()
	array, reward, done, empty = env.step(env.action_space.sample()) # take a random action
	print array, reward, done, empty
	if done:
		env.reset()

# pause = raw_input()
