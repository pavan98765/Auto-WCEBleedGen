from ultralytics import YOLO
import subprocess

# command to train the model
# yolo task=detect mode=train model=/path/to/your/model.pt data=/path/to/your/data.yaml epochs=50 imgsz=800 plots=True

# Define the paths to the model and data.yaml (replace with actual paths)
model = "yolov8s.pt"
data_yaml_path = "/path/to/your/data.yaml"

# Construct the YOLO training command as a list of strings
command = [
    "yolo",
    "task=detect",
    "mode=train",
    f"model={model}",
    f"data={data_yaml_path}",
    "epochs=50",
    "imgsz=800",
    "plots=True",
]

try:
    # Join the list of strings into a single command string and execute it
    subprocess.run(" ".join(command), shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error:", e)
