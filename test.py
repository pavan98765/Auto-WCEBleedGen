from ultralytics import YOLO
import subprocess

# Define the path to the YOLO model and other parameters
model_path = "C:/Users/Jarvis/Desktop/BTP_wce/#wce_detection/models/yolo_small_180e_more_data/runs/detect/train/weights/best.pt"
confidence_threshold = 0.25

# Path of image/ folder of images / video
test_data_path = (
    "C:/Users/Jarvis/Desktop/BTP_wce/data/#Test_Dataset_WCEBleedGen/Test_Dataset_1"
)

# Construct the YOLO predict command
command = [
    "yolo",  # The YOLO executable (assuming it's in your PATH)
    "task=detect",
    "mode=predict",
    f"model={model_path}",
    f"conf={confidence_threshold}",
    f"source={test_data_path}",
    "save=True",
]

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

# results of the test will be saved in the following directory: runs\detect\predict
