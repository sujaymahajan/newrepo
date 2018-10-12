ROW_LIMIT = 5000
WEBSERVER_THREADS = 4
SUPERSET_WEBSERVER_PORT = 8088
SUPERSET_WEBSERVER_TIMEOUT = 60
SECRET_KEY = 'thisismysecretkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:////mnt/superset.db'
CSRF_ENABLED = True
HTTP_HEADERS = {}
 
# https://stackoverflow.com/questions/48966344/assign-anonymoususermixin-to-a-real-user
AUTH_TYPE = 3
class PredefinedUserMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['REMOTE_USER'] = 'admin'
        return self.app(environ, start_response)
ADDITIONAL_MIDDLEWARE = [PredefinedUserMiddleware]
 
