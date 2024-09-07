"""
This Flask web application predicts loan eligibility based on user input features.
It loads a pre-trained model and uses it to make predictions.
"""

from flask import Flask, render_template, request
import pickle
import pandas as pd

# Paths to the model and data description files
model_path = "Models/model.pkl"
data_describe_path = "Data/Loan_Data_Describe.csv"

app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open(model_path, "rb"))

def model_pred(features):
    """
    Predict loan eligibility based on input features.

    Parameters:
    features (list): A list of input features for the model.

    Returns:
    int: The prediction result (0 or 1).
    """
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

# Load and preprocess the data description file
df = pd.read_csv(data_describe_path)
df = df.loc[[1, 2]].reset_index(drop=True)

@app.route("/", methods=["GET"])
def Home():
    """
    Render the home page.

    Returns:
    str: The rendered HTML template for the home page.
    """
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Handle the prediction request and render the result.

    Returns:
    str: The rendered HTML template with the prediction result.
    """
    if request.method == "POST":
        # Extract and preprocess input features from the form
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])

        loan_amt_outstanding = float(request.form["loan_amt_outstanding"])
        loan_amt_outstanding = (loan_amt_outstanding - df.iloc[0, 1]) / df.iloc[1, 1]

        total_debt_outstanding = float(request.form["total_debt_outstanding"])
        total_debt_outstanding = (total_debt_outstanding - df.iloc[0, 2]) / df.iloc[1, 2]

        income = float(request.form["income"])
        income = (income - df.iloc[0, 3]) / df.iloc[1, 3]

        years_employed = int(request.form["years_employed"])
        years_employed = (years_employed - df.iloc[0, 4]) / df.iloc[1, 4]

        fico_score = int(request.form["fico_score"])
        fico_score = (fico_score - df.iloc[0, 5]) / df.iloc[1, 5]

        # Make a prediction using the pre-trained model
        prediction = model.predict(
            [[credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score]]
        )

        # Render the result based on the prediction
        if prediction[0] == 1:
            return render_template(
                "index.html",
                prediction_text="Granting a loan to this client is too risky!",
            )
        else:
            return render_template(
                "index.html", prediction_text="Yes, you can grant a loan to this client."
            )
    else:
        return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)