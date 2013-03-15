from pyramid.config import Configurator

from wheres_the_beer.lib import config as conf

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    conf.set_config(global_config)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
