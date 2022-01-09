import tornado.ioloop
import tornado.web
import platform

class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"response": "System OK",
                    "OS": platform.platform()})
    
class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"response": "Hello, World"})


def make_app():
    return tornado.web.Application([
        (r"/", HealthCheckHandler),
        (r"/hello", HelloWorldHandler)
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()