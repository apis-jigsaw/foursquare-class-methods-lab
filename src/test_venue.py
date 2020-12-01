import psycopg2
import pytest
from decimal import *

from db_utilities import *
from venue import Venue

location =  {'address': '141 Front St', 'crossStreet': 'Pearl St', 'lat': 40.70243624175102, 'lng': -73.98753900608666, 'labeledLatLngs': [{'label': 'display', 'lat': 40.70243624175102, 'lng': -73.98753900608666}], 'postalCode': '11201', 'cc': 'US', 'neighborhood': 'DUMBO', 'city': 'New York', 'state': 'NY', 
        'country': 'United States', 'formattedAddress': ['141 Front St (Pearl St)', 'New York, NY 11201', 'United States']}

categories = [{'id': '4bf58dd8d48988d151941735', 'name': 'Taco Place', 'pluralName': 'Taco Places', 'shortName': 'Tacos', 'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/taco_', 'suffix': '.png'}, 'primary': True}]

venue_details = {'id': '5b2932a0f5e9d70039787cf2', 'name': 'Los Tacos Al Pastor', 'categories': categories, 'location': location, 'rating': 7.9, 'price': {'tier': 1}, 'likes': {'count': 52}, 
        'delivery': {'url': 'https://www.seamless.com/menu/los-tacos-al-pastor-141a-front-st-brooklyn/857049?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=857049'}}

@pytest.fixture()
def clean_tables():
    drop_all_tables(test_conn, test_cursor)
    yield
    drop_all_tables(test_conn, test_cursor)

def test_venue_values():
    venue = Venue()
    venue.__dict__ = {'name':'Taco Place', 'price': 1}
    assert venue.values() == ['Taco Place', 1]

def test_venue_keys():
    venue = Venue()
    venue.__dict__ = {'likes': 12, 'name':'Taco Place', 'price': 1}
    assert venue.keys() == 'name, price, likes'

def test_save_venue(clean_tables):
    venue = Venue()
    venue.__dict__ = {'likes': 12, 'name':'Taco Place', 'price': 1}
    venue.save(test_conn, test_cursor)
