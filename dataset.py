from pathlib import Path
import yaml
import os

yaml_file = "data.yaml"



if not os.path.exists(yaml_file):
    print(f"Error: {yaml_file} not found.")
    exit()

with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

command = f"python3 train.py --img 640 --batch 16 --epochs 10 --data {yaml_file} --weights yolov5s.pt --name lev-counter-8"

os.system(command)