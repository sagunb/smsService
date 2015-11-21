import twilio.twiml
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
SECRET_KEY = 'development key'
app.secret_key = SECRET_KEY


###
# Routing for your application.
###

@app.route('/newsms', methods=['GET', 'POST'])
def receive_sms():
    """Respond to a new sms"""

    from_number = request.values.get('From')
    body = request.values.get('Body')

    if from_number and body:
        msg = "You sent us: {}".format(body)
    else:
        msg = "Successful reception"

    resp = twilio.twiml.Response()
    resp.message(msg)

    return str(resp)


@app.route('/')
def hello():
    """Respond to a new sms"""

    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
