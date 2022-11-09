import yaml
import os
import addict

# You can store your '/config.yaml' location here if you are running this with python and don't want to reinput it everytime
# eg change 'None' to something like 'C:\Dropbox\Chess\BookBuilder-main\config.yaml'
yaml_location = None

if yaml_location is None:
    yaml_location = input('What is the full path to your config.yaml file? (ie. /Users/youruser/BookBuilder/config.yaml): ')
while not os.path.exists(yaml_location):
        yaml_location = input('The location you have input does not exist, please try again: ')

print("Loading config file...")
with open(yaml_location, "r") as f:
    config = addict.Dict(yaml.safe_load(f))

print(f"File loaded!")
