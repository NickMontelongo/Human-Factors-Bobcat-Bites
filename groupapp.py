"""Main APP file, instantiates the app, database, encryptor, as
well as contains the definitions for the table models and the
flask forms documentation"""

import random
import os
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

# login information
from flask_login import LoginManager, UserMixin
from flask_login import logout_user, login_user, login_required, current_user

#Algorithm information
from searchalgorithm import food_recommendation,stringToArray
from hardcodedrestaurants import masterListRestaurants
# used to create form objects such as the search bar
from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, PasswordField, DecimalField, TextAreaField, widgets
from wtforms.validators import email, length, InputRequired, ValidationError, DataRequired
from wtforms_alchemy import QuerySelectMultipleField

# used for hashing/encrypting password
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# bcrypt object is utilized in password hashing/encryption
bcrypt = Bcrypt(app)

#Importing Individually Defined restaurant lists
from hardcodedrestaurants import masterListRestaurants


# fetches session key and Database URI from .env file
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

# database declaration / login declaration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

database = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    """used by login manager to load user based on their id"""
    return Person.query.get(int(user_id))

currentUserAllergens =[]
currentUserTastes =[]
currentUserFoodPreferences = ''
currentUserMaxBudget = 0
currentUserMinBudget= 0
masterListWithRecommendation =[]

#######################################FLASK FORMS ####################################################
class QuerySelectMultipleFieldWithCheckboxes(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ProfileForm(FlaskForm):
    """Class that will be utilized in profile.html to create the user fields for 
    profile creation """
    taste_choices = QuerySelectMultipleFieldWithCheckboxes("Flavor Choices", get_label='taste_name')
    allergen_choices = QuerySelectMultipleFieldWithCheckboxes("Allergen Choices", get_label='allergen_name')
    budget_min = DecimalField(validators=[InputRequired()],places=2)
    budget_max = DecimalField(validators=[InputRequired()],places=2)
    user_preferred_ingredients = TextAreaField(
        [InputRequired(), length(min=0, max=400)],
        render_kw={"Placeholder": "Input ingredients here in ingredient, format (Maximum 400 characters)"},
    )
    submit = SubmitField("Create User Profile")

class DisplayResultsForm(FlaskForm):
    accept = SubmitField("Approve")
    deny = SubmitField("Deny")

#I need to figure/fix this to add a search bar
class DisplaySearchResults(FlaskForm):
    submit = SubmitField("Search for Result")

class RegisterForm(FlaskForm):
    """Class that will be utilized by register.html to create the user entry field
    objects that will transfer the data"""

    user_email = EmailField(
        validators=[
            InputRequired(),
            email(
                message="Invalid. Please enter a valid email", allow_empty_local=True
            ),
            length(min=3, max=30),
        ],
        render_kw={"placeholder": "Your Email"},
    )
    user_password = PasswordField(
        validators=[InputRequired(), length(min=9, max=30)],
        render_kw={"placeholder": "Password"},
    )
    submit = SubmitField("Register User")

    def validate_user_email(self, user_email):
        """function used in Registration form to determine if the user email
        pre-exists raising an error
        Parameters: (string-user email)
        Returns: Error"""
        existing_user = Person.query.filter_by(email=user_email.data).first()
        if existing_user:
            raise ValidationError(
                "Email already on file, please login via the link below or register a different one."
            )
        

class LoginForm(FlaskForm):
    """Class that will be utilized by login.html to create the user entry field
    objects that will transfer the data"""

    user_email = EmailField(
        "Email",
        validators=[
            InputRequired("Please enter your email here"),
            email(
                message="Invalid. Please enter a valid email", allow_empty_local=True
            ),
            length(min=3, max=30),
        ],
        render_kw={"placeholder": "Your Email"},
    )

    user_password = PasswordField(
        "Password",
        validators=[
            InputRequired("Please enter your password here"),
            length(min=9, max=30),
        ],
        render_kw={"placeholder": "Password"},
    )
    submit = SubmitField("Login User")

    # to do: how to validate if something is an email? What requires a string to be an email
    def validate_user_email(self, user_email):
        """Function used by Loginform that checks to see if the email is valid and
        that the email exists in our database
        Parameters: (email entered by user)
        Returns: Validation Error"""
        existing_email = Person.query.filter_by(email=user_email.data).first()
        if not existing_email:
            raise ValidationError(
                "This email is not in our records. Please sign up with your email."
            )

###############################MODELS FOR DATABASE ######################################################

class Person(database.Model, UserMixin):
    """Person class that will be used to store the email and password information"""
    #login info for person
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(30), unique=True, nullable=False)
    hashed_password = database.Column(
        database.LargeBinary(60), unique=False, nullable=False
    )
    #profile info 
    budget_max = database.Column(database.Float)
    budget_min = database.Column(database.Float)
    preferred_ingredients = database.Column(database.String(200))
    tastes = database.relationship("Taste", secondary="person_taste", back_populates="persons")
    allergens = database.relationship("Allergen", secondary="person_allergen", back_populates="persons")
    #users favorite foods
    userfavoritefoods = database.relationship("Userfavoritefood", secondary="person_userfavoritefood", back_populates="persons")

    

class Taste(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    taste_name = database.Column(database.String(10), unique=True, nullable=False)
    #link to person
    persons = database.relationship("Person", secondary="person_taste", back_populates="tastes")
    def __repr__(self):
        return self.taste_name
    
database.Table(
        "person_taste",
        database.Column("person_id", database.ForeignKey("person.id"), primary_key = True),
        database.Column("taste_id", database.ForeignKey("taste.id"), primary_key = True)
    )

class Allergen(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    allergen_name = database.Column(database.String(20), unique=True, nullable=False)
    persons = database.relationship("Person", secondary="person_allergen", back_populates="allergens")
    #link to person
    def __repr__(self):
        return self.allergen_name

database.Table(
        "person_allergen",
        database.Column("person_id", database.ForeignKey("person.id"), primary_key = True),
        database.Column("allergen_id", database.ForeignKey("allergen.id"), primary_key = True)
    )


class Userfavoritefood(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    parent_restaurant = database.Column(database.String(20), nullable=False)
    food_name = database.Column(database.String(20), nullable=False)
    persons = database.relationship("Person", secondary="person_userfavoritefood", back_populates="userfavoritefoods")
    def __repr__(self):
        return self.food_name

database.Table(
        "person_userfavoritefood",
        database.Column("person_id", database.ForeignKey("person.id"), primary_key = True),
        database.Column("userfavoritefood_id", database.ForeignKey("userfavoritefood.id"), primary_key = True)
    )

def loadTastes():
    tasteArray = ["bitter", "salty", "savory", "sour", "spicy", "sweet", "none"]
    user_tastes = Taste.query.all()
    userTasteList = []
    for eachentry in user_tastes:
        userTasteList.append(eachentry.taste_name)
    for eachentry in tasteArray:
        if eachentry in userTasteList:
            continue
        else:
            taste1 = Taste(taste_name=eachentry)
            database.session.add(taste1)
        database.session.commit()
    return

def loadAllergens():
    allergen_array= ["beans", "beef", "cinnamon", "chicken", "dairy", "eggs", "fish", "gluten", "mustard",
                      "nuts", "pork", "potatoes", "shellfish", "tree nuts", "none"]
    user_allergens = Allergen.query.all()
    userAllergenList = []
    for eachentry in user_allergens:
        userAllergenList.append(eachentry.allergen_name)
    for eachentry in allergen_array:
            if eachentry in userAllergenList:
                continue
            else:
                allergen1 = Allergen(allergen_name=eachentry)
                database.session.add(allergen1)
            database.session.commit()
    return
########################################################################################################

# database creation
with app.app_context():
    database.create_all()

# app routes
@app.route("/")
def title():
    """renders a base page that allows user to be redirected to login or signup
    Parameters: (none)
    Returns: html file for display"""
    #Preload databases with tables
    loadAllergens()
    loadTastes()
    return render_template("title.html")

@app.route("/recommendbyrestaurant/<restaurant>", methods=["GET", "POST"])
@login_required
def getRecommendationByRestaurant(restaurant):
    form = DisplayResultsForm()
    #DEFINITION OF USER AND ASSOCIATED PROFILE VARIABLES
    user = Person.query.filter_by(email=current_user.email).first()
    currentUserFoodPreferences = stringToArray(user.preferred_ingredients)
    for eachEntry in user.tastes:
        if str(eachEntry) == "none":
            currentUserTastes.append("none")
            break
        currentUserTastes.append(str(eachEntry))   
    for eachEntry in user.allergens:
        if str(eachEntry) == "none":
            currentUserAllergens.append("none")
            break
        currentUserAllergens.append(str(eachEntry))
    currentUserMaxBudget = user.budget_max
    currentUserMinBudget = user.budget_min
    for eachEntry in masterListRestaurants:
        if eachEntry.restaurantName == restaurant:
            restaurantLocation = eachEntry.restaurantLocation
            currentRestaurantRecommendationList = food_recommendation(eachEntry, currentUserMinBudget,
                                                                      currentUserMaxBudget, currentUserFoodPreferences,
                                                                      currentUserAllergens, currentUserTastes)
            break
    recommendedRestaurantName = currentRestaurantRecommendationList[0].parentListName
    #TO DO: make File Path
    recommendedRestaurantName = recommendedRestaurantName.capitalize()
    recommendedFoodScore = currentRestaurantRecommendationList[0].recommendationScore
    recommendedFoodName = currentRestaurantRecommendationList[0].foodItemName
    return render_template("displayrec.html", restaurantLoc = restaurantLocation, restaurantName = recommendedRestaurantName,
                           foodScore = recommendedFoodScore, foodName=recommendedFoodName, form=form)


@app.route("/recommendrand/", methods=["GET", "POST"])
@login_required
def getRecommendationByRand():
    #Random Instantiation and use in masterlist
    randomIndex = random.randint(0,5)

    #DEFINITION OF USER AND ASSOCIATED PROFILE VARIABLES
    user = Person.query.filter_by(email=current_user.email).first()
    currentUserFoodPreferences = stringToArray(user.preferred_ingredients)
    for eachEntry in user.tastes:
        currentUserTastes.append(str(eachEntry))
    for eachEntry in user.allergens:
        currentUserAllergens.append(str(eachEntry))
    currentUserMaxBudget = user.budget_max
    currentUserMinBudget = user.budget_min
    return render_template("displayrand.html")

@app.route("/recommendbysearch/", methods=["GET", "POST"])
@login_required
def getRecommendationBySearch():
    #DEFINITION OF USER AND ASSOCIATED PROFILE VARIABLES
    user = Person.query.filter_by(email=current_user.email).first()
    currentUserFoodPreferences = stringToArray(user.preferred_ingredients)
    for eachEntry in user.tastes:
        currentUserTastes.append(str(eachEntry))
    for eachEntry in user.allergens:
        currentUserAllergens.append(str(eachEntry))
    currentUserMaxBudget = user.budget_max
    currentUserMinBudget = user.budget_min
    return render_template("displaysearch.html")

@app.route("/usersavedfavorites/", methods=["GET", "POST"])
@login_required
def displaySavedResults():
    user = current_user.email
    return render_template("favorites.html", user=user)



@app.route("/main", methods=["GET", "POST"])
@login_required
def display_main():
    """route is the main route to access website features, directed from user authenticated login"""
    return render_template("homepage.html")

@app.route("/user_profile", methods=["Get", "POST"])
@login_required
def create_profile():
    useremail = current_user.email
    user = Person.query.filter_by(email=useremail).first()
    form = ProfileForm(data={"taste_choices": user.tastes, "allergen_choices": user.allergens, "user_preferred_ingredients": user.preferred_ingredients, "budget_max": user.budget_max,"budget_min": user.budget_min})
    form.taste_choices.query = Taste.query.all()
    form.allergen_choices.query = Allergen.query.all()   
    if form.validate_on_submit():
        user.tastes.clear()
        user.allergens.clear()
        user.tastes.extend(form.taste_choices.data)
        user.allergens.extend(form.allergen_choices.data)
        user.budget_max = form.budget_max.data
        user.budget_min = form.budget_min.data
        user.preferred_ingredients = form.user_preferred_ingredients.data
        database.session.commit()
    return render_template("profile.html", user=useremail, form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    """this route allows a user to create a user and saves it the the database"""
    form = RegisterForm()
    if form.validate_on_submit():
        # generates a hashed password based on created bcrypt object
        bcrypt_hashed_password = bcrypt.generate_password_hash(form.user_password.data)
        new_user = Person(
            email=form.user_email.data, hashed_password=bcrypt_hashed_password
        )
        database.session.add(new_user)
        database.session.commit()
        # redirects to login
        return redirect(url_for("title"))
    # renders path page based on .html form (need to set up)
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """loads login form and querys the database to search for valid user based
    on email,if valid, the password from the form is compared to the hashed
    password of the database and if those match then the user is taken to main.
    Parameters: (none)
    Returns: redirects to either movieinfo or login"""
    form = LoginForm()
    password_error = ""
    if form.validate_on_submit():
        user = Person.query.filter_by(email=form.user_email.data).first()
        if user:
            if bcrypt.check_password_hash(
                user.hashed_password, form.user_password.data
            ):
                login_user(user)
                return redirect(url_for("display_main"))
            else:
                password_error = "The password you have entered does not match"
    return render_template("login.html", error=password_error, form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """logs out user from app and redirects app to login screen
    reauthentication
    Parameters: (none)
    Returns: redirect to login"""
    logout_user()
    return redirect(url_for("login"))


@login_manager.unauthorized_handler
def unauthorized_callback():
    """function to handle attempted unauthorized access, will redirect
    to homepage
    Parameters(none)
    Returns: redirect to beginning route ie '/' route"""
    return redirect(url_for("title"))

if __name__ == "__main__":
    app.run(debug=True)






