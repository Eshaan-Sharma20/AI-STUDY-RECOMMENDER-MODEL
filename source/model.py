import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


class StudentPerformanceModel:
    def __init__(self):
        # Initialize decision tree model
        self.classifier = DecisionTreeClassifier()

    def fetch_dataset(self, file_location):
        # Read CSV file
        dataset = pd.read_csv(file_location)

        # Separate features and target
        feature_data = dataset[['math', 'physics', 'dsa']]
        target_labels = dataset['label']

        return feature_data, target_labels

    def train_model(self, features, labels):
        # Split data into training and testing parts
        features_train, features_test, labels_train, labels_test = train_test_split(
            features, labels, test_size=0.2
        )

        # Train the model
        self.classifier.fit(features_train, labels_train)

        # Evaluate performance
        predictions = self.classifier.predict(features_test)

        print("\n--- Model Performance ---")
        print(classification_report(labels_test, predictions))

    def predict_level(self, student_scores):
        # Predict student's level
        predicted_result = self.classifier.predict(student_scores)
        return predicted_result[0]
