from flask import Flask
from bucket_app.user_controller import UserAuth


#This initializes the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = "9(et*u4507(malazdm1z#tj&n^xwj*3+p!=!d$me@u#&p8e52d"

auth = UserAuth()
bucket = auth.bucket_controller


from bucket_app import views

app.config.from_object('config')