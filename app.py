from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

loa_mean = 4159.68
loa_std = 1421.40

tdo_mean = 8718.92
tdo_std = 6627.16

income_mean = 70039.90
income_std = 20072.21

@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])
        loan_amt_outstanding = float(request.form["loan_amt_outstanding"])
        loan_amt_outstanding = (loan_amt_outstanding - loa_mean) / loa_std

        total_debt_outstanding = float(request.form["total_debt_outstanding"])
        total_debt_outstanding = (total_debt_outstanding - tdo_mean) / tdo_std

        income = float(request.form["income"])
        income = (income - income_mean) / income_std

        years_employed = int(request.form["years_employed"])
        fico_score = int(request.form["fico_score"])
        prediction = model.predict(
            [[credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score]]
        )

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
    app.run(host="0.0.0.0", port=5000, debug=True)
