from pyramid.view import view_config

from wheres_the_beer.lib.config import config


@view_config(route_name='home', renderer='templates/homepage.pt')
def my_view(request):
    google_maps_key = config.get('google_maps_key')
    return {'google_maps_key': google_maps_key}
