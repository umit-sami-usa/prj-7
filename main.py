import os
from dotenv import load_dotenv, dotenv_values
import toml

load_dotenv()
print(os.getenv("MY_KEY"))

print("hello prj-7")

with open('prj-7.config.toml', 'r') as f:
	config = toml.load(f)

#Access values from the toml config file
print(config['server']['host'])
print(config['server']['port'])
print(config['database']['username'])



