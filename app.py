import twilio.twiml
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
SECRET_KEY = 'development key'
app.secret_key = SECRET_KEY


###
# Routing for your application.
###

@app.route('/newsms')
def receive_sms():
    """Respond to a new sms"""

    try:
        resp = twilio.twiml.Response()
        resp.message("Hello, Mobile Monkey")
    except Exception as e:
        resp = 'There was an error: {}'.format(str(e))
    return str(resp)


@app.route('/')
def hello():
    """Respond to a new sms"""

    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
