from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from libs import journey_log

app = Flask("Track your day")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/add/journey", methods=['GET', 'POST'])
def add_journey():
    if request.method == 'POST':
        journey_log.save_new_trip(request.form)
        return redirect("/index")

    return render_template("add_journey.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)