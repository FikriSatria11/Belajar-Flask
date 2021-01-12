from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretkeyku2021"

@app.route("/", methods=["POST", "GET"])
def index():
    if "email" in session:
        return redirect(url_for('sukses_req'))
    else:
        # Jika tombol button diklik -> request Post
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            # jika email dan password benar
            if email == 'admin@gmail.com' and password == 'pass':
                session['email'] = email
                session['password'] = password
                return redirect(url_for('sukses_req'))
            # jika email dan password salah
            else:
                # harus login lagi
                return render_template("index.html")

        return render_template("index.html")

@app.route("/sukses")
def sukses_req():
    nilai = "Anda sukses login!"
    return render_template("sukses.html", nilai = nilai)

@app.route("/about")
def about():
    if "email" in session:
        return render_template("about.html")
    else:
        return redirect(url_for('index'))

@app.route("/contact")
def contact():
    if "email" in session:
        return render_template("contact.html")
    else:
        return redirect(url_for('index'))

@app.route("/logout")
def logout_akun():
    session.pop("email", "password")
    return redirect(url_for('index'))

@app.route("/redirect-about")
def redirect_about():
    return redirect(url_for('about'))

@app.route("/redirect-contact")
def redirect_contact():
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")