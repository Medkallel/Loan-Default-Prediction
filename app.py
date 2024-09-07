from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])


df = pd.read_csv('Data\Loan_Data_Describe.csv')
df = df.loc[[1, 2]].reset_index(drop=True)

@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])

        loan_amt_outstanding = float(request.form["loan_amt_outstanding"])
        loan_amt_outstanding = (loan_amt_outstanding - df.iloc[0,0]) / df.iloc[1, 0]

        total_debt_outstanding = float(request.form["total_debt_outstanding"])
        total_debt_outstanding = (total_debt_outstanding - df.iloc[0,1]) / df.iloc[1, 1]

        income = float(request.form["income"])
        income = (income - df.iloc[0,2]) / df.iloc[1, 2]

        years_employed = int(request.form["years_employed"])
        income = (income - df.iloc[0,3]) / df.iloc[1, 3]

        fico_score = int(request.form["fico_score"])
        income = (income - df.iloc[0,4]) / df.iloc[1, 4]

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
