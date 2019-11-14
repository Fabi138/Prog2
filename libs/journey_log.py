from datetime import date
import json

def save_new_trip(form_request):
    print(form_request)
    today = date.today()
    current_date = today.strftime("%d%m%Y")
    
    reise = read_trips()
    reise[current_date]  = []
    reise[current_date].append(
        {
            "reisemittel": form_request.get('reise_art'),
            "von": form_request.get('von'),
            'bis': form_request.get('bis'),
            'start_zeit': form_request.get('start_zeit'),
            'ziel_zeit': form_request.get('ziel_zeit'),
            'verspaetung': form_request.get('verspaetung', 0)
        }
    )

    with open('reise_log_buch.txt', "w", encoding="utf-8") as open_file:
        json.dump(reise, open_file)

def read_trips():
    reise = {}
    try:
        with open('reise_log_buch.txt', "r") as open_file:
            reise = json.load(open_file)
    except:
        print("Error with file at reise_log_buch.txt!")
    finally:
        return reise
