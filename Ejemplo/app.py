from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('register.html')

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/teacher", methods=["GET","POST"])
def teacher():
    return render_template("teacher.html")

@app.route("/student", methods=["GET","POST"])
def student():
    return render_template("student.html") 

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)