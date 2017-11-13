import json
import os
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

# This is a test route to ping the listening webhook
# You really just need the webhook route
@app.route("/intakeqwebhook")
def webhook():
    Print(request.data)
    return()


a
if __name__ == '__main__':
    app.run()

