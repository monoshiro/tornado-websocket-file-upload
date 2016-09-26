import os

import tornado.web
import tornado.websocket
import tornado.ioloop

import json
import base64

from tornado.options import options, define

define(name='port',default=8000, type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')


class WSIndexHandler(tornado.websocket.WebSocketHandler):

    def on_message(self, message):

        message_ = json.loads(message)

        if message_['data'] is not None:

            print(message_)

            data = message_['data']
            data = data.split(';base64')[1].encode('utf-8')
            data = base64.b64decode(data)

            with open(os.path.join('resource', message_['file_name']), 'wb') as file:
                file.write(data)

if __name__ == '__main__':
    application = tornado.web.Application(
        handlers=[
            (r'/index', IndexHandler),
            (r'/ws_index', WSIndexHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'template'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        debug=True,
        autoreload=False
    )
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
