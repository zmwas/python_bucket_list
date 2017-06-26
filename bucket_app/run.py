from user_controller import UserAuth
from flask import (Flask, render_template,
                   redirect, request)
from forms import (RegistrationForm,
                   LoginForm, CreateBucketListForm,
                   CreateBucketItemForm, UpdateBucketListForm, UpdateBucketItemForm, STATUS)
from bucket_controller import BucketController

app = Flask(__name__)
auth = UserAuth()
bucket = BucketController()
val = 0


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


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

        return redirect(request.referrer)

    return render_template('create_list.html', form=form)


@app.route('/update/<int:id>',methods=['GET','POST'])
def update_bucket(id):
    if not auth.current_user.is_logged_in:
        return redirect('/')
    val = id -1
    u_form = UpdateBucketListForm(csrf_enabled=False)
    if u_form.validate_on_submit():
        name = u_form.bucket.data
        status = dict(STATUS).get(u_form.completion_status.data)
        print(name)
        bucket.update_bucket(auth.current_user.email, val, name, status)
    return redirect(request.referrer)


@app.route('/main', methods=['GET','POST'])
def view_bucket_lists():
    """
    View that renders the bucket lists
    """

    if not auth.current_user.is_logged_in:
        return redirect('/')
    form = CreateBucketListForm(csrf_enabled=False)
    if form.validate_on_submit() and form.submit.data:
        bucket.add_bucket_item(auth.current_user.email, val, form.bucket_name.data)
        print(bucket.bucket_list_dictionaries)
        return redirect(request.referrer)

    buckets = bucket.bucket_list_dictionaries.get(auth.current_user.email)


    u_form = UpdateBucketListForm(csrf_enabled=False)
    if u_form.validate_on_submit():
        name = u_form.bucket.data
        status = dict(STATUS).get(u_form.completion_status.data)

        bucket.update_bucket(auth.current_user.email, id, name, status)
        return redirect(request.referrer)

    if buckets:
        return render_template('main_page.html', buckets=buckets, form=form, u_form=u_form)
    else:
        return render_template('main_page.html', form=form, u_form=u_form)


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
        return redirect(request.referrer)

    buckets = bucket.bucket_list_dictionaries.get(auth.current_user.email)
    if val > len(buckets):
        return redirect('page_not_found')

    single_bucket = buckets[int(val) - 1]

    u_form = UpdateBucketListForm(csrf_enabled=False)
    if u_form.validate_on_submit():
        name = u_form.bucket.data
        status = dict(STATUS).get(u_form.completion_status.data)
        bucket.update_bucket(auth.current_user.email, val, name, status)
        return redirect(request.referrer)

    return render_template('view_bucket_items.html', single_bucket=single_bucket, form=form, u_form=u_form, id=id)


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
    return redirect(request.referrer)


@app.route('/remove/<id>/<name>')
def delete_bucket_item(id, name):
    """
    View that  deletes bucket lists item
    """
    if not auth.current_user.is_logged_in:
        return redirect('/')
    val = int(id) - 1
    bucket.delete_bucket_item(auth.current_user.email, val, name)
    return redirect(request.referrer)


@app.route('/update/<int:id>/<name>',methods=['PUT'])
def update_bucket_item(id, name):
    if not auth.current_user.is_logged_in:
        return redirect('/')

    val = id - 1
    u_form = UpdateBucketItemForm(csrf_enabled=False)
    if u_form.validate_on_submit():
        name = form.bucket.data
        name = form.bucket.data
        status = dict(STATUS).get(u_form.completion_status.data)

    bucket.update_bucket_item(auth.current_user.email, val, name, completion_status)
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug=True)
