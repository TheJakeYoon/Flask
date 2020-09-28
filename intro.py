from flask import Flask, render_template, url_for, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="flask_tutorial"
)

cursor = mydb.cursor()

@app.route("/", methods=["POST", "GET"])
def index():
        return render_template("index.html")

@app.route("/database.html", methods=["POST", "GET"])
def database():
    if request.method == "POST":
        userDetails = request.form
        user_id = int(userDetails["id"])
        user_password = userDetails["password"]
        print(user_id)
        print(user_password)
        cursor.execute("INSERT INTO users(ID, password) VALUES(%s, %s)", (user_id, user_password))
        mydb.commit()
        return "<h1>submit pressed<h1> <a href='database.html'>Click here to check database</a>"
    else:
        resultValue = cursor.execute("SELECT * FROM users")
        userDetails = cursor.fetchall()
        return render_template("database.html", userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)