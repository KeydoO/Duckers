from api import API
from middleware import Middleware

app = API()

    
def custom_exception_handler(request, response, exception_cls):
    response.text = "Oops! Something went wrong. Please, contact our customer support at +1-202-555-0127."
app.add_exception_handler(custom_exception_handler)


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)

app.add_middleware(SimpleCustomMiddleware)


@app.route("/home")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be user")
    
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"
    
    
@app.route("/book")
class BooksHandler:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"
        
        
@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template("index.html", context={"name": "Duckers", "title": "Best Framework"}).encode()

