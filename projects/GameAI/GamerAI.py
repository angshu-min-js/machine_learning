from enviroment import Enviroment
from train import Trainer
from dqn import DQn

# Initialize the Enviroment
env = Enviroment(args) #args is the command line argument from the game
agent = DQN(env, args)

# Train
Trainer(agent).run()

# Play the game
env.gym.monitor.start(args.out, force=True)
agent.play()
env.gym.monitor.close()
