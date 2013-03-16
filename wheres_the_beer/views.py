from pyramid.view import view_config
import logging
import json

log = logging.getLogger(__name__)

from wheres_the_beer.lib import config

@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    google_maps_key = config.get('google_maps_key')
    return {'google_maps_key': google_maps_key}

@view_config(route_name='old_data', renderer='json')
def old_data_view(request):
    the_file = open('wheres_the_beer/static/data.json', 'r')
    data = []
    for line in the_file:
        data.append(json.loads(line))
    the_file.close()

    return {'data': data}
