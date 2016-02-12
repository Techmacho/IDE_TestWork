import cherrypy

class HelloWorld(object):
    def index(self):
        return "<a href='/sh'>Test me</a>"
    index.exposed = True

    def sh(self):
        from sense_hat import SenseHat

        s=SenseHat()
        s.show_message("testing")
        return "Was that cool?"
    sh.exposed = True


cherrypy.quickstart(HelloWorld())