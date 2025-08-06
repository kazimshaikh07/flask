from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Home route to render the feedback form
@app.route("/")
def feedback_form():
    return render_template("feedback.html")

# Route to handle form submission
@app.route("/submit", methods=["POST"])
def submit_feedback():
    Bname = request.form["Bname"]
    Aname = request.form["Aname"]
    message = request.form["message"]

    # Save to CSV file
    with open("feedback.csv", mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        formatted = f"Book name:  {Bname},Author name: {Aname}, Why you recommend: {message}"
        writer.writerow([formatted])

    return redirect("/thankyou")

# Thank you page
@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)