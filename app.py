from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    nilai = 200

    # looping
    hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

    # seleksi kondisi if-else
    perasaan = "nda tau" # jika senang maka dia juga cinta, jika tidak maka dia sedih

    # set variable\
    # langsung di template html
    return render_template("index.html", nilai = nilai, day = hari, feeling = perasaan)

@app.route("/ini_index")
def myindex():
    return "<h1>ini index!</h1> </br> <h3>selamat datang di main</h3>"

@app.route("/about")
def aboutku():
    return render_template("about.html")

@app.route("/contact")
def contactku():
    return render_template("contact.html")

# parsing nilai int
@app.route("/parsingint/<int:nilaiku>")
def int_parsing(nilaiku):
    return "nilainya adalah : {}".format(nilaiku)

# parsing nilai string
@app.route("/parsingstring/<string:namaku>")
def string_parsing(namaku):
    return "nilainya adalah : {}".format(namaku)

# argument parser
@app.route("/parsingargument")
def ayo_argument():
    data = request.args.get("nilai")
    return "nilainya dari argument parser adalah {}".format(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    