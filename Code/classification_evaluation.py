import csv
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def calculate_classification_metrics(true_labels, predicted_labels, average="weighted"):
    """
    Calculate classification metrics for predicted and true labels.

    Args:
        true_labels (list): A list of true class labels.
        predicted_labels (list): A list of predicted class labels.
        average (str, optional): The method used for averaging in precision, recall, and F1 score.
            Possible values are 'micro', 'macro', 'weighted', or 'samples'. Default is 'weighted'.

    Returns:
        dict: A dictionary containing precision, recall, F1 score, and accuracy.
    """
    precision = precision_score(true_labels, predicted_labels, average=average)
    recall = recall_score(true_labels, predicted_labels, average=average)
    f1 = f1_score(true_labels, predicted_labels, average=average)
    accuracy = accuracy_score(true_labels, predicted_labels)

    metrics = {
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "Accuracy": accuracy,
    }

    return metrics


def main(csv_file_path, averaging_method="weighted"):
    predicted_labels = []
    true_labels = []

    with open(csv_file_path, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:
            image_name, predicted_class, true_class = row
            predicted_labels.append(predicted_class)
            true_labels.append(true_class)

    # Calculate classification metrics with the specified averaging method
    classification_metrics = calculate_classification_metrics(
        true_labels, predicted_labels, average=averaging_method
    )

    # Print the results
    for metric, value in classification_metrics.items():
        print(f"{metric}: {value}")


if __name__ == "__main__":
    csv_file_path = "path/to/your/csv/file.csv"
    averaging_method = "weighted"  # You can change the averaging method if needed
    main(csv_file_path, averaging_method)
