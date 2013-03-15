import sys

from socketio.server import SocketIOServer
from pyramid.paster import get_app
from gevent import monkey; monkey.patch_all()
import gevent

from wheres_the_beer.lib import config

def broadcast_msg(server, ns_name, event, *args):
    pkt = dict(type="event",
               name=event,
               args=args,
               endpoint=ns_name)

    for sessid, socket in server.sockets.iteritems():
        socket.send_packet(pkt)

def send_tweets(server):
    # stream = tweetstream.SampleStream(user, password)
    # for tweet in stream:
    #     broadcast_msg(server, '/tweets', 'tweet', tweet)

    while True:
        print 'sending tweet'
        broadcast_msg(server, '/tweets', 'tweet', 'my_tweet')
        import time
        time.sleep(1)

if __name__ == '__main__':

    app = get_app(sys.argv[1])

    print 'Listening on port http://0.0.0.0:8080 and on port 10843 (flash policy server)'

    server = SocketIOServer(('0.0.0.0', 8080), app,
                            resource="socket.io", policy_server=True,
                            policy_listener=('0.0.0.0', 10843))
    gevent.spawn(send_tweets, server)
    server.serve_forever()