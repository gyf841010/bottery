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
import datetime
import config
import time

define("port", default=20004, help="run on the given port", type=int)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', mainHandler),
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


# main handler
class mainHandler(BaseHandler):
    def get(self):
        return self.render("index.html")


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
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        lottery_open_time_str = str(today) + " 09:34:59"
        lottery_open_time = time.strptime(lottery_open_time_str, '%Y-%m-%d %H:%M:%S')
        open_timestamp = time.mktime(lottery_open_time)
        now = time.time()
        if now > open_timestamp:
            f_dir = config.SAVE_FOLDER + str(today)
            if os.path.isfile(f_dir):
                with open(f_dir, 'r') as f:
                    lottery = [int(str) for str in f.readline().split(',')]
            else:
                with open(f_dir, 'w') as f:
                    lottery = self.gen_lottery()
                    f.write(','.join(str(i) for i in lottery))
        else:
            f_dir = config.SAVE_FOLDER + str(yesterday)
            with open(f_dir, 'r') as f:
                lottery = [int(str) for str in f.readline().split(',')]

        return self.write(json.JSONEncoder().encode({'date': str(today), 'lottery': lottery}))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
