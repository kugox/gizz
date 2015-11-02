__author__ = 'Kugox'
import web

urls = ('/user', 'user')
class user:
    def GET(self):
        return "user!" 


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()