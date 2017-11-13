import json
import os
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

# This is a test route to ping the listening webhook
# You really just need the webhook route
@app.route("/")
def hello():
    test_payload = {
      'IntakeId': "00000000-0000-0000-0000-000000000000",
      'Type': "Intake Submitted",
      'ClientId': 123
    }

    response = requests.post('http://localhost:5001/intakeqwebhook', test_payload)

    return "I am listening! I just sent {}, it returned {}".format(
        json.dumps(test_payload), json.dumps(response.content.decode()))





@app.route("/intakeqwebhook2")
def webhook():
    print(request.data)
    return "blahblahblah"




# THIS IS ALL YOU NEED
@app.route("/intakeqwebhook", methods=['POST'])
def listener():
    headers = {'X-Auth-Key': os.environ.get('INTAKEQ_API_KEY')}

    #response = requests.get('intakeq.com/api/{}'.format(request.form['IntakeId']), headers=headers)
    # response will contain all the data from the user's form
    # Then you can do whatever you want with it: AKA, translate it into HL7 and send it to Avreo
    return "Intake ID: {} sent to intakeq to retrieve form data.".format(request.form['IntakeId'])
    
if __name__ == '__main__':
    app.run()

