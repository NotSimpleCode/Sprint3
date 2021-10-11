from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('register.html')

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("login.html")

#hola acabo de editar
#vamos a editar otra vez pero desde visual
@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("register.html")
    
#pull request

if __name__ == "__main__":
    app.run(debug=True)