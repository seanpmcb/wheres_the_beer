from pyramid.config import Configurator

from wheres_the_beer.lib import config as conf

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    conf.set_config(global_config)

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('old_data', '/old_data')
    config.scan()
    return config.make_wsgi_app()
