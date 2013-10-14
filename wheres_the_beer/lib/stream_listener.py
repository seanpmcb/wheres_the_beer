import re

import tweepy
from tweepy.utils import import_simplejson as json

import logging
log = logging.getLogger(__name__)

class StreamListener(tweepy.StreamListener):

    def __init__(self, callback, server, ns_name, event, words=[], *args, **kwargs):
        super(StreamListener, self).__init__(*args, **kwargs)
        self.server = server
        self.callback = callback
        self.ns_name = ns_name
        self.event = event
        print '|'.join(words)
        self.words = re.compile('|'.join(words), re.IGNORECASE)

    def _matched_word(self, text):
        result = self.words.search(text)
        if result:
            return result.group()
        return None

    def on_status(self, status):
        if status.geo and status.geo.get('coordinates'):
            the_dict = {
                'id_str': status.id_str,
                'coordinates': status.geo['coordinates'],
                'text': status.text,
                'username': status.user.screen_name,
                'user_id': status.user.id,
                'matched_word': self._matched_word(status.text)
            }
            try:
                self.callback(self.server, self.ns_name, self.event, the_dict)
            except:
                pass
