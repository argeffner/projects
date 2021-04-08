from flask import Flask, render_template, request, jsonify, redirect, session, flash
import requests
from flask_debugtoolbar import DebugToolbarExtension
from models import Cats, Adopt, db, connect_db, User, Cost
from forms import NewUserForm, LoginForm, DeleteForm
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///catdopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'meow'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

CAT_KEY = "results"
IMG_KEY = 'kitty'
data_breeds = ['abyssinian', 'aegean', 'american bobtail', 'american curl', 'american shorthair', 'american wirehair', 'arabian mau', 'balinese', 'bambino', 'bengal', 'birman', 'bombay', 'british longhair', 'british shorthair', 'burmese', 'burmilla', 'california spangled', 'chantilly-tiffany', 'chartreux', 'chausie', 'cheetoh', 'colorpoint shorthair', 'cornish rex', 'cyprus', 'devon rex', 'donskoy', 'dragon li', 'egyptian mau', 'european burmese', 'exotic shorthair', 'havana brown', 'himalayan', 'japanese bobtail', 'javanese', 'khao manee', 'korat', 'kurilian', 'laperm', 'maine coon', 'malayan', 'manx', 'munchkin', 'nebelung', 'norwegian forest cat', 'ocicat', 'oriental', 'persian', 'pixie-bob', 'ragamuffin', 'ragdoll', 'russian blue', 'savannah', 'scottish fold', 'selkirk rex', 'siamese', 'siberian', 'singapura', 'snowshoe', 'somali', 'sphynx', 'tonkinese', 'toyger', 'turkish angora', 'turkish van', 'york chocolate']

connect_db(app)
db.create_all()

url = "https://api.thecatapi.com/v1/breeds/search"
headers = {'x-api-key': '82cef8ce-039b-47e9-a74f-f6a7053171cd'}

url_img = 'https://api.thecatapi.com/v1/images/search'



@app.route('/')
def home_route():
    """Show form."""
    # show intro and provide login or signup
    return render_template('home.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup."""

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = NewUserForm()
   
    if form.validate_on_submit():
        # collects data from the form inputs by user
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User.signup(username, password, email)
        db.session.commit()
        session["username"] = user.username
        flash('Welcome to our site!', 'success')
        return redirect(f"/users/{user.username}")
    else:  
        return render_template("signup.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password.']
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    session.pop("username")
    return redirect('/')


@app.route('/users/<username>')
def show_username(username):
    if "username" not in session or username != session['username']:
        # flash('You need to Login or Signup')
        # return redirect ('/')
        raise Unauthorized()

    user = User.query.get(username)
    form = DeleteForm()
    cats = Cats.query.all()
    adopt = Adopt.query.all()

    return render_template('show.html', user=user, form=form, cats=cats, adopt=adopt)

############# Doesn't work ######################
@app.route('/users/<username>/delete', methods=['POST'])
def delete_user(username):
    if "username" not in session or username != session['username']:
        # flash('You need to Login or Register')
        # return redirect ('/')
        raise Unauthorized()

    user = User.query.get(username)
    db.session.delete(user)
    db.session.commit()
    # need the session.pop('username') to avoid error message
    session.pop('username')

    return redirect('/')


@app.route('/users/<username>/options', methods=['POST'])
def get_data(username):

    if "username" not in session or username != session['username']:
        raise Unauthorized()
    
    user = User.query.get(username)
    breed = request.form.get("feline")
    breed = breed.lower()
    
    if breed not in data_breeds:
        flash(f'{breed} is not a cat breed')
        return redirect(f'/users/{user.username}')
    
    q = {'name': breed}
    res = requests.get(url, headers=headers, params=q)
    cat = res.json()

    # kitty = session[IMG_KEY]  # kitty[#][1]['item'] 
    for i in range(0, len(cat)):
        q_img = {'limit': '5', "breed_id": cat[i]['id']}
        r_img = requests.get(url_img, headers=headers, params=q_img)
        img = r_img.json()

        # print(len(img))
        if len(img) > 0:
            for j in range(0, len(img)):
                # kitty.append({'image': img[j]['url'], responses[i]})
                if Cats.query.filter_by(img=img[j]['url']).first() is None: 
                    cats = Cats(img=img[j]['url'], breed=cat[i]['name'])
                    db.session.add(cats)
                    db.session.commit()
                # return redirect(f'/users/{user.username}')
                kitties = Cats.query.all()
                adopt = Adopt.query.all()
                # flash(len(img))
                return render_template('show.html', cats=kitties, user=user, adopt=adopt)


@app.route('/users/<username>/info/<int:id>', methods=['GET'])
def get_breed_info(username, id):

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    cat = Cats.query.get_or_404(id)
    q = {'name': cat.breed}
    res = requests.get(url, headers=headers, params=q)
    cat = res.json()

    session[CAT_KEY] = []
    responses = session[CAT_KEY]

    for i in range(0, len(cat)):
        responses.append({
            "breed": cat[i]['name'], 
            "origin": cat[i]['origin'], 
            "life span": cat[i]['life_span'], 
            "description": cat[i]['description']
            })
    return render_template('info.html', responses=responses, user=user)


@app.route('/users/<username>/delete/<int:id>', methods=['POST'])
def delete_cat(username, id):
    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    cat = Cats.query.get_or_404(id)

    db.session.delete(cat)
    db.session.commit()
    flash('Cat deleted from list.')

    return redirect(f'/users/{user.username}')


@app.route('/users/<username>/adopt/<int:id>', methods=['POST'])
def adopt_a_cat(username, id):

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    cat_name = request.form.get("cat_name")
    user = User.query.get(username)
    cat = Cats.query.get_or_404(id)
    cat_img = cat.img
    u = user.username

    adopt = Adopt(user=u, cat_name=cat_name, cat_img=cat_img)
    db.session.add(adopt)
    db.session.commit()
    # delete causes foreignkey issue
    db.session.delete(cat)
    db.session.commit()
    # flash('Item deleted.')

    return redirect(f'/users/{user.username}')


@app.route('/users/<username>/checkout', methods=['POST'])
def pay_for_adoption(username):

    if "username" not in session or username != session['username']:
        raise Unauthorized()
    
    user = User.query.get(username) 
    numCats = Adopt.query.count()
    price = 100 * numCats
    adopt = Adopt.query.all()
    
    cost = Cost(user_id=username, price=price)
    db.session.add(cost)
    db.session.commit()
    # since there is no pay route it will simply logout
    # return redirect('/logout')
    return render_template('checkout.html', cost=cost, adopt=adopt, user=user)


@app.route('/users/<username>/finished', methods=['POST'])
def clear_all(username):

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username) 
    cats = Cats.query.all()
    adopt = Adopt.query.all()
    cost = Cost.query.all()

    for cat in cats:
        db.session.delete(cat)
        db.session.commit()
    for a in adopt:
        db.session.delete(a)
        db.session.commit()
    for c in cost:
        db.session.delete(c)
        db.session.commit()

    return redirect('/logout')










# This is for testing only 

@app.route('/test')
def get_data_test():
    breed = request.args["newish"]
    q = {'name': breed}
    res = requests.get(url, headers=headers, params=q)
    cat = res.json()
    
    for i in range(0, len(cat)):
        q_img = {'limit': '4', "breed_id": cat[i]['id']}
        r_img = requests.get(url_img, headers=headers, params=q_img)
        img = r_img.json()
        # print img based on length 
        print(len(img))
        if len(img) > 0:
            for j in range(0, len(img)):
                print(img[j]['url']) 
    
    
     
    # Early stage testing nothing here is currently permanent
    
   
    # make data bases with data about breed, origin, lifespan, description
    print (cat[0]['name'])
    print(cat[0]['origin'])
    print(cat[0]['life_span'], 'years')
    print(cat[0]['description'])
    print('******************************************************************')
    return jsonify(cat)  