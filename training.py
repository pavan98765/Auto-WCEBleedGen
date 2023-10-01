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

# Initialize the YOLOv8 model
model = YOLO(model="yolov8s.pt")

# Start training the model
model.train(
    task="detect",  # train detection (i.e. bounding boxes)
    epochs=50,
    imgsz=800,
    data=data_yaml_path,
    plots=True,  # Optional: Enable or disable training plots
    # weights="/path/to/pretrained/weights",  # Optional: Provide pretrained weights
    # batch_size=16,  # Optional: Adjust batch size as needed
    # device="0",  # Optional: Specify GPU device if you have multiple GPUs
    # project="your_project_name",  # Optional: Specify a project name
    # name="your_run_name",  # Optional: Specify a run name
    # save_dir="/path/to/save/directory",  # Optional: Specify a directory to save checkpoints and logs
)
