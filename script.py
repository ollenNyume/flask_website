from flask import Flask, render_template  # importing flask class obj from the flask library
app = Flask(__name__)  # instantiating obj


@app.route("/")  # url
def home():  # map output to url
    return render_template("index.html")


@app.route("/about/")  # url
def about():  # map output to url
    return render_template("about.html")


@app.route("/contact/")  # url
def contact():  # map output to url
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
