import tweepy

import json

import logging
log = logging.getLogger(__name__)

class StreamListener(tweepy.StreamListener):

    def __init__(self, callback, server, ns_name, event, *args, **kwargs):
        super(StreamListener, self).__init__(*args, **kwargs)
        self.server = server
        self.callback = callback
        self.ns_name = ns_name
        self.event = event
        self.tweetfile = open('wheres_the_beer/static/data.json', 'a', 1)

    def on_status(self, status):
        if status.geo and status.geo.get('coordinates'):
            the_dict = {
                'id_str': status.id_str,
                'coordinates': status.geo['coordinates'],
                'text': status.text,
                'username': status.user.screen_name,
                'user_id': status.user.id
            }
            try:
                self.callback(self.server, self.ns_name, self.event, the_dict)
                data = json.dumps(the_dict)
                self.tweetfile.write(data + '\n')
            except:
                pass
