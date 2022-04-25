from flask import Flask, render_template

app = Flask(__name__)

#frist pg and route
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

#dinamic name user when u add some new user in the app
@app.route("users/<user_name>")
def users(user_name):
    return render_template("users.html", user_name = user_name)


#connect site
if __name__ == "__main__":
    app.run(debug = True)