from flask import Flask
from route.admin import admin_route

app = Flask(__name__)
app.register_blueprint(admin_route)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
