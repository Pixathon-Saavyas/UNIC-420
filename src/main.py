# For vs code
# main program
# import required libraries
from agent import agent
from user import user
from uagents import Bureau

#adding all users to bureau and running it
if __name__ == "__main__":
    bureau = Bureau()
    bureau.add(agent)
    bureau.add(user)
    bureau.run()
