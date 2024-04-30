import gym
env = gym.make("CartPole-v1", render_mode="rgb_array")
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # 采取随机行动
env.close()