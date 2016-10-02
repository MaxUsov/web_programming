import os

top = "<div class='top'>Middleware TOP</div>"
bottom = "<div class='botton'>Middleware BOTTOM</div>"

 class MiddleWare:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
		response = self.app(environ, start_response)[0] 
		if (page.find('<body>') > 0):
            header, body = page.split('<body>')
            page = header + '<body>\n' + top + body
            header, body = page.split('</body>')
            page = header + bottom + '\t</body>' + body
        return page
    

def app(environ, start_response):
    
    path = environ['PATH_INFO']
    filePath = '.' + path  
    if not os.path.isfile(filePath):
        filePath ='./index.html' 

    appfile = open(filepath, 'r')
    fileContent = appfile.read()

    appfile.close()
    
    start_response('200 OK', [('Content-type', 'text/HTML')])
    return [fileContent ]

app = MiddleWare(app)


if __name__ == '__main__':
    from paste import reloader
    from paste.httpserver import serve

    reloader.install()
    serve(app, host='127.0.0.1', port=8000)