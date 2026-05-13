from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route("/", methods=["GET", "POST"])
def register():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        users.append({
            "username": username,
            "password": password
        })

        message = "User registered!"

    return render_template("index.html", message=message)

@app.route("/users")
def show_users():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
