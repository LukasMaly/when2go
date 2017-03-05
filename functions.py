import googlemaps
from datetime import datetime
import tests


def get_time_to_leave(home_address, work_address):
    gmaps = googlemaps.Client(key='AIzaSyAoH4CMI1eRkZywJThDOl33rbJ96W1kn2Q')

    now = datetime.now()
    directions_result = gmaps.directions(home_address,
                                         work_address,
                                         mode="transit",
                                         departure_time=now)

    tests.is_walking(directions_result)

    walking_duration = directions_result[0]['legs'][0]['steps'][0]['duration']['value']
    departure_stop = directions_result[0]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
    departure_time = directions_result[0]['legs'][0]['steps'][1]['transit_details']['departure_time']['value']
    line_name = directions_result[0]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
    arrival_stop = directions_result[0]['legs'][0]['steps'][-2]['transit_details']['arrival_stop']['name']

    time_to_leave = departure_time - walking_duration
    time_to_leave_str = datetime.fromtimestamp(time_to_leave).strftime('%Y-%m-%d %H:%M:%S')

    return time_to_leave_str
