from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    nilaiku = 200

    # looping
    hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

    # seleksi kondisi if-else
    perasaan = "nda tau" # jika senang maka dia juga cinta, jika tidak maka dia sedih

    #set variable


    return render_template("index.html", nilai = nilaiku, day = hari, feeling = perasaan)

@app.route("/ini_index")
def myindex():
    return "<h1>ini index!</h1> </br> <h3>selamat datang di main</h3>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    