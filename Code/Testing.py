import cv2
import os
from ultralytics import YOLO


def predict_on_single_image(
    model_path, input_image_path, output_image_path=None, confidence_threshold=0.25
):
    """
    Performs YOLOv8 object detection on a single input image.

    Args:
        model_path (str): Path to the YOLOv8 model weights.
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the annotated image (optional).
        confidence_threshold (float): Confidence threshold for object detection (default: 0.25).
    """
    # Load the YOLOv8 model
    model = YOLO(model_path)

    # Load the input image
    image = cv2.imread(input_image_path)

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
            if confidence >= confidence_threshold:
                cv2.rectangle(
                    image, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (255, 255, 255), 2
                )  # Green color, thicker lines

                # Put confidence score in the top-right corner with a smaller font
                conf_text = f"{confidence:.2f}"
                cv2.putText(
                    image,
                    conf_text,
                    (
                        xyxy[2] - 30,
                        xyxy[1] + 12,
                    ),  # Adjust the coordinates for positioning
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.4,  # Smaller font size
                    (255, 255, 255),  # Green color
                    1,  # Thickness
                )

    if output_image_path is not None:
        # Save the annotated image
        cv2.imwrite(output_image_path, image)
    else:
        # If no output path is specified, return the annotated image as a NumPy array
        return image


def predict_on_images_in_directory(
    model_path, input_dir, output_dir, confidence_threshold=0.25
):
    """
    Performs YOLOv8 object detection on all images in a directory.

    Args:
        model_path (str): Path to the YOLOv8 model weights.
        input_dir (str): Directory containing input images.
        output_dir (str): Directory to save annotated images.
        confidence_threshold (float): Confidence threshold for object detection (default: 0.25).
    """
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
        input_image_path = os.path.join(input_dir, image_file)

        # Load the input image
        image = cv2.imread(input_image_path)

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
                if confidence >= confidence_threshold:
                    cv2.rectangle(
                        image,
                        (xyxy[0], xyxy[1]),
                        (xyxy[2], xyxy[3]),
                        (255, 255, 255),
                        2,
                    )

                    # Put confidence score in the top-right corner with a smaller font
                    conf_text = f"{confidence:.2f}"
                    cv2.putText(
                        image,
                        conf_text,
                        (
                            xyxy[2] - 30,
                            xyxy[1] + 12,
                        ),  # Adjust the coordinates for positioning
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.4,  # font size
                        (255, 255, 255),  # color
                        1,  # Thickness
                    )

        # Save the annotated image to the output directory with the same file name
        output_image_path = os.path.join(output_dir, image_file)
        cv2.imwrite(output_image_path, image)


# Example usage for processing a single image:
model_path = "path/to/your/model.pt"
input_image_path = "path/to/your/input/image.jpg"
output_image_path = "path/to/your/output/image.jpg"
confidence_threshold = 0.25
predict_on_single_image(
    model_path, input_image_path, output_image_path, confidence_threshold
)

# Example usage for processing all images in a directory:
model_path = "path/to/your/model.pt"
input_dir = "path/to/your/input/directory"
output_dir = "path/to/your/output/directory"
confidence_threshold = 0.25
predict_on_images_in_directory(model_path, input_dir, output_dir, confidence_threshold)


# COMAND LINE USAGE:
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

# The above command will train the YOLOv8 model for given epochs and save the best model weights in the weights folder. The training results will be saved in the runs/train folder.
