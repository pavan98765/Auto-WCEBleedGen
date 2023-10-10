# Auto-WCEBleedGen Challenge Submission

## Table of Achieved Evaluation Metrics

| Dataset    | Metric                                      | Value                |
| ---------- | ------------------------------------------- | -------------------- |
| Validation | **Classification Accuracy**                 | **96.10%**           |
| Validation | **Classification Recall**                   | **96.10%**           |
| Validation | **Classification F1-Score**                 | **96.10%**           |
| Validation | **Detection Mean Average Precision**        | **76.8%** @ 0.5(IoU) |
| Validation | **Detection Average Precision**             | **76.8%**            |
| Validation | **Detection Intersection over Union (IoU)** | **80.75%**           |

## Screenshots/Pictures of Best Validation Results

### Image 20 (Validation Dataset)

![Image 20](Detection_Predictions/validation/img-20-_png_jpg.rf.af18786f8de1f8982a0682bac1a8b529.jpg)

### Image 47 (Validation Dataset)

![Image 47](Detection_Predictions/validation/img-47-_png_jpg.rf.30b4e1998b43b09def5e6b834803c050.jpg)

### Image 54 (Validation Dataset)

![Image 54](Detection_Predictions/validation/img-54-_png_jpg.rf.61c88ed1508f277adf41ebd28a2b0bc1.jpg)

### Image 114 (Validation Dataset)

![Image 114](Detection_Predictions/validation/img-114-_png_jpg.rf.c546305f452ee31659ddcf4b8be6911f.jpg)

### Image 149 (Validation Dataset)

![Image 149](Detection_Predictions/validation/img-149-_png_jpg.rf.b4e7d488af5d4e43f57ad0bfce5961d0.jpg)

### Image 157 (Validation Dataset)

![Image 157](Detection_Predictions/validation/img-157-_png_jpg.rf.0fe24c07220a083cd41846b4fe5efb7d.jpg)

### Image 212 (Validation Dataset)

![Image 212](Detection_Predictions/validation/img-212-_png_jpg.rf.13173dbff86234bb7e94d731a9938626.jpg)

### Image 305 (Validation Dataset)

![Image 305](Detection_Predictions/validation/img-305-_png_jpg.rf.36d0534520f464d319826af3461a4320.jpg)

### Image 314 (Validation Dataset)

![Image 314](Detection_Predictions/validation/img-314-_png_jpg.rf.84a0cdeda1ee24e6c164d386166278d5.jpg)

### Image 786 (Validation Dataset)

![Image 786](Detection_Predictions/validation/img-786-_png_jpg.rf.f8f9590f1c5a553515c52cb2f6acd4b5.jpg)

## Interpretability Plots for Best Validation Results

### Interpretability Plot 1

![Interpretability Plot 1](path_to_plot_1.png)

## Screenshots/Pictures of Best Testing Results (Dataset 1)

### A0001.png (Dataset 1)

![A0001.png](Detection_Predictions/test_dataset_1/A0001.png)

### A0006.png (Dataset 1)

![A0006.png](Detection_Predictions/test_dataset_1/A0006.png)

### A0026.png (Dataset 1)

![A0026.png](Detection_Predictions/test_dataset_1/A0026.png)

### A0038.png (Dataset 1)

![A0038.png](Detection_Predictions/test_dataset_1/A0038.png)

### A0041.png (Dataset 1)

![A0041.png](Detection_Predictions/test_dataset_1/A0041.png)

<!-- Repeat the pattern for images 3-5 (Dataset 1) -->

## Screenshots/Pictures of Best Testing Results (Dataset 2)

### A0060.png (Dataset 2)

![A0060.png](Detection_Predictions/test_dataset_2/A0060.png)

### A00129.png (Dataset 2)

![A0129.png](Detection_Predictions/test_dataset_2/A0129.png)

### A0134.png (Dataset 2)

![A0134.png](Detection_Predictions/test_dataset_2/A0134.png)

### A0145.png (Dataset 2)

![A0145.png](Detection_Predictions/test_dataset_2/A0145.png)

### A0060.png (Dataset 2)

![A0285.png](Detection_Predictions/test_dataset_2/A0285.png)

## Interpretability Plots for Best Testing Results (Dataset 1)

### Interpretability Plot 1 (Dataset 1)

![Interpretability Plot 1 (Dataset 1)](path_to_plot_1_dataset1.png)

## Interpretability Plots for Best Testing Results (Dataset 2)

### Interpretability Plot 1 (Dataset 2)

![Interpretability Plot 1 (Dataset 2)](path_to_plot_1_dataset2.png)

## Link to Datasets and Models:

We Recommend you to explore our dataset and trained models on the [Roboflow Universe platform](https://universe.roboflow.com/wce-fpcql/wce_clean_train_2.0).
It has multiple versions of the dataset, more data has been added and annotated, 6 models have been trained, deployed and evaluated, which can be easily visualized and used!

## Repository Structure

1. #Model Weights:
   This directory contains the YOLOv8 trained model, named **best.pt**, along with any other relevant training data or model-related files.**All the Predictions and Evaluations for classification and Detection are done with this model**
2. Classification Predictions:
   Inside this directory,the **All_Predictions.csv** file contains the classification prediction of both test_dataset_1 and 2 from the yolo detection model.
   Along with it there are validation predictions and evals.
3. Code:
   This section contains the code for training, testing, and validation.
4. Datasets:
   The Datasets directory holds our annotated dataset in YOLO format,split into an 80/20 ratio for training and validation(all evaluations are done on this validation data).
5. Detection Predictions:
   This directory includes predictions of the yolo detection model on the Validation Dataset, Test Dataset 1, and Test Dataset 2 with the labels.
6. Matlab Classification Model
   This directory contains a separate classification model, based on MobileNet architecture,built using matlab. All relevant code and results realated to this model are stored here.

## YOLOv8 Detection Model

I have trained a yolov8 x model on the bleeding dataset. I detects the bleeding regions. I am using the same model for classification as well, basically if there is a detection then classified as bleeding.

## How to Run

To run the training, just download the weights(Model_weights/best.pt) and datase(datasets) , then run the training command or script.
To validate run the validation script or command.
To predict run Testing.py in the end give the path to model weights, input folder, output folder and the predictions will be stored.
Using Testing_with_classification.py will give the predictions along with classification results.

## Conclusion

I have trained the yolov8 model 'x' version on the dataset, I reannotated the dataset, then collected more data annotated them and trained on it. All the evaluation metrics are calculated on the default validation dataset also stored in the repo.
