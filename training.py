# Install necessary libraries
# pip install ultralytics==8.0.134

# Import required libraries
import ultralytics

# Check GPU access
ultralytics.checks()

from ultralytics import YOLO

# Specify the location of your dataset and data.yaml file
dataset_location = "/path/to/your/dataset"
data_yaml_path = "/path/to/your/data.yaml"
data_yaml_path = "C:/Users/Jarvis/Desktop/BTP_wce/#wce_detection/notebooks/datasets/wce_clean_train_2.0-1/data.yaml"

# Initialize the YOLOv8 model
model = YOLO(model="yolov8s.pt")

# Start training the model
model.train(
    task="detect",  # train detection (i.e. bounding boxes)
    epochs=50,
    imgsz=800,
    data=data_yaml_path,
    # weights="/path/to/pretrained/weights",  # Optional: Provide pretrained weights
    # batch_size=16,  # Optional: Adjust batch size as needed
    # device="0",  # Optional: Specify GPU device if you have multiple GPUs
    # project="your_project_name",  # Optional: Specify a project name
    # name="your_run_name",  # Optional: Specify a run name
    # save_dir="/path/to/save/directory",  # Optional: Specify a directory to save checkpoints and logs
    plots=True,  # Optional: Enable or disable training plots
)
