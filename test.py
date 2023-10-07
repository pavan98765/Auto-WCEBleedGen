import cv2
import os
from ultralytics import YOLO

# Define the Paths to the Weights, input and output directories!
model_path = "path/to/your/model.pt"
input_dir = "path/to/your/input/directory"
output_dir = "path/to/your/output/directory"

# Load the YOLOv8 model
model = YOLO(model_path)

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# List all image files in the input directory
image_files = [
    f for f in os.listdir(input_dir) if f.endswith(".png") or f.endswith(".jpg")
]

for image_file in image_files:
    # Path to the input image
    image_path = os.path.join(input_dir, image_file)

    # Load the input image
    image = cv2.imread(image_path)

    # Run YOLOv8 inference on the image
    results = model(image)

    xyxys = []
    confidences = []

    # Extract the bounding boxes and confidence scores
    for result in results:
        boxes = result.boxes
        confidences = boxes.conf.tolist()
        xyxys = boxes.xyxy.tolist()

        # Draw bounding boxes with thicker lines
        for xyxy, confidence in zip(xyxys, confidences):
            xyxy = [int(coord) for coord in xyxy]
            cv2.rectangle(
                image, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (255, 255, 255), 2
            )  # Green color, thicker lines

            # Put confidence score in the top-right corner with a smaller font
            conf_text = f"{confidence:.2f}"
            cv2.putText(
                image,
                conf_text,
                (xyxy[2] - 30, xyxy[1] + 12),  # Adjust the coordinates for positioning
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,  # Smaller font size
                (255, 255, 255),  # Green color
                1,  # Thickness
            )

    # Save the annotated image to the output directory with the same file name
    output_image_path = os.path.join(output_dir, image_file)
    cv2.imwrite(output_image_path, image)
# The annotated images will be saved in the following directory: output_dir

# Prediction/Testing through Command Line
# Another way to run YOLOv8 inference/Prediction is to use the command-line interface.Run the following command below in the terminal:

# yolo task=detect mode=predict model=/path/to/your/model.pt data=/path/to/your/data.yaml source=/path/to/your/images_or_video_or_folder save=True conf=0.25

# The above command will run YOLOv8 inference on the images or video or folder and save the results in the runs/detect/predict folder.

# Validation through Command Line
# To run YOLOv8 validation on the validation dataset, run the following command below in the terminal:

# yolo task=detect mode=val model=/path/to/your/model.pt data=/path/to/your/data.yaml

# The above command will run YOLOv8 validation on the validation dataset and save the results in the runs/detect/val folder.

# Training through Command Line
# To train the YOLOv8 model, run the following command below in the terminal:
# yolo task=detect mode=train model=/path/to/your/model.pt data=/path/to/your/data.yaml epochs=50 imgsz=800 plots=True
