import cherrypy

class HelloWorld(object):
    def index(self):
        return "<a href='/sh?foo=test'>Test me</a>"
    index.exposed = True

    def sh(self,foo=None):
        from sense_hat import SenseHat

        s=SenseHat()
        s.show_message(foo)
        return "Was that cool?"
    sh.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(HelloWorld())