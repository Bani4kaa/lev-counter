from pathlib import Path
import yaml
import os

# Path to your YAML file describing the dataset
yaml_file = "data.yaml"



# Check if the YAML file describing the dataset exists
if not os.path.exists(yaml_file):
    print(f"Error: {yaml_file} not found.")
    exit()

# Open the YAML file and load its contents
with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

# Construct the command for training
command = f"python3 train.py --img 640 --batch 16 --epochs 5 --data {yaml_file} --weights yolov5s.pt --name lev-counter-2_2"

# Execute the command
os.system(command)