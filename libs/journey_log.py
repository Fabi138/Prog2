from datetime import date
from datetime import datetime
from plotly.offline import plot
import plotly.graph_objects as go
from . import file_helper

def save_new_trip(form_request):
    """Summary
    Add a new trip to the log
    Args:
        form_request (request.form): form of add_journey.html
    """
    #print(form_request)
    today = date.today()
    current_date = today.strftime("%d%m%Y") #need current date for key in dict
    
    start_zeit = form_request.get('start_zeit')
    ziel_zeit = form_request.get('ziel_zeit')

    start = datetime.strptime(start_zeit, '%H:%M') #string to date for calculation
    ziel = datetime.strptime(ziel_zeit, '%H:%M') #string to date for calculation
    
    travel_time = ziel - start  
    travel_time_minutes = int(travel_time.total_seconds()/60) #convert from hh:mm to minutes

    reise = read_trips()
    current_date_data = reise.get(current_date, []) #get the current date entry
    current_date_data.append(
        {
            "reisemittel": form_request.get('reise_art'),
            "von": form_request.get('von'),
            'bis': form_request.get('bis'),
            'start_zeit': start_zeit,
            'ziel_zeit': ziel_zeit,
            'verspaetung': form_request.get('verspaetung', 0),
            'travel_time': travel_time_minutes
        }
    )

    reise[current_date] = current_date_data
    
    file_helper.save_data('reise_log_buch.txt', reise)

def read_trips():
    """Summary
    read all the data from the logs
    Returns:
        dict: all journeys 
    """
    return file_helper.read_data('reise_log_buch.txt')

def pie_chart():
    """Summary
    generate pie chart for time per vehical
    Returns:
        String: html of chart
    """
    labels = ['Flugzeug','Auto','Zug']
    time = {'flugzeug': 0, 'auto': 0, 'zug': 0}

    data = read_trips()

    for key, reise in data.items(): #for everyday 
        for trip in reise: #for every trip in day
            time[trip['reisemittel']] = time[trip['reisemittel']] + trip['travel_time']

    #print(time)
    values = [time['flugzeug'], time['auto'], time['zug']] #create valuelist for chart

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    div = plot(fig, output_type="div")
    return div