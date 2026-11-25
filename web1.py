from flask import Flask
2  app = Flask(__name__)
3  
4  @app.route("/")
5  def hello():
6      return "Hello, World!"



@app.route("/")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"



@app.route("/")
def index():
    return "Welcome!"

@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"

@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"



from flask import request

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return '''
    <form method="post">
      <input name="name">
      <button>Send</button>
    </form>'''


