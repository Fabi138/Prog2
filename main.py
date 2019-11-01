from flask import Flask
from flask import render_template

app = Flask("Track your day")

@app.route("/")
@app.route("/index")
def index():
    print("dsf")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)