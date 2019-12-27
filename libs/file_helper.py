import json

def read_data(filename):
    """Summary
    read all the data from the logs
    Returns:
        any: data 
    """
    data = {}
    try:
        with open(filename, "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file at reise_log_buch.txt!")
    finally:
        return data

def save_data(filename, data): 
    """Summary
    save the data to the specified file
    Args:
        String: filename
        any: data to be stored 
    """
    with open(filename, "w", encoding="utf-8") as open_file:
        json.dump(data, open_file)