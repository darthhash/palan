import os

bind = "0.0.0.0:" + os.environ.get("PORT", "8080")
wsgi_app = "app:app"
workers = 1
loglevel = "debug"
capture_output = True
