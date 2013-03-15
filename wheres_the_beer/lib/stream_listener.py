import tweepy

import logging
log = logging.getLogger(__name__)

class StreamListener(tweepy.StreamListener):

    def __init__(self, callback, server, ns_name, event, *args, **kwargs):
        super(StreamListener, self).__init__(*args, **kwargs)
        self.server = server
        self.callback = callback
        self.ns_name = ns_name
        self.event = event

    def on_status(self, status):
        if status.geo and status.geo.get('coordinates'):
            the_dict = {
                'id_str': status.id_str,
                'coordinates': status.geo['coordinates'],
                'text': status.text,
                'username': status.user.screen_name,
                'user_id': status.user.id
            }
            self.callback(self.server, self.ns_name, self.event, the_dict)
            log.info('spm')
