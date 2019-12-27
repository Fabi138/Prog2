from datetime import date
from datetime import datetime
from plotly.offline import plot
import plotly.graph_objects as go
from . import file_helper

def save_new_game(form_request):
    """Summary
    Add a new trip to the log
    Args:
        form_request (request.form): form of add_journey.html
    """
    print(form_request)
     
    today = date.today()
    current_date = today.strftime("%d%m%Y") #need current date for key in dict

    games = read_games()
    current_date_data = games.get(current_date, []) #get the current date entry

    # Check if this game was already played today
    added = False
    for game in current_date_data:
        if game['game'] ==  form_request.get('game'): # if game played add new time to existing
            game['time'] = int(game['time']) + int(form_request.get('time'))
            added = True
    
    if not added: # if not played yet add new entry
        current_date_data.append(
            {
                "game": form_request.get('game'),
                "time": form_request.get('time')
            }
        )

    games[current_date] = current_date_data
    
    file_helper.save_data('game_log_buch.txt', games)

def read_games():
    """Summary
    read all the data from the logs
    Returns:
        dict: all journeys 
    """
    return file_helper.read_data('game_log_buch.txt')

def read_my_games():
    """Summary
    read all the data from the logs
    Returns:
        dict: all journeys 
    """
    return file_helper.read_data('all_games.txt')

def add_game(request):
    all_games = read_my_games()
    today = date.today()
    current_date = today.strftime("%d%m%Y")

    all_games[request.get('game')] = current_date

    file_helper.save_data("all_games.txt", all_games)

def pie_chart():
    """Summary
    generate pie chart for time per vehical
    Returns:
        String: html of chart
    """
    my_games = read_my_games()
    labels = list(my_games.keys())
    
    print(labels)
    time = {}
    for game in labels:
        time[game] = 0
    data = read_games()

    for key, day in data.items(): #for everyday 
        for game in day: #for every game in day
            time[game['game']] = int(time[game['game']]) + int(game['time'])

    values = list(time.values()) #create valuelist for chart

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    div = plot(fig, output_type="div")
    return div
