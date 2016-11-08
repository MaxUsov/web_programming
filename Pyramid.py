from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from jinja2 import Environment, FileSystemLoader,Template

env = Environment(loader=FileSystemLoader('HTML'))

def AboutMe(request):
    template = env.get_template('/about/aboutme.html').render(link = """<a href = "/index.html">Ссылка на Index</a>""", head = """<h1>About me</h1>""")
    return Response(template)

def Index(request):
    template = env.get_template('index.html').render(link = """<a href = "/about/aboutme.html">Ссылка на AboutMe</a>""", head = """<h1>Index</h1>""")
    return Response(template)

if __name__ == '__main__':
    configure = Configurator()
    configure.add_route("aboutme",'/about/aboutme.html')
    configure.add_view(AboutMe,route_name = 'aboutme')
    configure.add_route('index', '/index.html')
    configure.add_view(Index, route_name = 'index')
    app = configure.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()