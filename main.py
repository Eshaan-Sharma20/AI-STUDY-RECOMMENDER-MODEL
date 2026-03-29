from src.model import StudentPerformanceModel
from src.recommend import generate_study_plan
import pandas as pd


def run_app():
    # Create model object
    study_model = StudentPerformanceModel()

    # Load dataset and train
    input_features, output_labels = study_model.fetch_dataset("data/dataset.csv")
    study_model.train_model(input_features, output_labels)

    print("\n===== AI Study Recommendation System =====")

    try:
        # Take user input
        math_marks = float(input("Enter your Math score: "))
        physics_marks = float(input("Enter your Physics score: "))
        dsa_marks = float(input("Enter your DSA score: "))

    except ValueError:
        print("Please enter valid numeric values.")
        return

    # Prepare input for prediction
    student_input = pd.DataFrame(
        [[math_marks, physics_marks, dsa_marks]],
        columns=["math", "physics", "dsa"]
    )

    # Get prediction and recommendation
    predicted_category = study_model.predict_level(student_input)
    study_advice = generate_study_plan(predicted_category)

    print(f"\nPredicted Performance Level: {predicted_category.upper()}")
    print(f"Suggested Plan: {study_advice}")


if __name__ == "__main__":
    run_app()
