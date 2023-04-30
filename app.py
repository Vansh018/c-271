from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID = 'AC94a5e738e69de142856bd939a670168c'
    TWILIO_SYNC_SERVICE_SID = 'IS0804f7e69c6bed89f51272c5aebb6588'
    TWILIO_API_KEY = 'SK0f348b61c091bea75fce18350dd7d383'
    TWILIO_API_SECRET = 'jiaO73FNVQaAuhptK6LB2RvVcAoXSsHz'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

