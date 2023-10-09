# Import required libraries
from ultralytics import YOLO
import subprocess

# Specify the location of your validation data.yaml file and model weights
data_yaml_path = "/path/to/your/validation_data.yaml"
# the trained model weights are in the repository named as best.pt
model_path = "path/to/your/trained/model/weights.pt"

# Command to run YOLOv8 validation
command = [
    "yolo",
    "task=detect",
    "mode=val",
    f"model={model_path}",
    f"data={data_yaml_path}",
]

# Execute the command
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# results of the validation will be saved in the following directory: runs\detect\val

# You can Use the command below to Validate the model
# yolo task=detect mode=val model=/path/to/your/model.pt data=/path/to/your/data.yaml
# The above command will run YOLOv8 validation on the validation dataset and save the results in the runs/detect/val folder.
