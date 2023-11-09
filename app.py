from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            file_path = "./static/images/file.jpg"
            file.save(file_path)

            result = "hello"
            # img_title = file.filename
            # img_url = file_path
            # return render_template("result.html", img_title=img_title, img_url=img_url)
            return render_template("predict.html", result=result)

    return render_template("predict.html")


@app.route("/discover")
def discover():
    return render_template("discover.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # send_message(request)
        message = "Thank you for contacting us! We'll get back to you soon."
        return render_template("contact.html", message=message)

    return render_template("contact.html", message="")


@app.route("/faq")
def faq():
    return render_template("faq.html")


def send_message(request):
    name = request.form["firstname"]
    email = request.form["email"]
    message = request.form["message"]

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = ""
    smtp_password = ""

    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = smtp_username
    msg["Subject"] = "Contact Form Submission"

    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, smtp_username, msg.as_string())
    server.quit()


# def process_image(image):
#     pass


if __name__ == "__main__":
    app.run(debug=True)
