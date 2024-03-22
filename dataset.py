from pathlib import Path
import yaml
import os

yaml_file = "data.yaml"



if not os.path.exists(yaml_file):
    print(f"Error: {yaml_file} not found.")
    exit()

with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

command = f"python3 export.py --weights best.pt --include tfjs"

os.system(command)