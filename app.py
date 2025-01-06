from flask import Flask, render_template, request
import pickle
model = pickle.load(open('spam.pkl', 'rb'))
cvect = pickle.load(open('vectorizer.pkl', 'rb'))
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]
    data = [message]
    vectorized_message = cvect.transform(data).toarray()
    prediction = model.predict(vectorized_message)
    if prediction[0] == 1:
        result = "Spam Email"
    else:
        result = "Not a Spam Email"
    return render_template("index.html", prediction=result, user_input=message)
if __name__ == "__main__":
    app.run(debug=True)
