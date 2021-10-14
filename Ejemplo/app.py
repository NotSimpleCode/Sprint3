from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('register.html')

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("teacher.html")

@app.route("/login2", methods=["GET","POST"])
def login2():
    return render_template("student.html") 
    
@app.route("/salir", methods=["GET","POST"])
def salir():
    return render_template("login.html") 


if __name__ == "__main__":
    app.run(debug=True)