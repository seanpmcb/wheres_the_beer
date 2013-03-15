from pyramid.view import view_config
import logging

log = logging.getLogger(__name__)

from wheres_the_beer.lib import config


@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    google_maps_key = config.get('google_maps_key')
    return {'google_maps_key': google_maps_key}
