from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    nilaiku = 200
    return render_template("index.html", nilai = nilaiku)

@app.route("/ini_index")
def myindex():
    return "<h1>ini index!</h1> </br> <h3>selamat datang di main</h3>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    