import sys

from socketio.server import SocketIOServer
from pyramid.paster import get_app
from gevent import monkey; monkey.patch_all()
import gevent
import tweepy

from wheres_the_beer.lib import config
from wheres_the_beer.lib.stream_listener import StreamListener

def broadcast_msg(server, ns_name, event, *args):
    pkt = dict(type="event",
               name=event,
               args=args,
               endpoint=ns_name)

    for sessid, socket in server.sockets.iteritems():
        socket.send_packet(pkt)

def send_tweets(server):
    auth = tweepy.auth.OAuthHandler(config.get('twitter_key'),
                                    config.get('twitter_secret'))
    auth.set_access_token(config.get('twitter_access_token'),
                          config.get('twitter_access_secret'))
    listener = StreamListener(broadcast_msg, server, '/tweets', 'tweet')
    streamer = tweepy.Stream(auth=auth, listener=listener, secure=True,
                             retry_count=2)

    track = config.get('search_for').split(',')

    streamer.filter(track=track)


if __name__ == '__main__':

    app = get_app(sys.argv[1])

    print 'Listening on port http://0.0.0.0:8080 and on port 10843 (flash policy server)'

    server = SocketIOServer(('0.0.0.0', 8080), app,
                            resource="socket.io", policy_server=True,
                            policy_listener=('0.0.0.0', 10843))
    gevent.spawn(send_tweets, server)
    server.serve_forever()