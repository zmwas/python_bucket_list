from controllers.user_controller import UserAuth
from flask import (Flask, render_template,
                   redirect, request)
from bucket_app.forms import (RegistrationForm,
                              LoginForm, CreateBucketListForm,
                              CreateBucketItemForm)

from controllers.bucket_controller import BucketController

app = Flask(__name__)
auth = UserAuth()
bucket = BucketController()
val = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    View that renders the index page
    """

    if auth.current_user.is_logged_in:
        return redirect('/main')

    login_form = LoginForm(csrf_enabled=False)
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        response = auth.login(email, password)
        if response == 'Welcome':
            return redirect('/main')

    registration_form = RegistrationForm(csrf_enabled=False)

    if registration_form.validate_on_submit():
        name = registration_form.name.data
        email = registration_form.email.data
        password = registration_form.password.data
        response = auth.add_user(name, email, password)
        if type(auth.add_user(name, email, password)) == list:
            return redirect('/')
        elif response == 'That email is taken':
            redirect('/')

    return render_template('index.html', login_form=login_form,
                           registration_form=registration_form)


@app.route('/bucket', methods=['GET', 'POST'])
def create_bucket_list():
    """
    View that renders the bucket list  creation form
    """
    if not auth.current_user.is_logged_in:
        return redirect('/')

    form = CreateBucketListForm(csrf_enabled=False)

    if form.validate_on_submit():
        name = form.bucket_name.data
        bucket.create_bucket(auth.current_user.email, name,
                             completion_status="On Ice")

        return redirect('/main')

    return render_template('create_list.html', form=form)


@app.route('/main', methods=['GET'])
def view_bucket_lists():
    """
    View that renders the bucket lists
    """

    if not auth.current_user.is_logged_in:
        return redirect('/')
    form = CreateBucketListForm(csrf_enabled=False)
    if form.validate_on_submit():
        bucket.add_bucket_item(auth.current_user.email, val, form.bucket_name.data)
        print(bucket.bucket_list_dictionaries)

    buckets = bucket.bucket_list_dictionaries.get(auth.current_user.email)

    if buckets:
        return render_template('main_page.html', buckets=buckets, form=form)
    else:
        return render_template('main_page.html', form=form)


@app.route('/<int:id>', methods=['GET'])
def view_bucket_items(id):
    """
    View that renders the bucket items page
    """
    if not auth.current_user.is_logged_in:
        return redirect('/')
    val = id
    form = CreateBucketItemForm(csrf_enabled=False)
    if form.validate_on_submit():
        bucket.add_bucket_item(auth.current_user.email, val, form.bucket_item_name.data)
        print(bucket.bucket_list_dictionaries)
        return redirect('/main')

    buckets = bucket.bucket_list_dictionaries.get(auth.current_user.email)
    single_bucket = buckets[int(val) - 1]

    return render_template('view_bucket_items.html', single_bucket=single_bucket, form=form, id=id)


@app.route('/bucket-item', methods=['GET', 'POST'])
def create_bucket_items():
    if not auth.current_user.is_logged_in:
        return redirect('/')
    form = CreateBucketItemForm(csrf_enabled=False)
    if form.validate_on_submit():
        bucket.add_bucket_item(auth.current_user.email, val, form.bucket_item_name.data)
        print(bucket.bucket_list_dictionaries)
        return redirect(request.referrer)

    return render_template("create_items.html", form=form, id=id)


@app.route('/remove/<id>')
def delete_bucket(id):
    """
    View that renders the deletes bucket lists
    """
    if not auth.current_user.is_logged_in:
        return redirect('/')
    val = int(id) - 1
    bucket.delete_bucket(auth.current_user.email, val)
    return redirect('/main')


@app.route('/remove/<id>/<name>')
def delete_bucket_item(id, name):
    """
    View that  deletes bucket lists item
    """
    if not auth.current_user.is_logged_in:
        return redirect('/')
    val = int(id) - 1
    bucket.delete_bucket_item(auth.current_user.email, val, name)
    return redirect('/main')


if __name__ == '__main__':
    app.run(debug=True)
