#storage of the actual restaurant
class Restaurant:
    def __init__ (self, restaurantName, foodList, restaurantLocation):
        self.restaurantName = restaurantName
        self.foodList = foodList
        self.restaurantLocation = restaurantLocation

#storage of the food item information
class Food:
    def __init__ (self, name, price, ingredients, allergens, flavorProfile):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.allergens = allergens
        self.flavorProfile = flavorProfile
        self.recommendationScore = 0.0

#will hold all restaurants
masterListRestaurants = []


def setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, restaurantName, restaurantLocation,
                         foodList, showResults=False):
    """Use this function to create the restaurant object will lowercase all food names,
    uppercase the restaurant location and restaurant name. And finally create the object and 
    display it"""
    for eachName in foodNames:
        eachName = eachName.lower()
    for eachFoodIngredientList in foodIngredients:
        for eachIngredient in eachFoodIngredientList:
            eachIngredient = eachIngredient.lower()
    for eachAllergenList in foodAllergens:
        for eachAllergen in eachAllergenList:
            eachAllergen = eachAllergen.lower()
    for eachFlavorList in flavorProfile:
        for eachFlavor in eachFlavorList:
            eachFlavor = eachFlavor.lower()
    restaurantName = restaurantName.upper()
    restaurantLocation = restaurantLocation.upper()
    for i in range(len(foodNames)):
        newFoodItem = Food(foodNames[i], foodPrices[i], foodIngredients[i], foodAllergens[i], flavorProfile[i])
        if showResults:
            print(f' Name: {newFoodItem.name}')
            print(f' Price: {newFoodItem.price}')
            print(f' Ingredients: {newFoodItem.ingredients}')
            print(f' Allergens: {newFoodItem.allergens}')
            print(f' Flavors: {newFoodItem.flavorProfile}')
        foodList.append(newFoodItem)
    if showResults:    
        print(f' This is restaurantName: {restaurantName}')
        print(f' This is restaurant Location: {restaurantLocation}')
    return (Restaurant(restaurantName, foodList, restaurantLocation))

# Rules
# restaurant list names must equal query string on main page
# restaurant ingredients and info all lowercase
# acceptable allergens: dairy, eggs, chicken, beef, pork, fish, shellfish, tree nuts, peanuts, gluten, beans, mustard, cinnamin, (possibly other spices NOT HERBS, NOT SALT, NOT PEPPER< NOT POTATOES)
# tastes: sweet, salty, sour, spicy, bitter, and savory
#list objects for absurdbird creation

################### 3 test cases for High Fidelity Prototype ##########################################
absurdbird = []
foodNames = ["3 chicken tender basket", "4 chicken tender basket", "5 chicken tender basket", "tender slider", "snack box", "fried oreo", "mac and cheese", "fries" ]
foodPrices = [5.99, 6.99, 7.99, 2.99, 4.99, 2.99, 2.19, 2.99]
foodIngredients = [["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"], ["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"],
["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"], ["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"],
["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"], ["oreos", "pancake mix", "oil"], ["cheese", "cheese sauce", "pasta"], ["potatoes"]]
foodAllergens = ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chocolate", "sugar"], ["dairy", "gluten"], ["flour", "potatoes"]
flavorProfile = [["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["sweet"], ["savory"], ["salty"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Absurd Bird", "The Den Food Company",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


ajsbbq=[]
foodNames= ["Nachos Plain", "Nachos Chopped BBQ chicken", "Nachos Chopped brisket", "Nachos Beyond beef", "Jumbo Sandwiches", 
            "Jumbo Sandwiches with side", "1 meat BBQ Plate", "2 meat BBQ Plate", "3 meat BBQ Plate", "Jumbo sausage wrap", 
            "Brisket Mac n' Cheese", "Beyond beef Mac vegetarian", "Cheesecake Bites(3)"]
foodPrices= [6.00, 8.00, 9.00, 9.00, 8.00, 10.00, 9.00, 11.00, 14.00, 5.00, 8.00, 9.00, 4.00]
foodIngredients= [["cheese", "corn chips"],["cheese", "corn chips", "BBQ sause", "chicken"],["cheese", "corn chips", "brisket"],["cheese", "corn chips", "vegetarian beef"],
                  ["bread", "bbq sauce", "chicken", "brisket", "sausage", "vegetarian beef"],["bread", "BBQ sauce", "chicken", "brisket", "sausage", "vegetarian breef", "potato", "mayo", "cabage", "cheese", "pasta", "chips"],
                  ["brisket", "sausage", "chicken", "BBQ sauce"], ["bread", "BBQ sauce", "chicken", "brisket", "sausage", "vegetarian breef", "potato", "mayo", "cabage", "cheese", "pasta", "chips"],
                  ["brisket", "sausage", "chicken", "BBQ sauce"],["bread", "BBQ sauce", "chicken", "brisket", "sausage", "vegetarian breef", "potato", "mayo", "cabage", "cheese", "pasta", "chips"],
                  ["brisket", "sausage", "chicken", "BBQ sauce"],["sausage", "sauce", "tortilla"], ["cheese", "brisket", "pasta"], ["vegetarian beef", "cheese", "pasta"],["cheese", "egg", "sauce"]]
foodAllergens = [["dairy", "gluten"],["dairy", "gluten", "chicken"],["dairy", "gluten", "beef"],["dairy", "gluten"], ["gluten", "chicken", "beef", "pork"], ["gluten", "chicken", "beef", "pork"],
                 ["brisket", "sausage", "chicken"],["brisket", "sausage", "chicken"],["brisket", "sausage", "chicken"],["gluten", "pork"], ["cheese", "brisket", "pasta"], ["gluten", "dairy", "pasta"],
                   ["dairy", "egg", "gluten"]]
flavorProfile = [["cheesey", "savory"], ["cheesey", "sweet", "savory"], ["cheesey", "meaty", "dry"], ["cheesey", "sweet"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], 
                 ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["sweet", "savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "AJs BBQ", "In front of Student Writing Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


burger512 = []
foodNames =["korean flame", "blue mushroom", "guadalupe burger", "hays co burger", "the classic", "fiesta fries", "firebird fries", "disco fries", "fries", "chicken strips"]
foodPrices=[7.99, 7.99, 7.99, 7.99, 6.99, 6.19, 5.69, 4.69, 2.19, 5.99]
foodIngredients =[["bread", "fried onions", "pico de gallo", "cheese", "kimchi", "beef", "gochujang mayo"], ["blue cheese", "bread", "beef", "mushrooms", "bacon"], ["cheese", "guacamole", "pico de gallo", "tortilla strips", "bread", "black bean", "beef"], 
                  ["cheese", "fried onions", "barbeque sauce", "bacon", "bread", "beef", "gochujang mayo"], ["black beans", "cheese", "guacamole", "potatoes", "flour", "pico de gallo"],["pickles", "tomatoes", "beef", "bread", "lettuce", "cheese"], ["teriyaki", "chicken", "flour", "cilantro", "kimchi", "gochujang mayo", "potatoes"],
                  ["cheese", "bacon", "potatoes", "flour", "fried onions"], ["potatoes", "flour", "seasoning"], ["chicken", "flour", "seasoning"]]
foodAllergens = [["gluten", "beef", "dairy", "eggs"], ["gluten", "beef", "dairy", "pork"], ["dairy", "gluten", "beef", "beans"], ["dairy", "gluten", "pork", "beef", "eggs"], ["dairy", "beef", "gluten" ],["beans", "dairy"], ["chicken", "eggs"], ["dairy", "pork"], ["none"], ["gluten", "chicken"]]
flavorProfile = [["savory", "salty", "spicy"],["savory", "salty"], ["savory", "salty"], ["savory", "sweet", "salty"], ["savory", "salty"], ["salty", "savory"], ["salty"], ["salty"], ["salty"], ["salty", "savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Burger 512", "LBJ Student Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


teaco=[]
foodNames= ["vietnamese sandwich", "spring rolls", "egg rolls"]
foodPrices= [4.95, 4.49, 3.25]
foodIngredients= [["bread", "pork", "mayo", "cilantro", "vinegar", "onion", "carrot", "cilantro", "chilies"],["rice wrapper", "rice noodle", "carrot", "cucumber", "shrimp", "mint", "basil", "cilantro"], ["pork", "garlic", "ginger", "coleslaw", "onion", "soy sauce", "egg roll wrapper", "egg", "sesame oil"]]
foodAllergens = [["pork", "eggs", "gluten", "chilies"],["gluten", "shrimp"],["pork", "egg", "garlic"]]
flavorProfile = [["savory", "spicy"], ["savory"], ["savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Tea Co", "The Den Food Company",
                         foodList=[])
masterListRestaurants.append(restaurantObject)




pizzahut=[]
foodNames =["Personal Pan Pizza - Cheese", "Personal Pan Pizza - Pepperoni", "Personal Pan Pizza - Italian Sausage", "Personal Pan Pizza - Supreme", "Meaty Marinara Pasta", "Chicken Alfredo Pasta", "Breadsticks", "6 Baked Wings"]
foodPrices =[4.79, 4.79, 4.79, 4.79, 5.49, 5.49, 3.19, 5.39]
foodIngredients=[["cheese", "bread", "tomato sauce"],["cheese", "bread", "tomato sauce", "pepperoni"],["cheese", "bread", "tomato sauce", "sausage"],["cheese", "bread", "tomato sauce", "mushroom"],["meat", "tomato sause"],["Chicken", "pasta", "sauce"],["bread", "tomato sauce"],["bread", "wings", "chicken"]]
foodAllergens =[["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"]]
flavorProfile =[["savory", "cheesey"],["savory", "cheesey", "meaty"],["savory", "cheesey", "meaty"],["savory", "cheesey"],["savory", "meaty", "saucy"],["savory", "creamy"],["savory", "salty"],["savory", "saucy"]]

thesaltymenu=[]
foodNames= ["Horchata", "Traditional Glazed", "Churro + Dulce de leche star", "Texas Chocolate sheet cake", "Boston Cream", "Ube Pina Colada(V)"]
foodPrices= [4.50, 3.50, 4.25, 4.25, 4.65, 4.75]
foodIngredients= [["brioche", "horchata mixture", "chocolate, cinnamon"],["dough", "vanilla bean glaze"],["broche", "cinnamon", "sugar", "coffee", "whipped cream"], ["chocolate", "dough", "sugar", "glaze"], ["brioche", "vinilla custard", "ganache glaze"], ["vegan brioche", "pineapple jam", "coconut milk glaze", "coconut streusel"]]
foodAllergens = [["gluten", ""],["gluten", ""],["gluten"],["gluten"], ["gluten"], ["gluten"]]
flavorProfile = [["sweet"], ["sweet"], ["sweet", "bitter"], ["sweet", "savory"], ["sweet"], ["sweet"]]

pomhoney=[]
foodNames= ["Salad", "Pita Wrap", "Grain Bowl"]
foodPrices= [7.99, 7.99, 7.99]
foodIngredients= [["Falafel", "Chicken", "Lamb", "Beef", "Hummus"], ["Falafel", "Chicken", "Lamb", "Beef", "Hummus"], ["Falafel", "Chicken", "Lamb", "Beef", "Hummus"]]
foodAllergens = [["dairy", "eggs", "gluten", "garlic"], ["dairy", "eggs", "gluten", "garlic"], ["dairy", "eggs", "gluten", "garlic"]]
flavorProfile = [["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"]]

ourfavorite=[]
foodNames= [""]
foodPrices= [6.99]
foodIngredients= [[""]]
foodAllergens = [[""]]
flavorProfile = [[""]]


ShakeSmart=[]
foodNames= ["Rawcai bowl", "Raw-PB Bowl", "The Buzz Bowl", "Original Acai Bowl", "PB&A bowl", "Dragon Bowl", "Peanut Butter toast",
            "Almond Butter Toast", "Avocado Toast", "Turks and Matoes wrap", "Rubi's Tuna Salad", "Veggie Delight"]
foodPrices= [7.50, 7.50, 7.50, 7.50, 7.50, 7.50, 4.75, 5.25, 5.75, 8.45, 8.45, 7.95]
foodIngredients= [["granola", "banana", "chocolate", "coconut"], ["granola", "banana", "peanut butter"], ["granola", "pineapple", "coconut"],
                  ["strawberry", "apple", "granola"], ["peanut butter", "banana", "granola"], ["pineapple", "granola", "chia"],
                  ["peanut butter", "bread"], ["almond butter", "bread", "banana"], ["avocado", "bread"],["hummus", "tomato"],
                  ["tuna", "carrots", "spinach"], ["tomato", "hummus"]]
foodAllergens = [[], ["peanut butter"], [], [], ["peanut butter"], [], ["peanut butter"], ["nuts"], [], [], [], []]
flavorProfile = [["fresh", "healthy", "crunchy"], ["fresh", "healthy", "crunchy"], ["fresh", "healthy", "crunchy"],
                 ["fresh", "healthy", "crunchy"], ["fresh", "healthy", "crunchy"], ["fresh", "healthy", "crunchy"],
                 ["Sweet", "bready"], ["Sweet", "healthy"], ["Savory", "healthy"], ["fresh", "healthy"],
                 ["fresh", "healthy"], ["fresh", "healthy"]]

TuTaco=[]
foodNames= ["Migas Taco", "Bean & Cheese Taco", "Bacon, Egg, & Cheese Taco", "Chilaquiles Taco", "Chorizo & Egg Taco", "Egg Taco",
            "Chicken Quesadilla", "Cheese Quesadilla", "Al Pastor Quesadilla", "Beef Quesadilla", "Steak Quesadilla", "Beyond Meat Quesadilla",
            "Al Pastor Taco Salad", "Beef Taco Salad", "Beyond Meat Taco Salad", "Chicken Taco Salad", "Steak Taco Salad",
            "Chicken Burrito", "Steak Burrito", "Beyond Meat Burrito", "Beef Burrito", "Al Pastor Burrito", "Chicken Taco",
            "Steak Taco", "Beyond Meat Taco", "Beef Taco", "Al Pastor Taco", "Nachos", "Chips and Salsa",
            "Chips and Guacamole"]
foodPrices= [2.59, 2.39, 2.59, 2.59, 2.59, 1.99, 7.49, 5.99, 7.49, 6.99, 8.49, 7.49, 7.49, 6.99, 7.49, 7.49, 8.49, 7.49,
             8.99, 7.49, 6.99, 7.49, 2.99, 3.09, 3.09, 2.39, 3.09, 5.99, 1.99, 3.19]
foodIngredients= [["egg", "cheese", "bread"], ["bean", "cheese"], ["bacon", "egg", "cheese"],["egg", "cheese", "bread"],
                  ["egg", "cheese", "bread", "chorizo"], ["egg", "bread"], ["chicken", "bread", "cheese"],
                  ["bread", "cheese"], ["pork", "bread", "cheese"], ["beef", "bread", "cheese"], ["beef", "bread", "cheese"],
                  ["bread", "cheese"], ["pork", "bread", "cheese"], ["beef", "bread", "cheese"], ["bread", "cheese"],
                  ["Chicken", "bread", "cheese"], ["beef", "bread", "cheese"], ["chicken", "bread", "cheese"], ["steak", "bread", "cheese"],
                  ["bread", "cheese"], ["beef", "bread", "cheese"], ["pork", "bread", "cheese"], ["chicken", "bread", "cheese"],
                  ["steak", "bread", "cheese"], ["bread", "cheese"], ["beef", "bread", "cheese"], ["pork", "bread", "cheese"],
                  ["chips", "cheese"], ["chips", "salsa"], ["chips", "Avocado"]]
foodAllergens = [["eggs", "gluten", "dairy"], ["gluten", "dairy"], ["eggs"], ["eggs"], ["eggs"], ["eggs"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten"], ["gluten"], ["gluten"]]
flavorProfile = [["egg", "cheese", "savory"], ["savory"], ["savory", "salty"], ["savory"], ["egg", "cheese", "bread"],
                 ["savory"], ["chicken", "savory"], ["savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"],
                 ["savory"], ["savory", "meaty"], ["savory", "meaty"], ["savory"], ["savory", "meaty"], ["savory", "meaty"],
                 ["savory", "meaty"], ["savory", "meaty"], ["savory", "meaty"],["savory","meaty"], ["savory", "meaty"],
                 ["savory", "meaty"], ["savory", "meaty"], ["savory","meaty"],["savory"], ["savory", "meaty"], ["savory", "cheesy"],
                 ["savory", "salty"],["savory", "healthy"]]

WoodsStPizza=[]
foodNames= ["Cheese Pizza Slice", "Pepperoni Pizza Slice", "Alfredo and Veggie Pizza Slice", "Bacon and Herbs Pizza Slice",
            "Pepperoni Calzone", "Weekly Pasta Bowl", "Garlic Knots", "Cookie"]
foodPrices= [3.29, 3.29, 4.19, 4.19, 4.49, 5.49, 1.09, 1.99]
foodIngredients= [["cheese", "bread", "tomato sauce"], ["cheese", "bread", "tomato sauce", "pepperoni"], ["cheese", "bread", "Alfredo sauce", "Veggies"],
                  ["cheese", "bread", "tomato sauce", "Bacon"], ["cheese", "bread", "tomato sauce", "pepperoni"], ["pasta", "sauce"],
                  ["garlic"], ["sugar", "chocolate"]]
foodAllergens = [["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"]]
flavorProfile = [["savory", "cheesy"], ["savory", "cheesy", "meaty"], ["savory", "cheesy", "meaty"], ["savory", "cheesy", "saucy"],
                 ["savory", "meaty", "saucy"], ["savory", "cheesy", "meaty"],["savory", "salty"],["sweet", "sugary"]]

RevolutionNoodle=[]
foodNames= ["Shio Ramen", "Veggie Ramen", "Spicy Miso Ramen", "Curry Ramen", "Smoked Brisket Ramen", "Tsukimi Ramen", "Flying Pig Sandwich",
            "Chicken Run Sandwich", "Kickin Tofu Sandwich", "Chicken Dumplings", "Pork Dumplings", "Veggie Dumplings", "Vietnamese Sandwich",
            "Spring Rolls", "Egg Rolls"]
foodPrices= [7.99, 7.99, 7.99, 7.99, 7.99, 7.99, 5.99, 5.99, 3.99, 7.29, 7.29, 7.29, 4.95, 4.49, 3.25]
foodIngredients= [["Chicken", "Noodle", "Broth", "egg"], ["Chicken", "Noodle", "Broth", "egg"], ["Curry", "Noodle", "Broth", "egg"],
                  ["Brisket", "Noodle", "Broth", "egg"], ["Pork", "Noodle", "Broth", "egg"], ["Por", "Noodle", "Broth", "egg"],
                  ["pork", "bread"], ["Chicken", "bread"], ["Tofu", "bread"], ["Chicken", "bread"], ["Pork", "bread"],
                  ["Veggies", "bread"], ["Bread", "Beef"], ["Veggies"], ["Veggies", "egg", "pork"]]
foodAllergens = [["gluten", "dairy", "egg"], ["gluten", "dairy", "egg"], ["gluten", "dairy", "egg"], ["gluten", "dairy", "egg"],
                 ["gluten", "dairy", "egg"], ["gluten", "dairy", "egg"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"]]
flavorProfile = [["savory", "salty", "meaty"], ["savory", "salty", "meaty"], ["savory", "salty", "meaty"],
                 ["savory", "salty", "meaty"], ["savory", "salty", "meaty"], ["savory", "salty", "meaty"],
                 ["savory", "salty", "meaty"], ["savory", "salty", "meaty"], ["savory", "salty"], ["savory", "salty", "meaty"],
                 ["savory", "salty", "meaty"], ["savory", "Fresh"], ["savory", "salty", "meaty"], ["savory", "salty"],
                 ["savory", "salty", "meaty"]]

chickfila=[]
foodNames= ["Chicken Sandwich", "Deluxe Sandwich w/ cheese", "Spicy Chicken Sandwich", "Spicy Deluxe Sandwich w/ cheese", "Grilled Chicken Sandwich", "Grilled Chicken Club w/ cheese", 
            "5 ct Chicken Nuggets", "8 ct Chicken Nuggets", "12 ct Chicken Nuggets", "30 ct Chicken Nuggets", "5 ct Grilled Nuggets", "8 ct Grilled Nuggets", "12 ct Grilled Nuggets", 
            "2 ct Chick-n-Strips", "3 ct Chick-n-Strips", "4 ct Chick-n-Strips", "Cool Wrap", "Cobb Salad", "Spicy Southwest Salad", "Grilled Market Salad", "Chicken Biscuit", 
            "Spicy Chicken Biscuit", "4 ct Chick-n-Minis", "Egg White Grill", "Hash Brown Scramble Burrito w/ Nuggets", "Hash Brown Scramble Bowl w/ Nuggets", "Chicken, Egg & Cheese Biscuit", 
            "Bacon, Egg & Cheese Biscuit", "Sausage, Egg & Cheese Biscuit", "Chicken, Egg & Cheese Muffin", "Bacon, Egg & Cheese Muffin", "Sausage, Egg & Cheese Muffin"]
foodPrices= [6.49, 7.39, 6.89, 7.79, 11.05, 4.50, 6.59, 9.05, 22.55, 4.79, 7.65, 10.89, 4.75, 6.99, 8.79, 10.49, 12.35, 12.59, 12.59, 8.95, 9.29, 10.25, 10.85, 10.79, 10.79, 10.39,
             9.49, 9.49, 10.49, 9.75, 9.75]
foodIngredients= [["chicken", "bread", "breading", "pickles"],["chicken", "bread", "breading", "tomato", "lettuce", "pickles", "cheese"],["chicken", "spice", "bread", "breading", "pickles"],
                  ["chicken", "bread", "breading", "spice", "tomato", "lettuce", "pickles", "cheese"],["chicken", "spice", "bread", "breading", "pickles"], ["bread", "chicken", "tomato", "lettuce", "Honey Roasted BBQ sauce"], 
                  ["chicken", "bread", "tomato", "lettuce", "bacon", "Honey Roasted BBQ Sauce"], ["chicken", "breading"], ["chicken", "breading"], 
                  ["chicken", "breading"], ["chicken", "breading"], ["chicken"], ["chicken"], ["chicken"], ["chicken", "breading"], ["chicken", "breading"], 
                  ["chicken", "breading"], ["chicken", "cheese", "lettuce", "tortilla", "Avocado lime ranch Dressing"], ["chicken", "breading", "mixed greens", "corn", "cheese", "bacon", "egg", "tomato", "Avocado lime ranch Dressing"], 
                  ["chicken", "spice", "mixed greens", "tomatoes", "cheese", "corn", "black beans", "poblano chiles", "red pepper", "creamy salad dressing"], ["chicken", "mixed greens", "cheese", "apples", "strawberries", "blueberries", "nut granola", "almonds", "Zesty Apple Cider Vinaigrette"], 
                  ["chicken", "biscuit"], ["chicken", "spice", "biscuit"], ["chicken", "biscuit"], ["chicken", "english muffin", "cheese"], ["chicken", "hask browns", "egg", "cheese", "tortilla", "jalapeno salsa"], 
                  ["chicken", "hash browns", "egg", "cheese", "Jalapeno Salsa"], ["chicken", "egg", "cheese"], ["bacon", "egg", "cheese", "biscuit"], ["sausage", "egg", "cheese", "biscuit"], ["chicken", "egg", "cheese", "english muffin"], 
                  ["bacon", "egg", "cheese", "english muffin"], ["sausage", "egg", "cheese", "english muffin"]]
foodAllergens = [["gluten", "chicken"], ["dairy", "chicken", "gluten"], ["gluten", "chicken"], ["dairy", "chicken", "gluten"], ["dairy", "chicken", "gluten"], 
                 ["dairy", "chicken", "gluten", "pork"], ["chicken", "gluten"], ["chicken", "gluten"], ["chicken", "gluten"], ["chicken", "gluten"],
                 ["chicken"], ["chicken"], ["chicken"], ["chicken", "gluten"], ["chicken", "gluten"], ["chicken", "gluten"], ["chicken", "gluten"], 
                 ["chicken", "avocado"], ["chicken", "dairy"], ["chicken", "dairy", "fruit"], ["chicken"], ["gluten", "chicken"], ["chicken", "gluten"], 
                 ["chicken", "dairy", "gluten"], ["chicken", "dairy", "gluten"], ["chicken", "dairy"], ["chicken", "egg", "dairy"], ["chicken", "egg", "dairy", "pork"], 
                 ["pork", "egg", "dairy", "gluten"], ["chicken", "egg", "dairy", "gluten"], ["pork", "egg", "dairy", "gluten"], ["pork", "egg", "dairy", "gluten"]]
flavorProfile = [["meaty", "savory"], ["fresh", "meaty", "savory"], ["meaty", "savory"], ["fresh", "meaty", "savory"], ["fresh", "meaty", "savory"], 
                 ["fresh", "meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"],
                 ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], 
                 ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["meaty", "savory"], ["meaty", "savory", "spicy"],
                 ["meaty", "savory"], ["meaty", "savory"],  ["meaty", "savory"], ["cheesey", "savory", "spicy"], ["meaty", "savory", "cheesey"], 
                 ["meaty", "savory", "cheesey"], ["meaty", "savory", "cheesey"], ["meaty", "savory", "cheesey"], ["meaty", "savory", "cheesey"], ["meaty", "savory", "cheesey"]]

CreatePremiumDeli=[]
foodNames= ["6 inch The Piglet", "6 inch Jones Club", "6 inch Pesto Chicken", "6 inch The Italian", "6 inch The OG", "6 inch Edgy Veggie", "12 inch The Piglet", "12 inch Jones Club", "12 inch Pesto Chicken", 
            "12 inch The Italian", "12 inch The OG", "12 inch Edgy Veggie", "West Coast Cobb Salad", "Chopped Wedge Salad", "Classic Ceasar Salad"]
foodPrices= [4.99, 5.99, 6.49, 5.49, 5.99, 5.49, 7.99, 8.99, 9.99, 8.49, 8.99, 7.99, 7.49, 5.49, 4.99]
foodIngredients= [["cheese", "ham", "lettuce", "tomato", "mayo", "Mustard"], ["turkey", "ham", "cheese", "bacon", "lettuce", "tomato", "jalapeno ranch"], 
                  ["pesto chicken", "spinach", "cheese", "tomato", "black olives", "pesto mayo"], ["cheese", "ham", "salami", "pepperoni", "capicola", "lettuce", "tomato", "Onion", "oil & vinegar", "salt & pepper"], 
                  ["turkey", "cheese", "lettuce", "tomato", "honey", "Dijon Dressing"], ["beet", "vegan cheese", "spinach", "tomato", "onion", "bell pepper", "oil & vinegar", "salt & pepper"], 
                  ["cheese", "ham", "lettuce", "tomato", "mayo", "mustard"], ["turkey", "ham", "cheese", "bacon", "lettuce", "tomato", "jalapeno Ranch"], 
                  ["cheese", "ham", "salami", "pepperoni", "capicola", "lettuce", "tomato", "Onion", "oil & vinegar", "salt & pepper"], ["turkey", "cheese", "lettuce", "tomato", "Honey Dijon Dressing"], 
                  ["beet", "vegan cheese", "spinach", "tomato", "onion", "bell pepper", "oil & vinegar", "salt & pepper"], ["chicken", "romaine", "spinach", "bacon", "egg", "tomato", "black olives", "Guacamole"], 
                  ["romaine", "tomato", "red onion", "bacon", "cheese", "walnut"], ["romaine", "croutons", "parmesan", "red onion"]]
foodAllergens = [["dairy", "pork"],["turkey", "pork", "dairy"], ["chicken", "dairy", "olives"], ["dairy", "pork"], ["turkey", "dairy"], ["beet", "onion", "pepper"], 
                 ["dairy", "pork", "mayo", "mustard"], ["turkey", "pork", "dairy", "jalapeno"], ["pesto chicken", "spinach", "cheese", "tomato", "black olives", "pesto mayo"], 
                 ["dairy", "pork", "gluten"], ["gluten", "dairy", "turkey"], ["gluten", "onion", "beet"], ["chicken", "pork", "egg", "olive", "guacamole"], ["walnuts", "onion", "pork", "dairy"], 
                 ["cheese", "onion", "gluten"]]
flavorProfile = [["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], 
                 ["fresh", "savory", "spicy"], ["fresh", "savory", "spicy"], ["fresh", "savory", "meaty"], ["fresh", "savory", "meaty"], ["fresh", "savory", "bitter"], 
                 ["fresh", "savory"], ["fresh", "savory"], ["fresh", "cheese", "onion"]]

DunkinDoughnuts=[]
foodNames= ["Sausage, Egg & Cheese Sandwich", "Bacon, Egg & Cheese Sandwich", "Turkey Sausage, Egg & Cheese Sandwich", "Egg & Cheese Sandwich","Sourdough Breakfast Sandwich", "Wake-Up Wrap", "Hash Brown", 
            "Muffins", "Donuts", "Munchkins Donut Hole Treats"]
foodPrices= [5.39, 5.39, 5.39, 4.39, 5.99, 1.59, 0.99, 1.35, 3.50]
foodIngredients= [["croissannt", "bagel", "english muffin", "sausage", "egg", "cheese"], ["bagel", "biscuit", "croissant", "english muffin", "bacon", "egg", "cheese"], 
                  ["english muffin", "turkey sausage", "egg", "cheese"], ["bagle", "croissant", "english muffin", "egg", "cheese"], ["sourdough bread", "egg", "bacon", "cheese"], ["tortilla", "egg" , "cheese", "bacon", "sausage", "turkey sausage"], 
                  ["potatoe"], ["buttermilk", "flour", "carrot", "blueberry", "chocolate chip", "coffee", "corn"], ["wheat flour" ,"yeast donut concentrate", "egg"], ["wheat flour" ,"yeast donut concentrate", "egg"]]
foodAllergens = [["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "pork"], ["dairy", "egg", "gluten", "soy"], 
                 ["starch"], ["egg", "chocolate", "dairy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"]]
flavorProfile = [["savory", "cheesey"], ["savory", "cheesey"], ["savory", "cheesey"], ["savory", "cheesey"], ["savory", "cheesey", "meaty"], ["savory", "cheesey"], 
                 ["savory"], ["sweet", "savory"], ["sweet", "savory"], ["sweet", "savory"]]

WingIt=[]
foodNames= ["Regular Tender Basket", "Large Tender Basket", "5 Wings", "Loaded Baked Potato", "Fried Cauliflower Basket", "Waffle Sliders", "Mac & Cheese",
            "5 Chicken Tenders", "3 Chicken Tenders", "Twiced Baked Potato Casserole", "American Potato Salad", "Steak Fries", "Coleslaw", "Crudite"]
foodPrices= [6.99, 9.19, 8.49, 5.49, 4.99, 5.49, 2.19, 7.49, 5.49, 2.19, 1.99, 2.19, 1.99, 1.19]
foodIngredients= [["chicken", "bread"], ["chicken", "bread"], ["chicken", "bread"], ["potato", "bacon", "cheese"], ["Cauliflower", "bread"],
                  ["chicken", "bread"], ["cheese", "noodles"],["chicken", "bread"], ["chicken", "bread"], ["potato", "bacon", "cheese"],
                  ["eggs", "potato", "onion"], ["bread"], ["mayo", "cabbage"], ["carrots", "celery"]]
foodAllergens = [["chicken", "gluten"], ["chicken", "gluten"], ["chicken", "gluten"], ["mayo", "pork", "gluten"], ["gluten"],
                 ["chicken", "gluten"], ["cheese", "gluten"], ["chicken", "gluten"], ["chicken", "gluten"], ["dairy"], ["mayo"],
                 ["gluten"], ["mayo"], []]
flavorProfile = [["savory", "crunchy"], ["savory", "crunchy"], ["savory", "crunchy"], ["savory", "creamy"], ["savory", "crunchy"],
                 ["savory", "cheesy"], ["savory", "crunchy"], ["savory", "crunchy"], ["savory"], ["fresh"], ["savory", "crunchy"],
                 ["fresh", "crunchy"], ["fresh", "crunchy"]]

Starbucks=[]
foodNames= ["Ham & Cheese Savory Foldover", "Wheat Spinach Savory Foldover", "Pepperoni & Tomato Savory Foldover", "Cheese Danish",
            "Butter Croissant", "Chocolate Croissant", "Blueberry Scone", "Banana Nut Bread", "Iced Lemon Pound Cake",
            "Morning Bun", "Chocolate Chip Cookie", "Double Chocolate Chunk Brownie", "Hearty Blueberry Oatmeal",
            "Bacon & Gouda Breakfast Sandwich", "Sausage & Cheddar Breakfast Sandwich", "Spinach & Feta Breakfast Wrap",
            "Reduced-Fat Turkey Bacon Breakfast Sandwich", "Slow-Roasted Ham & Swiss on Croissant Bun", "Protein Bistro Box",
            "Cheese & Fruit Bistro Box", "Omega-3 Bistro Box", "PB&J on Wheat Bistro Box", "Turkey Rustico Panini", "Turkey Pesto Panini",
            "Ham & Swiss Panini", "Chicken Santa Fe Flatbread", "Chicken BLT Salad Deli Sandwich", "Roasted Tomato & Mozzarella Panini",
            "Old-Fashioned Grilled Cheese", "Cake pop"]
foodPrices= [3.45, 3.45, 3.45, 2.45, 2.45, 2.75, 2.45, 2.75, 2.45, 2.45, 1.95, 2.35, 3.45, 3.75, 3.45, 3.75, 3.75, 4.75,
             5.25, 4.95, 5.95, 5.25, 6.45, 6.45, 5.95, 5.95, 5.95, 5.55, 5.25, 1.95]
foodIngredients= [["cheese", "bread", "ham"], ["cheese", "bread", "spinach"], ["pepperoni", "bread", "tomato"], ["cheese", "bread"],
                  ["bread"], ["chocolate", "bread"], ["blueberry", "bread"], ["banana", "bread", "nuts"],
                  ["lemon", "bread"], ["cinnamon", "bread"], ["chocolate", "bread"], ["chocolate", "bread"],
                  ["blueberry", "oatmeal"], ["egg", "bread", "bacon"], ["sausage", "bread", "egg"], ["cheese", "bread", "spinach"],
                  ["turkey", "bread", "bacon"], ["ham", "bread", "cheese"], ["cheese", "meat"], ["cheese", "fruit"],
                  ["blueberry", "nuts"], ["peanut butter", "bread", "jelly"], ["turkey", "bread", "cheese"], ["cheese", "bread", "turkey"],
                  ["cheese", "bread", "ham"], ["chicken", "bread", "cheese"], ["chicken", "bread", "bacon"], ["cheese", "bread", "tomato"],
                  ["cheese", "bread"], ["bread"]]
foodAllergens = [["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy", "nuts"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"],["gluten"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten", "dairy"],["gluten", "dairy"], ["gluten", "dairy"], ["dairy"], ["dairy"], ["nuts"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten"], ["gluten", "dairy"], ["gluten", "dairy"], ["gluten"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "dairy"]]
flavorProfile = [["savory", "cheesy"], ["savory", "cheesy"], ["savory", "cheesy"], ["savory", "cheesy"], ["savory"],
                 ["sweet"], ["sweet", "fruity"], ["sweet", "nutty"], ["sweet", "lemon"], ["sweet", "cinnamon"],
                 ["sweet"], ["sweet"], ["sweet", "fresh"], ["savory", "cheesy"], ["savory", "cheesy"],
                 ["savory", "cheesy"], ["savory", "healthy"], ["savory", "cheesy"], ["healthy", "crunchy"], ["fruity", "healthy"],
                 ["healthy", "crunchy"], ["sweet"], ["savory", "meaty"], ["savory", "fresh"], ["savory", "cheesy"],
                 ["savory", "bready"], ["savory", "fresh"], ["savory", "cheesy"], ["savory", "cheesy"], ["sweet"]]

AsadoLatinGrill=[]
foodNames= ["Refried Beans", "Black Beans", "Spanish Rice", "Grilled Chili Lime Chicken",
            "Flank Steak Fajita", "Salsa Fresca", "Classic Guacamole", "Queso", "Chorizo Tofu", "cilantro lime rice"]
foodPrices= [1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99] #FIND ACTUAL VALUES
foodIngredients= [["Beans"], ["beans"], ["rice"], ["chicken", "lime"], ["Beef"], ["tomatoes", "jalapenos"], ["avocado"],
                  ["cheese"], ["tofu", "Chorizo"], ["rice"]]
foodAllergens = [[], [], ["gluten"], ["poultry"], [], ["tomato"], ["avocado"], ["dairy"], [], ["gluten"]]
flavorProfile = [["savory"], ["savory"], ["savory"], ["savory", "meaty"], ["savory", "meaty"], ["spicy", "fresh"],
                 ["fresh", "savory"], ["cheesy", "savory"], ["savory"], ["savory"]]

KawaSushi=[]
foodNames= ["All American Roll", "All Star Combo", "Atomic Roll", "California Roll","California Combo", "California Roll Plus",
            "Caterpillar Roll", "Crunchy California Roll", "Crunchy Shrimp Roll", "Dragon Roll- Grilled Eel",
            "Dragon Roll- Salmon", "Dragon Roll- Tuna", "Dynamite Roll", "Grilled Eel Roll", "Inari Sushi", "Nigiri Delux",
            "Philadelphia Roll Imitation Crab", "Philadelphia Roll Smoked Salmon", "Potsticker- Chicken", "Potsticker- Pork",
            "Rainbow Roll", "Salmon & Avocado Roll", "Salmon Roll", "Salmon Lovers Combo", "Sashimi", "Shaggy Dog Roll",
            "South West Roll", "Spicy California Roll", "Spicy California Roll Plus", "Spicy Crab Roll Plus", "Spicy Shrimp Roll",
            "Spicy Tuna Roll", "Spring Roll- Shrimp", "Summer Roll", "Sushi & Nigiri Combo", "Sushi Delight Combo",
            "Sushic Combo", "Tailgater's Special", "Tempura Imitation Crab Roll", "Tempura Shrimp Roll", "Tuna & Avocado Roll",
            "Tuna Roll", "Tuna Lovers Combo", "Veggie Roll Plus", "Crunchy California Burrito", "Dynamite Tuna Burrito",
            "Volcano Burrito", "Salmon Poke Bowl", "Tuna Poke Bowl"]
foodPrices= [3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45
             , 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45
             , 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45, 3.45] #NEEDS PRICES
foodIngredients= [["imitation crab", "rice", "avocado"], ["imitation crab", "rice", "avocado"], ["imitation crab", "rice", "cream cheese"],
                  ["imitation crab", "rice", "cucumber"], ["imitation crab", "rice", "cucumber"], ["imitation crab", "rice", "cucumber"], ["cucumber", "rice", "avocado"],
                  ["imitation crab", "rice", "cucumber"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"],
                  ["rice", "fish"], ["rice", "tofu"], ["rice", "fish"], ["rice", "imitation crab"], ["rice", "fish"], ["bread", "chicken"],
                  ["bread", "pork"], ["rice", "fish", "avocado"], ["fish", "rice", "avocado"], ["rice", "fish"], ["rice", "fish"],
                  ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"],
                  ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"],
                  ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"],
                  ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "veggies"],
                  ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"], ["rice", "fish"]]
foodAllergens = [["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten"],
                 ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"], ["gluten", "fish"]]
flavorProfile = [["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"],
                 ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"], ["savory", "umami"]]

EiensteinsBagels=[]
foodNames= [""]
foodPrices= []
foodIngredients= [[""]]
foodAllergens = [[""]]
flavorProfile = [[""]]

MeltLab=[]
foodNames= ["Classic Sandwich", "Sunrise Sandwich", "The Italian Sandwich", "Mac Attack Sandwich", "The Big Cheese Sandwich", 
            "Lil Buffalo Sandwich", "Turkey Melt Sandwich", "Patty Melt", "Vegan Classic", "Vegan Patty Melt", "Vegan Eggplant Parm", 
            "Classic Mac & Cheese Bake", "Vegan Mac Bake", "Buffalo Mac Bake"]
foodPrices= [2.99, 4.99, 6.99, 6.49, 4.99, 6.49, 6.99, 10.99, 3.99, 9.99, 6.99, 5.99, 6.99, 6.99]
foodIngredients= [[""]]
foodAllergens = [[""]]
flavorProfile = [["meaty", "fresh", "savory"], ["fresh", "savory"], ["meaty", "fresh", "savory"], ["savory" ,"cheesey"], ["savory" ,"cheesey"], 
                 ["sweet", "savory", "tangy", "meaty"], ["meaty", "savory"], ["savory" ,"cheesey", "meaty"], ["fresh", "savory"], ["fresh", "savory"], 
                ["fresh", "savory"], ["cheesey", "savory"], ["cheesey", "fresh", "savory"], ["sweet", "cheese", "tangy", "savory"]]


MondoSubs=[]
foodNames= ["6 inch all american hero" ,"12 inch all american hero", "6 inch very veggie", "12 inch very veggie", "6 inch home on the ranch", 
            "12 inch home on the ranch", "6 inch turkey sub", "12 inch turkey sub", "6 inch the classic italian", "12 inch the classic italian", 
            "6 inch tuna tuna", "12 inch tuna tuna", "6 inch roast beef wrangler", "12 inch roast beef wrangler", "6 inch piggy wiggy" , "12 inch piggy wiggy" , 
            "6 inch buffalo chicken", "12 inch buffalo chicken", "6 inch cajun chicken", "12 inch cajun chicken", "6 inch italian meatball", "12 inch italian meatball", 
            "6 inch turkey melt", "12 inch turkey melt", "chicken ceasar wrap"]
foodPrices= [4.49, 7.99, 3.69, 6.99, 4.49, 7.99, 3.99, 6.99, 4.49, 7.99, 3.79, 6.79, 4.79, 8.49, 3.79, 6.59, 4.29, 7.99, 4.19, 7.99, 3.89, 7.49, 4.19, 
             7.59, 5.99]
foodIngredients= [["ham", "roast beef", "turkey", "cheese"], ["ham", "roast beef", "turkey", "cheese"], ["hummus", "guacamole", "bell peppers", "cucumbers", "carrots", "lettuce", "tomato"], 
                  ["hummus", "guacamole", "bell peppers", "cucumbers", "carrots", "lettuce", "tomato"], ["turkey", "bacon", "cheese", "ranch dressing"], 
                  ["turkey", "bacon", "cheese", "ranch dressing"], ["turkey", "lettuce", "tomato", "mayo"], ["turkey", "lettuce", "tomato", "mayo"], 
                  ["capicola", "salami", "pepperoni", "red pepper", "cheese"], ["capicola", "salami", "pepperoni", "red pepper", "cheese"], 
                  ["tuna", "cheese", "mayo"], ["roast beef", "red onion", "cheese", "mayo"], ["roast beef", "red onion", "cheese", "mayo"], 
                  ["ham", "cheese", "ranch dressing"], ["ham", "cheese", "ranch dressing"], ["chicken", "spicy buffalo sauce", "provolone", "blue cheese"], 
                  ["chicken", "spicy buffalo sauce", "provolone", "blue cheese"], ["chicken", "mayo", "onion", "bell pepper", "tomato", "lettuce", "cheese"], 
                  ["chicken", "mayo", "onion", "bell pepper", "tomato", "lettuce", "cheese"], ["meatballs", "marinara sauce", "provolone", "parmesan cheese"], 
                  ["meatballs", "marinara sauce", "provolone", "parmesan cheese"], ["ham", "turkey", "tomato", "mayo", "cheese"], ["ham", "turkey", "tomato", "mayo", "cheese"], 
                  ["chicken", "creamy ceasar dressing", "chopped romaine", "parmesan cheese", "tomato", "red onion"]]
foodAllergens = [["dairy", "beef", "pork", "turkey"], ["dairy", "beef", "pork", "turkey"], ["guacamole", "peppers"], ["guacamole", "peppers"], 
                 ["pork", "turkey", "dairy"], ["pork", "turkey", "dairy"], ["turkey", "dairy"], ["turkey", "dairy"], ["pork", "dairy"], ["pork", "dairy"],
                 ["fish", "dairy"], ["fish", "dairy"], ["dairy", "beef"], ["dairy", "beef"], ["beef", "dairy"], ["beef", "dairy"], ["dairy", "chicken"], ["dairy", "chicken"],
                 ["chicken", "dairy", "peppers"], ["chicken", "dairy", "peppers"], ["beef", "dairy"], ["beef", "dairy"], ["pork", "turkey", "dairy"], 
                 ["pork", "turkey", "dairy"], ["chicken", "dairy"]]
flavorProfile = [["meaty", "savory"], ["meaty", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["savory", "crisp"],["savory", "crisp"],
                 ["fresh", "savory"], ["fresh", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["fresh", "savory"], ["fresh", "savory"], 
                 ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], 
                 ["savory", "meaty", "tangy"], ["savory", "meaty", "tangy"], ["meaty", "savory"], ["meaty", "savory"], ["savory", "meaty"], ["savory", "meaty"], 
                 ["meaty", "savory"]]

PandaExpress=[]
foodNames= ["bowl", "plate", "bigger plate"]
foodPrices= [7.90, 9.40, 10.90]
foodIngredients= [["chow mein", "fried rice", "white steamed rice" ,"super greens", "brown steamed rice", "shrimp", "broccoli", "sweet and spicy sauce", "chicken", "angus steak", "onion", 
                   "bell peppers", "mushrooms", "black pepper sauce", "honey sauce", "walnuts", "teriyaki sauce", "sweet sauce", "organic honey", "beef", "sweet-tangy sauce", "pineapples", "chili sauce", 
                   "string beans", "mild ginger soy sauce", "celery", "kale", "cabbage"], ["chow mein", "fried rice", "white steamed rice" ,"super greens", "brown steamed rice", "shrimp", "broccoli", "sweet and spicy sauce", "chicken", "angus steak", "onion", 
                   "bell peppers", "mushrooms", "black pepper sauce", "honey sauce", "walnuts", "teriyaki sauce", "sweet sauce", "organic honey", "beef", "sweet-tangy sauce", "pineapples", "chili sauce", 
                   "string beans", "mild ginger soy sauce", "celery", "kale", "cabbage"], ["chow mein", "fried rice", "white steamed rice" ,"super greens", "brown steamed rice", "shrimp", "broccoli", "sweet and spicy sauce", "chicken", "angus steak", "onion", 
                   "bell peppers", "mushrooms", "black pepper sauce", "honey sauce", "walnuts", "teriyaki sauce", "sweet sauce", "organic honey", "beef", "sweet-tangy sauce", "pineapples", "chili sauce", 
                   "string beans", "mild ginger soy sauce", "celery", "kale", "cabbage"]]
foodAllergens = [["gluten, shellfish", "soybeans", "wheat", "sesame", "egg", "dairy", "treenuts"], ["gluten, shellfish", "soybeans", "wheat", "sesame", "egg", "dairy", "treenuts"], 
                 ["gluten, shellfish", "soybeans", "wheat", "sesame", "egg", "dairy", "treenuts"]]
flavorProfile = [["savory", "fresh", "meaty", "crispy", "sweet", "spicy"], ["savory", "fresh", "meaty", "crispy", "sweet", "spicy"], 
                 ["savory", "fresh", "meaty", "crispy", "sweet", "spicy"]]


# Test looper




