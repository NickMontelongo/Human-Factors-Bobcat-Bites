"""Main APP file, instantiates the app, database, encryptor, as
well as contains the definitions for the table models and the
flask forms documentation"""

import random
import os
from hardcodedrestaurants import masterListRestaurants
from flask import Flask, url_for, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

# login information
from flask_login import LoginManager, UserMixin
from flask_login import logout_user, login_user, login_required, current_user


# Algorithm information
from searchalgorithm import (
    food_recommendation,
    stringToArray,
    stringToArrayNoLower,
)

# used to create form objects such as the search bar
from flask_wtf import FlaskForm
from wtforms import (
    Form,
    StringField,
    SelectField,
    EmailField,
    SubmitField,
    PasswordField,
    DecimalField,
    TextAreaField,
    widgets,
)
from wtforms.validators import email, length, InputRequired, ValidationError
from wtforms_alchemy import QuerySelectMultipleField

# used for hashing/encrypting password
from flask_bcrypt import Bcrypt


app = Flask(__name__)

# bcrypt object is utilized in password hashing/encryption
bcrypt = Bcrypt(app)


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


#######################################FLASK FORMS ####################################################


class FoodSearchForm(FlaskForm):
    choices = [("Name", "Name"), ("Flavor", "Flavor"), ("Ingredient", "Ingredient")]
    choice_select = SelectField("Search for Recommendations", choices=choices)
    search = StringField("search", validators=[InputRequired()])
    submit = SubmitField("Search for Result")


class QuerySelectMultipleFieldWithCheckboxes(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class ProfileForm(FlaskForm):
    """Class that will be utilized in profile.html to create the user fields for
    profile creation"""

    taste_choices = QuerySelectMultipleFieldWithCheckboxes(
        "Flavor Choices", get_label="taste_name"
    )
    allergen_choices = QuerySelectMultipleFieldWithCheckboxes(
        "Allergen Choices", get_label="allergen_name"
    )
    budget_min = DecimalField(validators=[InputRequired()], places=2)
    budget_max = DecimalField(validators=[InputRequired()], places=2)
    user_preferred_ingredients = TextAreaField(
        [InputRequired(), length(min=0, max=400)],
        render_kw={
            "Placeholder": "Input ingredients here in ingredient, format (Maximum 400 characters)"
        },
    )
    submit = SubmitField("Create User Profile")

    def validate_budget_max(self, budget_max):
        budget_min = current_user.budget_min
        if budget_max.data <= budget_min:
            raise ValidationError(
                "Maximum budget range must be greater than minimum budget range."
            )
        if budget_max.data <= 0:
            raise ValidationError(
                "Maximum Budget values cannot be less than or equal to zero."
            )

    def validate_budget_min(self, budget_min):
        budget_max = current_user.budget_max
        if budget_max <= budget_min.data:
            raise ValidationError(
                "Minimum budget range must be greater than maximum budget range."
            )
        if budget_min.data < 0:
            raise ValidationError("Minimum budget range cannot be less than zero.")


class DisplayFavoritesForm(FlaskForm):
    remove = SubmitField(label="Remove from Favorites")


class DisplayResultsForm(FlaskForm):
    accept = SubmitField(label="Favorite this food item")
    deny = SubmitField(label="Next food item")
    reset = SubmitField(label="Reset Results")


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

    # login info for person
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(30), unique=True, nullable=False)
    hashed_password = database.Column(
        database.LargeBinary(60), unique=False, nullable=False
    )
    # profile info
    budget_max = database.Column(database.Float)
    budget_min = database.Column(database.Float)
    preferred_ingredients = database.Column(database.String(200))
    tastes = database.relationship(
        "Taste", secondary="person_taste", back_populates="persons"
    )
    allergens = database.relationship(
        "Allergen", secondary="person_allergen", back_populates="persons"
    )

    # users favorite foods
    userfavoritefoods = database.relationship(
        "Userfavoritefood",
        secondary="person_userfavoritefood",
        back_populates="persons",
    )


class Taste(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    taste_name = database.Column(database.String(10), unique=True, nullable=False)
    # link to person
    persons = database.relationship(
        "Person", secondary="person_taste", back_populates="tastes"
    )

    def __repr__(self):
        return self.taste_name


database.Table(
    "person_taste",
    database.Column("person_id", database.ForeignKey("person.id"), primary_key=True),
    database.Column("taste_id", database.ForeignKey("taste.id"), primary_key=True),
)


class Allergen(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    allergen_name = database.Column(database.String(20), unique=True, nullable=False)
    persons = database.relationship(
        "Person", secondary="person_allergen", back_populates="allergens"
    )
    # link to person
    def __repr__(self):
        return self.allergen_name


database.Table(
    "person_allergen",
    database.Column("person_id", database.ForeignKey("person.id"), primary_key=True),
    database.Column(
        "allergen_id", database.ForeignKey("allergen.id"), primary_key=True
    ),
)


class Userfavoritefood(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    parent_restaurant = database.Column(database.String(40), nullable=False)
    food_name = database.Column(database.String(60), nullable=False)
    persons = database.relationship(
        "Person",
        secondary="person_userfavoritefood",
        back_populates="userfavoritefoods",
    )

    def __repr__(self):
        return f"{self.food_name}, {self.parent_restaurant}"


database.Table(
    "person_userfavoritefood",
    database.Column("person_id", database.ForeignKey("person.id"), primary_key=True),
    database.Column(
        "userfavoritefood_id",
        database.ForeignKey("userfavoritefood.id"),
        primary_key=True,
    ),
)


def loadCurrentUserBaseProfile():
    """Function to load up the base information for user profile, allows user to skip profile creation
    Parameters: (none)   Returns: (none)"""
    if current_user.budget_min == None:
        current_user.budget_min = 3.00
    if current_user.budget_max == None:
        current_user.budget_max = 20.00
    if current_user.preferred_ingredients == None:
        current_user.preferred_ingredients = "none"
    database.session.commit()


def loadUserFavoriteFoods(masterListofRestaurants):
    """Function to load every food item into userFavoriteFoods, that starts the process to
    building the relationship between current user and their preferred foods
    Parameters: (List of Restaurants with food objects)   Returns: (none)"""
    databaseUserFavFood = Userfavoritefood.query.all()
    databaseFoodList = []
    databaseRestaurantList = []
    # Loads every pre-existing entry in database to an array (none if there is none)
    for eachEntry in databaseUserFavFood:
        databaseFoodList.append(eachEntry.food_name)
        databaseRestaurantList.append(eachEntry.parent_restaurant)
    # evaluates each food item in master list and if in the database does not attempt to add
    # if not in the database, database model object created using restaurant name/food name and committed
    for eachRestaurant in masterListofRestaurants:
        for eachFoodItem in eachRestaurant.foodList:
            # checks foodname/restaurant combination for passing since common items like fries can exist in multiple restaurants
            if (eachFoodItem.name in databaseFoodList) and (
                eachRestaurant.restaurantName in databaseRestaurantList
            ):
                continue
            else:
                foodItem = Userfavoritefood(
                    parent_restaurant=eachRestaurant.restaurantName,
                    food_name=eachFoodItem.name,
                )
                database.session.add(foodItem)
    database.session.commit()
    return


def loadTastes():
    tasteArray = ["bitter", "salty", "savory", "sour", "spicy", "sweet"]
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
    allergen_array = [
        "beans",
        "beef",
        "cinnamon",
        "chicken",
        "dairy",
        "eggs",
        "fish",
        "gluten",
        "mustard",
        "nuts",
        "pork",
        "potatoes",
        "shellfish",
    ]
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
    # Preload databases with tables
    loadAllergens()
    loadTastes()
    loadUserFavoriteFoods(masterListRestaurants)
    return render_template("title.html")


@app.route(
    "/recommendbyrestaurant/<restaurant>&<restaurant_index>&<list_index>",
    methods=["GET", "POST"],
)
@login_required
def getRecommendationByRestaurant(restaurant, restaurant_index, list_index):
    form = DisplayResultsForm()
    # DEFINITION OF USER AND ASSOCIATED PROFILE VARIABLES
    list_index = int(list_index)
    restaurant_index = int(restaurant_index)
    user = Person.query.filter_by(email=current_user.email).first()
    currentUserFoodPreferences = stringToArray(user.preferred_ingredients)
    currentUserTastes = []
    currentUserAllergens = []
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
    favFoodArray = user.userfavoritefoods
    userFavoriteList = []
    for eachDatabaseEntry in favFoodArray:
        eachDatabaseEntry = str(eachDatabaseEntry)
        tempArray = stringToArrayNoLower(eachDatabaseEntry)
        userFavoriteList.append({"name": tempArray[0], "restaurantName": tempArray[1]})
    currentRestaurantRecommendationList = food_recommendation(
            masterListRestaurants[restaurant_index],
            currentUserMinBudget,
            currentUserMaxBudget,
            currentUserFoodPreferences,
            currentUserAllergens,
            currentUserTastes,
            userFavoriteList,
            restaurant,
        )
    if len(currentRestaurantRecommendationList) == 0:
        restaurant_index = 25
        list_index = 0
        currentRestaurantRecommendationList = food_recommendation(
            masterListRestaurants[restaurant_index],
            currentUserMinBudget,
            currentUserMaxBudget,
            currentUserFoodPreferences,
            currentUserAllergens,
            currentUserTastes,
            userFavoriteList,
        )
    recommendedRestaurantName = masterListRestaurants[restaurant_index].restaurantName
    restaurantLocation = masterListRestaurants[restaurant_index].restaurantLocation
    recommendedFoodScore = currentRestaurantRecommendationList[
        list_index
    ].recommendationScore
    recommendedFoodName = currentRestaurantRecommendationList[list_index].name
    recommendedFoodPrice = currentRestaurantRecommendationList[list_index].price
    recommendedFoodPrice = f"{recommendedFoodPrice:.2f}"
    if form.validate_on_submit():
        if form.accept.data:
            # comment lines 469-475
            # if on the placeholder because of empty restaurant list, nowhere to go until user selects differently
            if restaurant_index == 25 and list_index == 0:
                flash(
                    "Cannot save placeholder. The Restaurant you originally selected has no more items, either unfavorite some items or try another restaurant."
                )
                list_index = 0
                return redirect(
                    url_for(
                        "getRecommendationByRestaurant",
                        restaurant=restaurant,
                        restaurant_index=restaurant_index,
                        list_index=list_index,
                    )
                )
            elif list_index < len(currentRestaurantRecommendationList) - 1:
                list_index = list_index + 1
            else:
                flash(
                    "You cycled through the entire menu, you are now at the beginning of the list.")
                list_index = 0
            foodItem = Userfavoritefood.query.filter_by(
                food_name=recommendedFoodName,
                parent_restaurant=recommendedRestaurantName,
            ).first()
            user.userfavoritefoods.append(foodItem)
            database.session.commit()
            flash(f"The food item {foodItem.food_name} was added to your favorites")
            return redirect(
                url_for(
                    "getRecommendationByRestaurant",
                    restaurant=restaurant,
                    restaurant_index=restaurant_index,
                    list_index=list_index,
                )
            )
        if form.deny.data:
            # comment lines 497-503
            # if on the placeholder because of empty restaurant list, nowhere to go until user selects differently
            if restaurant_index == 25 and list_index == 0:
                flash(
                    "The Restaurant has no more items, either unfavorite some items or try restaurant."
                )
                list_index = 0
                return redirect(
                    url_for(
                        "getRecommendationByRestaurant",
                        restaurant=restaurant,
                        restaurant_index=restaurant_index,
                        list_index=list_index,
                    )
                )
            elif list_index < len(currentRestaurantRecommendationList) - 1:
                list_index = list_index + 1
            else:
                flash(
                    "You cycled through the entire menu, you are now at the beginning of the list."
                )
                list_index = 0
            return redirect(
                url_for(
                    "getRecommendationByRestaurant",
                    restaurant=restaurant,
                    restaurant_index=restaurant_index,
                    list_index=list_index,
                )
            )
        if form.reset.data:
            return redirect(
                url_for(
                    "getRecommendationByRestaurant",
                    restaurant=restaurant,
                    restaurant_index=restaurant_index,
                    list_index=0,
                )
            )
    return render_template(
        "displayrec.html",
        restaurantLoc=restaurantLocation,
        restaurantName=recommendedRestaurantName,
        foodScore=recommendedFoodScore,
        foodPrice=recommendedFoodPrice,
        foodName=recommendedFoodName,
        form=form,
    )


@app.route("/recommendrand/<restaurantIndex>&<foodIndex>", methods=["GET", "POST"])
@login_required
def getRecommendationByRand(restaurantIndex, foodIndex):
    form = DisplayResultsForm()
    # DEFINITION OF USER AND ASSOCIATED PROFILE VARIABLES
    foodIndex = int(foodIndex)
    restaurantIndex = int(restaurantIndex)
    user = Person.query.filter_by(email=current_user.email).first()
    currentUserFoodPreferences = stringToArray(user.preferred_ingredients)
    currentUserTastes = []
    currentUserAllergens = []
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
    favFoodArray = user.userfavoritefoods
    userFavoriteList = []
    for eachDatabaseEntry in favFoodArray:
        eachDatabaseEntry = str(eachDatabaseEntry)
        tempArray = stringToArrayNoLower(eachDatabaseEntry)
        userFavoriteList.append({"name": tempArray[0], "restaurantName": tempArray[1]})
    for eachEntry in masterListRestaurants:
        food_recommendation(
            eachEntry,
            currentUserMinBudget,
            currentUserMaxBudget,
            currentUserFoodPreferences,
            currentUserAllergens,
            currentUserTastes,
            userFavoriteList,
        )
        eachEntry.foodList.sort(key=lambda x: x.recommendationScore, reverse=True)
    recommendedRestaurantName = masterListRestaurants[restaurantIndex].restaurantName
    restaurantLocation = masterListRestaurants[restaurantIndex].restaurantLocation
    recommendedFoodScore = (
        masterListRestaurants[restaurantIndex].foodList[foodIndex].recommendationScore
    )
    recommendedFoodName = (
        masterListRestaurants[restaurantIndex].foodList[foodIndex].name
    )
    recommendedFoodPrice = (
        masterListRestaurants[restaurantIndex].foodList[foodIndex].price
    )
    recommendedFoodPrice = f"{recommendedFoodPrice:.2f}"
    if form.validate_on_submit():
        if form.accept.data:
            if restaurantIndex == 25:
                flash(f"Placeholder food item cannot be added.")
            else:
                restaurantIndex = random.randint(0, (len(masterListRestaurants) - 1))
                foodIndex = random.randint(
                    0, (len(masterListRestaurants[restaurantIndex].foodList) - 1)
                )
                while (
                    masterListRestaurants[restaurantIndex]
                    .foodList[foodIndex]
                    .recommendationScore
                    < 1
                ):
                    restaurantIndex = random.randint(
                        0, (len(masterListRestaurants) - 2)
                    )
                    foodIndex = random.randint(
                        0, (len(masterListRestaurants[restaurantIndex].foodList) - 1)
                    )
                foodItem = Userfavoritefood.query.filter_by(
                    food_name=recommendedFoodName,
                    parent_restaurant=recommendedRestaurantName,
                ).first()
                user.userfavoritefoods.append(foodItem)
                database.session.commit()
                flash(f"The food item {foodItem.food_name} was added to your favorites")
                return redirect(
                    url_for(
                        "getRecommendationByRand",
                        foodIndex=foodIndex,
                        restaurantIndex=restaurantIndex,
                    )
                )
        if form.deny.data:
            restaurantIndex = random.randint(0, (len(masterListRestaurants) - 2))
            foodIndex = random.randint(
                0, (len(masterListRestaurants[restaurantIndex].foodList) - 1)
            )
            while (
                masterListRestaurants[restaurantIndex]
                .foodList[foodIndex]
                .recommendationScore
                < 1
            ):
                restaurantIndex = random.randint(0, (len(masterListRestaurants) - 2))
                foodIndex = random.randint(
                    0, (len(masterListRestaurants[restaurantIndex].foodList) - 1)
                )
            return redirect(
                url_for(
                    "getRecommendationByRand",
                    foodIndex=foodIndex,
                    restaurantIndex=restaurantIndex,
                )
            )
    return render_template(
        "displayrand.html",
        restaurantLoc=restaurantLocation,
        restaurantName=recommendedRestaurantName,
        foodScore=recommendedFoodScore,
        foodPrice=recommendedFoodPrice,
        foodName=recommendedFoodName,
        form=form,
    )


@app.route("/recommendbysearch/", methods=["GET", "POST"])
@login_required
def getRecommendationBySearch():
    form = FoodSearchForm()
    if form.validate_on_submit():
        searchType = form.choice_select.data
        searchString = form.search.data
        return redirect(
            url_for("searchResults", searchString=searchString, searchType=searchType)
        )
    return render_template("displaysearch.html", form=form)


@app.route(
    "/recommendbysearch/results?searchString=<searchString>&searchType=<searchType>",
    methods=["GET", "POST"],
)
@login_required
def searchResults(searchType, searchString):
    results = []
    currentUserFoodPreferences = stringToArray(current_user.preferred_ingredients)
    currentUserTastes = []
    currentUserAllergens = []
    for eachEntry in current_user.tastes:
        if str(eachEntry) == "none":
            currentUserTastes.append("none")
            break
        currentUserTastes.append(str(eachEntry))
    for eachEntry in current_user.allergens:
        if str(eachEntry) == "none":
            currentUserAllergens.append("none")
            break
        currentUserAllergens.append(str(eachEntry))
    currentUserMaxBudget = current_user.budget_max
    currentUserMinBudget = current_user.budget_min
    favFoodArray = current_user.userfavoritefoods
    userFavoriteList = []
    for eachDatabaseEntry in favFoodArray:
        eachDatabaseEntry = str(eachDatabaseEntry)
        tempArray = stringToArrayNoLower(eachDatabaseEntry)
        userFavoriteList.append({"name": tempArray[0], "restaurantName": tempArray[1]})
    for eachRestaurant in masterListRestaurants:
        food_recommendation(
            eachRestaurant,
            currentUserMinBudget,
            currentUserMaxBudget,
            currentUserFoodPreferences,
            currentUserAllergens,
            currentUserTastes,
            userFavoriteList,
        )
    if searchType == "Name":
        searchString = searchString.lower()
        for eachEntry in masterListRestaurants:
            for eachFoodItem in eachEntry.foodList:
                if searchString in eachFoodItem.name.lower():
                    results.append(
                        {
                            "name": eachFoodItem.name,
                            "price": eachFoodItem.price,
                            "score": eachFoodItem.recommendationScore,
                            "rname": eachEntry.restaurantName,
                            "rlocation": eachEntry.restaurantLocation,
                        }
                    )
                    break
    elif searchType == "Ingredient":
        searchString = searchString.lower()
        for eachEntry in masterListRestaurants:
            for eachFoodItem in eachEntry.foodList:
                for eachIngredient in eachFoodItem.ingredients:
                    if searchString in eachIngredient.lower():
                        results.append(
                            {
                                "name": eachFoodItem.name,
                                "price": eachFoodItem.price,
                                "score": eachFoodItem.recommendationScore,
                                "rname": eachEntry.restaurantName,
                                "rlocation": eachEntry.restaurantLocation,
                            }
                        )
                        break
    else:  # searchType =="Flavor"
        searchString = searchString.lower()
        for eachEntry in masterListRestaurants:
            for eachFoodItem in eachEntry.foodList:
                for eachFlavor in eachFoodItem.flavorProfile:
                    if searchString in eachFlavor.lower():
                        results.append(
                            {
                                "name": eachFoodItem.name,
                                "price": eachFoodItem.price,
                                "score": eachFoodItem.recommendationScore,
                                "rname": eachEntry.restaurantName,
                                "rlocation": eachEntry.restaurantLocation,
                            }
                        )
                        break
        # display the results here
    return render_template(
        "displayresults.html",
        results=results,
        len=len(results),
        searchString=searchString,
    )


@app.route(
    "/search/foodresults?<foodName>&<restaurantName>&<restaurantLocation>&<foodPrice>&<foodScore>",
    methods=["GET", "POST"],
)
@login_required
def displayFoodItem(foodName, restaurantName, restaurantLocation, foodPrice, foodScore):
    form = DisplayResultsForm()
    user = Person.query.filter_by(email=current_user.email).first()
    foodPrice = float(foodPrice)
    foodPrice = f"{foodPrice:.2f}"
    if form.validate_on_submit():
        if form.accept.data:
            foodItem = Userfavoritefood.query.filter_by(
                food_name=foodName, parent_restaurant=restaurantName
            ).first()
            user.userfavoritefoods.append(foodItem)
            database.session.commit()
            flash(f"The food item {foodItem.food_name} was added to your favorites")
            return redirect(url_for("getRecommendationBySearch"))
        if form.deny.data:
            return redirect(url_for("getRecommendationBySearch"))
    return render_template(
        "displayfooditem.html",
        foodName=foodName,
        restaurantName=restaurantName,
        foodPrice=foodPrice,
        foodScore=foodScore,
        restaurantLocation=restaurantLocation,
        form=form,
    )


@app.route("/usersavedfavorites/", methods=["GET", "POST"])
@login_required
def displaySavedResults():
    userEmail = current_user.email
    results = []
    userPrefIngred = stringToArray(current_user.preferred_ingredients)
    userTastes = []
    userAllergens = []
    for eachEntry in current_user.tastes:
        if str(eachEntry) == "none":
            userTastes.append("none")
            break
        userTastes.append(str(eachEntry))
    for eachEntry in current_user.allergens:
        if str(eachEntry) == "none":
            userAllergens.append("none")
            break
        userAllergens.append(str(eachEntry))
    maxBudget = current_user.budget_max
    minBudget = current_user.budget_min
    favFoodArray = current_user.userfavoritefoods
    userFavoriteList = []
    for eachDatabaseEntry in favFoodArray:
        eachDatabaseEntry = str(eachDatabaseEntry)
        tempArray = stringToArrayNoLower(eachDatabaseEntry)
        userFavoriteList.append({"name": tempArray[0], "restaurantName": tempArray[1]})
    for eachRestaurant in masterListRestaurants:
        food_recommendation(
            eachRestaurant,
            minBudget,
            maxBudget,
            userPrefIngred,
            userTastes,
            userAllergens,
        )
    for eachFavoritedItem in userFavoriteList:
        for eachRestaurant in masterListRestaurants:
            if eachFavoritedItem.get("restaurantName") == eachRestaurant.restaurantName:
                for eachFoodItem in eachRestaurant.foodList:
                    if eachFavoritedItem.get("name") == eachFoodItem.name:
                        results.append(
                            {
                                "name": eachFoodItem.name,
                                "price": eachFoodItem.price,
                                "score": eachFoodItem.recommendationScore,
                                "rname": eachRestaurant.restaurantName,
                                "rlocation": eachRestaurant.restaurantLocation,
                            }
                        )
            else:
                continue
    return render_template(
        "favorites.html", results=results, len=len(results), userEmail=userEmail
    )


@app.route(
    "/favorites/foodresults?<foodName>&<restaurantName>&<restaurantLocation>&<foodPrice>&<foodScore>",
    methods=["GET", "POST"],
)
@login_required
def displayFavorites(
    foodName, restaurantName, restaurantLocation, foodPrice, foodScore
):
    form = DisplayFavoritesForm()
    user = current_user
    foodPrice = float(foodPrice)
    foodPrice = f"{foodPrice:.2f}"
    if form.validate_on_submit():
        foodItem = Userfavoritefood.query.filter_by(
            food_name=foodName, parent_restaurant=restaurantName
        ).first()
        user.userfavoritefoods.remove(foodItem)
        database.session.commit()
        flash(f"{foodItem.food_name} was removed from your favorites")
        return redirect(url_for("displaySavedResults"))
    return render_template(
        "displayfavoriteitem.html",
        foodName=foodName,
        restaurantName=restaurantName,
        foodPrice=foodPrice,
        foodScore=foodScore,
        restaurantLocation=restaurantLocation,
        form=form,
    )


@app.route("/main", methods=["GET", "POST"])
@login_required
def display_main():
    """route is the main route to access website features, directed from user authenticated login"""
    loadCurrentUserBaseProfile()
    return render_template("homepage.html")


@app.route("/user_profile", methods=["Get", "POST"])
@login_required
def create_profile():
    useremail = current_user.email
    user = Person.query.filter_by(email=useremail).first()
    form = ProfileForm(
        data={
            "taste_choices": user.tastes,
            "allergen_choices": user.allergens,
            "user_preferred_ingredients": user.preferred_ingredients,
            "budget_max": user.budget_max,
            "budget_min": user.budget_min,
        }
    )
    form.taste_choices.query = Taste.query.all()
    form.allergen_choices.query = Allergen.query.all()
    messageToUser = ""
    if form.validate_on_submit():
        messageToUser = "Your profile was successfully updated"
        user.tastes.clear()
        user.allergens.clear()
        user.tastes.extend(form.taste_choices.data)
        user.allergens.extend(form.allergen_choices.data)
        user.budget_max = form.budget_max.data
        user.budget_min = form.budget_min.data
        user.preferred_ingredients = form.user_preferred_ingredients.data
        database.session.commit()
    return render_template(
        "profile.html", user=useremail, messageToUser=messageToUser, form=form
    )


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


@app.route("/about", methods=["GET", "POST"])
@login_required
def about():
    return render_template("about.html")


@login_manager.unauthorized_handler
def unauthorized_callback():
    """function to handle attempted unauthorized access, will redirect
    to homepage
    Parameters(none)
    Returns: redirect to beginning route ie '/' route"""
    return redirect(url_for("title"))


if __name__ == "__main__":
    app.run(debug=True)
