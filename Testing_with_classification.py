import cv2
import os
import csv
from ultralytics import YOLO


def predict_on_single_image(
    model_path,
    input_image_path,
    output_image_path=None,
    confidence_threshold=0.25,
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

    num_boxes_detected = 0

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

                num_boxes_detected += 1
    print("Number of boxes detected: ", num_boxes_detected)
    if num_boxes_detected >= 1:
        detected_class = "Bleeding"
    else:
        detected_class = "Non-Bleeding"

    print("Detected class:", detected_class)

    # Save the annotated image
    cv2.imwrite(output_image_path, image)

    return detected_class


def predict_on_images_in_directory(
    model_path, input_dir, output_dir="output_images", confidence_threshold=0.25
):
    """
    Performs YOLOv8 object detection on all images in a directory and saves the results in a CSV file.

    Args:
        model_path (str): Path to the YOLOv8 model weights.
        input_dir (str): Directory containing input images.
        output_dir (str): Directory to save annotated images (default: "output_images").
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

    # Create a CSV file to store the results
    csv_file_path = os.path.join(output_dir, "classification.csv")
    with open(csv_file_path, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Image Name", "Predicted Class Label"])

        for image_file in image_files:
            # Path to the input image
            input_image_path = os.path.join(input_dir, image_file)

            # Load the input image
            image = cv2.imread(input_image_path)

            # Run YOLOv8 inference on the image
            results = model(image)

            xyxys = []
            confidences = []

            num_boxes_detected = 0

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
                            0.4,  # Smaller font size
                            (255, 255, 255),  # Green color
                            1,  # Thickness
                        )

                        num_boxes_detected += 1
            print("Number of boxes detected in", image_file, ":", num_boxes_detected)

            # Determine the class based on the number of boxes detected
            if num_boxes_detected >= 1:
                detected_class = "Bleeding"
            else:
                detected_class = "Non-Bleeding"

            print("Detected class for", image_file, ":", detected_class)

            # Remove the ".png" extension from the image name
            image_name = os.path.splitext(image_file)[0]
            # Write the results to the CSV file
            csv_writer.writerow([image_name, detected_class])

            # Save the annotated image to the output directory with the same file name
            output_image_path = os.path.join(output_dir, image_file)
            cv2.imwrite(output_image_path, image)


# Example usage for processing a single image:
model_path = "path/to/your/model_weights.pt"
input_image_path = "path/to/your/input_image.jpg"
output_image_path = "path/to/your/output_image.jpg"
confidence_threshold = 0.25
predict_on_single_image(
    model_path, input_image_path, output_image_path, confidence_threshold
)

# Example usage for processing all images in a directory:
model_path = "path/to/your/model_weights.pt"
input_dir = "path/to/your/input_directory"
output_dir = "path/to/your/output_directory"
confidence_threshold = 0.25
predict_on_images_in_directory(model_path, input_dir, output_dir, confidence_threshold)
