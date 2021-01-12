from flask import Flask, template_render, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretkeyku2021"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")