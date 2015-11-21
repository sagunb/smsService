from sms_service import SmsService
from flask import Flask, request

app = Flask(__name__)
SECRET_KEY = 'development key'
app.secret_key = SECRET_KEY

###
# Singleton instances
###
sms_sender = SmsService()
available_doctors = ['4169488810', '+14162768158', '16472359220']


###
# Routing for your application.
###


@app.route('/newsms', methods=['GET', 'POST'])
def receive_sms():
    """Respond to a new sms"""

    from_number = request.values.get('From')
    body = request.values.get('Body')

    resp = sms_sender.reply_to_message()
    sos = "Dear MedMS volunteers. A patient with the following number: {} is requesting assistance. " \
          "Patient's message: {}".format(from_number, body)
    failed_messages = sms_sender.send_new_message(sos, get_available_doctors())

    return str(resp)


def get_available_doctors():
    return available_doctors


@app.route('/')
def hello():
    return 'O Hai!'

if __name__ == '__main__':
    app.run(debug=True)
