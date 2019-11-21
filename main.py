from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from libs import journey_log
from datetime import datetime


app = Flask("Track your day")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/list/journey")
def list_journey():
    trips = journey_log.read_trips()
    chart = journey_log.pie_chart()
    return render_template("list_journey.html", reisen = trips, viz_div=chart)


@app.route("/add/journey", methods=['GET', 'POST'])
def add_journey():
    if request.method == 'POST':
        journey_log.save_new_trip(request.form)
        return redirect("/list/journey")

    return render_template("add_journey.html")

@app.template_filter('datetime')
def format_date_for_index(value):
    date = datetime.strptime(value, '%d%m%Y')
    return date.strftime("%d.%m.%Y")

if __name__ == "__main__":
    app.run(debug=True, port=5000)