def is_walking(directions_result):
    """Test if first and last have travel mode WALKING."""
    start_travel_mode = directions_result[0]['legs'][0]['steps'][0]['travel_mode']
    stop_travel_mode = directions_result[0]['legs'][-1]['steps'][0]['travel_mode']

    if start_travel_mode != 'WALKING':
        raise Exception("start_travel_mode != 'WALKING'")
    elif stop_travel_mode != 'WALKING':
        raise Exception("stop_travel_mode != 'WALKING'")
    else:
        pass