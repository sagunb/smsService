import twilio.twiml
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
SECRET_KEY = 'development key'
app.secret_key = SECRET_KEY


###
# Routing for your application.
###

@app.route('/')
def receive_sms():
    """Respond to a new sms"""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
