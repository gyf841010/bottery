#!/usr/bin/python
# coding=utf-8

import os
import json
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.httpclient
import tornado.options
from tornado.options import define, options

import logging
from tornado.httpserver import HTTPServer

import tornado.httputil

define("port", default=20004, help="run on the given port", type=int)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/calc/gen', calcHandler),
        ]
        configs = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug="no",
            gzip=True,
        )
        tornado.web.Application.__init__(self, handlers, **configs)
        self.http_client = tornado.httpclient.AsyncHTTPClient(max_clients=150)

    def listen(self, port, address="0.0.0.0", **kwargs):
        self.server = HTTPServer(self, **kwargs)
        self.server.listen(port, address)


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request)

    def filter(self, s):
        s = s.encode('utf-8')
        ret = s.replace("%", "%%")
        return "'%s'" % ret if len(ret) > 1 else "''"


# calc handler
class calcHandler(BaseHandler):
    def gen_lottery(self):
        lottery = []
        from random import randint

        while len(lottery) < 6:
            x = randint(1, 49)
            if x in lottery:
                continue
            lottery.append(x)
        lottery.sort()
        return lottery

    def get(self):
        lottery = self.gen_lottery()
        return self.write(json.JSONEncoder().encode({'status': 0, 'lottery': lottery}))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
