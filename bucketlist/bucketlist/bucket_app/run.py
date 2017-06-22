from flask import Flask, render_template, redirect, request

from bucket_app.forms import RegistrationForm, LoginForm, CreateBucketListForm
from controllers.user_controller import UserAuth
from controllers.bucket_controller import BucketController

app = Flask(__name__)
auth = UserAuth()
bucket = BucketController()




@app.route('/register', methods=["GET", "POST"])
def register():
    if auth.current_user.is_logged_in:
        return redirect('/bucket')

    form = RegistrationForm(csrf_enabled=False)

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        response = auth.add_user(name, email, password)
        if type(response) == list:
            return redirect('/login')
            print(response)
            print(name, password)
        elif response == 'That email is taken':
            redirect('/register')
            print(response)

    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if auth.current_user.is_logged_in:
        return redirect('/bucket')

    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        response = auth.login(email, password)
        print(response)
        if response == 'Welcome':
            print(auth.current_user)
            return redirect('/bucket')

    return render_template('login.html', form=form)


@app.route('/bucket', methods=['GET', 'POST'])
def create_bucket_list():
    form = CreateBucketListForm(csrf_enabled=False)

    if form.validate_on_submit():
        name = form.bucket_name.data
        b = bucket.create_bucket(auth.current_user.email, name, completion_status="On Ice")

        return redirect('/main')

    return render_template('create_list.html', form=form)

    return render_template('view_bucket_items.html', single_bucket=single_bucket)


if __name__ == '__main__':
    app.run(debug=True)
