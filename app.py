from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template')
app.config["files"] = "."

@app.route("/")
def home():
    return render_template("UI.html")


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)

