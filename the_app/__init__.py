from flask import Flask

app = Flask(__name__, instance_relative_config=True)#creamos app
app.config.from_object("config")


from the_app import routes