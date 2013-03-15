from socketio.namespace import BaseNamespace

class TweetsNamespace(BaseNamespace):
    def on_tweet(self, msg):
        self.emit('tweets', msg)

def socketio_service(request):
    socketio_manage(request.environ, {'/tweets': ChatNamespace},
                    request)
    return "out"