from flask import Flask, request
from app import *


application = create_app("dev_saska")

with application.app_context():
    DB.create_all()

if __name__ == '__main__':
    # Run the app.
    application.run()
