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

def printListLengths(foodNames,foodPrices,foodIngredients,foodAllergens,flavorProfile):
    print(f'food names length: {len(foodNames)}')
    print(f'food prices length: {len(foodPrices)}')
    print(f'food ingredients length: {len(foodIngredients)}')
    print(f'food allergens length: {len(foodAllergens)}')
    print(f'flavor profile length: {len(flavorProfile)}')
    return

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
foodAllergens = ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chocolate", "sugar"], ["dairy", "gluten"], [""]
flavorProfile = [["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["sweet"], ["savory"], ["salty"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Absurd Bird", "The Den Food Company",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


AJsBBQ=[]
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
flavorProfile = [["cheesy", "savory"], ["cheesy", "sweet", "savory"], ["cheesy", "meaty", "dry"], ["cheesy", "sweet"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], 
                 ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["sweet", "savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "AJs BBQ", "In front of Student Writing Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


AsadoLatinGrill=[]
foodNames= ["Refried Beans", "Black Beans", "Spanish Rice", "Grilled Chili Lime Chicken",
            "Flank Steak Fajita", "Salsa Fresca", "Classic Guacamole", "Queso", "Chorizo Tofu", "cilantro lime rice"]
foodPrices= [2.99, 2.99, 2.99, 7.49, 8.99, 1.99, 3.99, 3.19, 6.99, 2.99] 
foodIngredients= [["Beans"], ["beans"], ["rice"], ["chicken", "lime"], ["Beef"], ["tomatoes", "jalapenos"], ["avocado"],
                  ["cheese"], ["tofu", "Chorizo"], ["rice"]]
foodAllergens = [[], [], ["gluten"], ["poultry"], [], ["tomato"], ["avocado"], ["dairy"], [], ["gluten"]]
flavorProfile = [["savory"], ["savory"], ["savory"], ["savory", "meaty"], ["savory", "meaty"], ["spicy", "fresh"],
                 ["fresh", "savory"], ["cheesy", "savory"], ["savory"], ["savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Asado Latin Grill", "Jones Dining Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


BlimpieAmericanSubs=[]
foodNames= ["Blimple Best Rg", "Blimple Best Lg", "Turkey & Provolone Rg", "Turkey & Provolone Lg", "The Club Rg", "The Club Lg", "Ham & Swiss Rg", "Ham & Swiss Lg", "Roast Beef & Provolone Rg", 
            "Roast Beef & Provolone Lg", "Tuna Rg", "Tuna Lg", "BLT Rg", "BLT Lg", "Meatball Parmigiana Rg", "Meatball Parmigiana Lg", "Philly Cheese Steak Rg", "Philly Cheese Steak Lg", 
            "Chicken Cheddar Bacon Ranch Rg", "Chicken Cheddar Bacon Ranch Lg", "Buffalo Chicken Rg", "Buffalo Chicken Lg", "Ultimate Club Rg", "Ultimate Club Lg", "Turkey Bacon Cheddar Rg", "Turkey Bacon Cheddar Lg", 
            "Sicilian Rg", "Sicilian Lg", "The Blimp Rg", "The Blimp Lg", "Spicy Italian Rg", "Spicy Italian Lg", "Trio Supreme Rg", "Trio Supreme Lg", "Hoboken Hero Rg", "Hoboken Hero Lg", "Italian Beef Rg", 
             "Italian Beef Lg", "Turkey Reuben Rg", "Turkey Reuben Lg"]
foodPrices=[5.99, 7.49, 5.29, 7.49, 5.29, 7.49, 5.29, 7.49, 5.29, 7.49, 5.29, 7.49, 5.29, 7.49, 6.49, 12.49, 8.69, 16.99, 6.49, 12.49, 6.49, 12.49, 6.99, 13.49, 6.99, 12.99, 6.49, 12.49, 8.69, 16.69, 
            6.99, 12.99, 6.99, 12.99, 6.99, 12.99, 6.99, 12.99, 6.99, 12.99]
foodIngredients =[["ham", "salami", "capicola", "prasciuttini", "provolone", "bread"], ["ham", "salami", "capicola", "prasciuttini", "provolone", "bread"], ["turkey", "provolone", "bread"], ["turkey", "provolone", "bread"], 
                  ["ham", "turkey", "swiss", "bread"], ["ham", "turkey", "swiss", "bread"], ["ham", "swiss", "bread"], ["ham", "swiss", "bread"], ["roast beef", "provolone", "bread"],  ["roast beef", "provolone", "bread"], 
                  ["tuna", "mayo", "pickles", "bread"], ["tuna", "mayo", "pickles", "bread"], ["bacon", "lettuce", "tomato", "bread"], ["bacon", "lettuce", "tomato", "bread"], ["meatball", "cheese", "bread"], ["meatball", "cheese", "bread"], 
                  ["philly steak", "cheese", "bread"], ["philly steak", "cheese", "bread"], ["chicken", "cheddar", "bacon", "ranch", "bread"], ["chicken", "cheddar", "bacon", "ranch", "bread"], ["chicken", "buffalo sauce", "bread"], 
                  ["chicken", "buffalo sauce", "bread"], ["ham", "turkey", "swiss", "bacon", "tomato", "onion", "peppercorn dressing"], ["ham", "turkey", "swiss", "bacon", "tomato", "onion", "peppercorn dressing"], 
                  ["turkey", "bacon", "cheddar", "bread"], ["turkey", "bacon", "cheddar", "bread"], ["ham", "prosciuttini", "pepperoni", "provolone", "red pepper", "italian dressing", "bread"], ["ham", "prosciuttini", "pepperoni", "provolone", "red pepper", "italian dressing", "bread"], 
                  ["turkey", "roast beef", "prosciuttini", "salami", "pepperoni", "provolone", "sweet pepper", "tomato", "lettuce", "pickles", "onion", "mayo", "vinegar", "oil", "oregano", "bread"], 
                  ["turkey", "roast beef", "prosciuttini", "salami", "pepperoni", "provolone", "sweet pepper", "tomato", "lettuce", "pickles", "onion", "mayo", "vinegar", "oil", "oregano", "bread"], 
                  ["ham", "salami", "pepperoni", "provolone", "tomato", "lettuce", "onion", "spicy giardiniera", "bread"], ["ham", "salami", "pepperoni", "provolone", "tomato", "lettuce", "onion", "spicy giardiniera", "bread"], 
                  ["roast beef", "turkey", "bacon", "swiss", "tomato", "lettuce", "onion", "mayo"], ["roast beef", "turkey", "bacon", "swiss", "tomato", "lettuce", "onion", "mayo"], ["prosciuttini", "pepperoni", "salami", "provolone", "tomato", "lettuce", "onions", "vinegar", "oil", "oregano", "bread"], 
                  ["prosciuttini", "pepperoni", "salami", "provolone", "tomato", "lettuce", "onions", "vinegar", "oil", "oregano", "bread"], ["roast beef", "au jus", "provolone", "spicy", "giardiniera", "parmesan", "bread"], 
                  ["roast beef", "au jus", "provolone", "spicy", "giardiniera", "parmesan", "bread"], ["turkey", "sauerkaut", "swiss", "1000 island dressing", "bread"], ["turkey", "sauerkaut", "swiss", "1000 island dressing", "bread"]]
foodAllergens=[["pork", "dairy", "gluten"], ["pork", "dairy", "gluten"], ["dairy", "turkey", "gluten"], ["dairy", "turkey", "gluten"], ["pork", "turkey", "dairy", "gluten"], ["pork", "turkey", "dairy", "gluten"], 
               ["pork", "dairy", "gluten"], ["pork", "dairy", "gluten"], ["beef", "dairy", "gluten"], ["beef", "dairy", "gluten"], ["fish", "mayo", "gluten"], ["fish", "mayo", "gluten"], ["pork", "gluten"], ["pork", "gluten"], 
               ["beef", "dairy", "gluten"], ["beef", "dairy", "gluten"], ["beef", "dairy", "gluten"], ["beef", "dairy", "gluten"], ["chicken", "dairy", "pork"], ["chicken", "dairy", "pork"], ["chicken", "gluten"], ["chicken", "gluten"], 
               ["pork", "turkey", "dairy", "peppercorn"], ["pork", "turkey", "dairy", "peppercorn"], ["turkey", "pork", "dairy", "gluten"], ["turkey", "pork", "dairy", "gluten"], ["pork", "dairy", "gluten"], ["pork", "dairy", "gluten"], 
               ["turkey", "beef", "pork", "vinegar"], ["turkey", "beef", "pork", "vinegar"], ["pork", "dairy", "gluten"], ["pork", "dairy", "gluten"], ["beef", "turkey", "pork", "dairy", "gluten"], ["beef", "turkey", "pork", "dairy", "gluten"], 
               ["pork", "dairy", "gluten"], ["pork", "dairy", "gluten"], ["beef", "dairy"], ["beef", "dairy"], ["turkey", "dairy", "gluten"], ["turkey", "dairy", "gluten"]]
flavorProfile=[["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory"], 
               ["meaty", "savory"], ["meaty", "savory"], ["meaty", "savory", "fresh"], ["meaty", "savory", "fresh"], ["meaty", "savory", "fresh"], ["meaty", "savory", "fresh"], ["meaty", "savory"], ["meaty", "savory"], 
               ["meaty", "cheesy", "savory"], ["meaty", "cheesy", "savory"], ["meaty", "savory"], ["meaty", "savory"], ["meaty", "cheesy", "savory"], ["meaty", "cheesy", "savory"], ["meaty", "cheesy", "savory"], ["meaty", "cheesy", "savory"], 
               ["meaty", "fresh", "savory"], ["meaty", "fresh", "savory"], ["meaty", "fresh", "savory"], ["meaty", "fresh", "savory"], ["spicy", "meaty", "savory"], ["spicy", "meaty", "savory"], ["meaty", "cheesy", "savory"], ["meaty", "cheesy", "savory"], 
               ["meaty", "cheesy", "savory", "tangy"], ["meaty", "cheesy", "savory", "tangy"], ["meaty", "spicy", "savory"], ["meaty", "spicy", "savory"], ["tangy", "sweet", "meaty", "savory"], ["tangy", "sweet", "meaty", "savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Blimpie American Subs", "The Den Food Company",
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

#Information may be incorrect as there were 33 ingredients entries and 31 price entries
chickfila=[]
foodNames= ["Chicken Sandwich", "Deluxe Sandwich w cheese", "Spicy Chicken Sandwich", "Spicy Deluxe Sandwich w cheese", "Grilled Chicken Sandwich", "Grilled Chicken Club w cheese", 
            "5 ct Chicken Nuggets", "8 ct Chicken Nuggets", "12 ct Chicken Nuggets", "30 ct Chicken Nuggets", "5 ct Grilled Nuggets", "8 ct Grilled Nuggets", "12 ct Grilled Nuggets", 
            "2 ct Chick-n-Strips", "3 ct Chick-n-Strips", "4 ct Chick-n-Strips", "Cool Wrap", "Cobb Salad", "Spicy Southwest Salad", "Grilled Market Salad", "Chicken Biscuit", 
            "Spicy Chicken Biscuit", "4 ct Chick-n-Minis", "Egg White Grill", "Hash Brown Scramble Burrito w Nuggets", "Hash Brown Scramble Bowl w Nuggets", "Chicken, Egg & Cheese Biscuit", 
            "Bacon, Egg & Cheese Biscuit", "Sausage, Egg & Cheese Biscuit", "Chicken, Egg & Cheese Muffin", "Bacon, Egg & Cheese Muffin", "Sausage, Egg & Cheese Muffin"]
foodPrices= [6.49, 7.39, 6.89, 7.79, 11.05, 4.50, 6.59, 9.05, 22.55, 4.79, 7.65, 10.89, 4.75, 6.99, 8.79, 10.49, 12.35, 12.59, 12.59, 8.95, 9.29, 10.25, 10.85, 10.79, 10.79, 10.39,
             9.49, 9.49, 10.49, 9.75, 9.75, 9.75]
foodIngredients= [["chicken", "bread", "breading", "pickles"],["chicken", "bread", "breading", "tomato", "lettuce", "pickles", "cheese"],["chicken", "spice", "bread", "breading", "pickles"],
                  ["chicken", "bread", "breading", "spice", "tomato", "lettuce", "pickles", "cheese"],["chicken", "spice", "bread", "breading", "pickles"], ["bread", "chicken", "tomato", "lettuce", "Honey Roasted BBQ sauce"], 
                  ["chicken", "bread", "tomato", "lettuce", "bacon", "Honey Roasted BBQ Sauce"], ["chicken", "breading"], ["chicken", "breading"], 
                  ["chicken", "breading"], ["chicken", "breading"], ["chicken"], ["chicken"], ["chicken"], ["chicken", "breading"], ["chicken", "breading"], 
                  ["chicken", "breading"], ["chicken", "cheese", "lettuce", "tortilla", "Avocado lime ranch Dressing"], ["chicken", "breading", "mixed greens", "corn", "cheese", "bacon", "egg", "tomato", "Avocado lime ranch Dressing"], 
                  ["chicken", "spice", "mixed greens", "tomatoes", "cheese", "corn", "black beans", "poblano chiles", "red pepper", "creamy salad dressing"], ["chicken", "mixed greens", "cheese", "apples", "strawberries", "blueberries", "nut granola", "almonds", "Zesty Apple Cider Vinaigrette"], 
                  ["chicken", "biscuit"], ["chicken", "spice", "biscuit"], ["chicken", "biscuit"], ["chicken", "english muffin", "cheese"], ["chicken", "hask browns", "egg", "cheese", "tortilla", "jalapeno salsa"], 
                  ["chicken", "hash browns", "egg", "cheese", "Jalapeno Salsa"], ["chicken", "egg", "cheese"], ["bacon", "egg", "cheese", "biscuit"], ["sausage", "egg", "cheese", "biscuit"], ["chicken", "egg", "cheese", "english muffin"], 
                  ["bacon", "egg", "cheese", "english muffin"]]
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
                 ["meaty", "savory"], ["meaty", "savory"],  ["meaty", "savory"], ["cheesy", "savory", "spicy"], ["meaty", "savory", "cheesy"], 
                 ["meaty", "savory", "cheesy"], ["meaty", "savory", "cheesy"], ["meaty", "savory", "cheesy"], ["meaty", "savory", "cheesy"], ["meaty", "savory", "cheesy"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Chick Fil A", "LBJ Student Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


CoffeeandPiMarket=[]
foodNames= ["chex mix", "paqui chips", "zapp's chips", "stacy's pita chips", "gardettos", "kettle chips", "PopTart",
            "nutri-grain bar", "black forest gummy", "kind bar", "belvita", "ctc cereal bar", "trix cereal bar",
            "clif bar", "luna bar", "rice krispie treat", "nature valley bar", "rxbar", "kellogs protein bar", "think thin bar",
            "milk duds", "hershey's bar", "twizzlers", "trolli gummy", "welch's fruit snack", "haribo fruit snack", "lifesavers", "gummy bears"]
foodPrices= [4.39, 2.39, 1.29, 1.19, 4.49, 1.39, 1.55, 1.39, 2.49, 3.25, 1.79, 2.39, 1.09, 2.49, 2.49, 1.29, 1.49, 3.89,
             2.85, 2.85, 1.89, 2.05, 2.05, 3.19, 3.19, 1.19, 2.49, 1.19]
foodIngredients= [["corn", "bread", "salt"], ["corn"], ["potato"], ["bread"], ["rye", "salt"], ["potato"], ["bread", "sugar"],
                  ["bread", "sugar"], ["gluten", "sugar"], ["granola", "nuts"], ["bread"], ["cereal"], ["cereal", "sugar"],
                  ["granola", "nuts"], ["granola", "nuts"], ["cereal", "sugar"], ["granola", "nuts"], ["granola", "nuts"],
                  ["granola", "nuts"], ["granola", "nuts"], ["chocolate", "malt"], ["chocolate"], ["gluten", "sugar"],
                  ["gluten", "sugar"], ["gluten", "sugar"], ["gluten", "sugar"], ["gluten", "sugar"], ["gluten", "sugar"]]
foodAllergens = [["gluten"], ["corn", "gluten"], ["gluten"], ["gluten"], ["gluten"], ["gluten"], ["gluten", "dairy"],
                 ["gluten", "dairy"], ["gluten"], ["gluten", "nuts"], ["gluten", "nuts"], ["gluten", "nuts"], ["gluten"],
                 ["gluten", "dairy"], ["gluten", "dairy"], ["gluten", "nuts"], ["gluten", "nuts"], ["gluten", "nuts"],
                 ["gluten", "nuts"], ["gluten", "nuts"], ["gluten", "malt"], ["gluten", "chocolate"], ["gluten", "sugar"],
                 ["gluten", "sugar"], ["gluten", "sugar"], ["gluten", "sugar"], ["gluten", "sugar"], ["gluten", "sugar"]]
flavorProfile = [["savory", "salty"], ["savory", "salty", "spicy"], ["savory", "salty"], ["savory", "salty"],  ["savory", "salty"],  ["savory", "salty"],  ["sweet", "sugary"],
                 ["healthy", "nutty"], ["sweet", "chewy"], ["healthy", "nutty"],["healthy", "nutty"], ["healthy", "nutty"], ["sweet", "crunchy"],
                 ["healthy", "nutty"],["healthy", "nutty"], ["sweet", "sugary"],["healthy", "nutty"], ["healthy", "nutty"],
                 ["healthy", "nutty"],["healthy", "nutty"], ["sweet", "chewy"], ["sweet"], ["sweet", "chewy"],
                 ["sweet", "chewy"], ["sweet", "chewy"], ["sweet", "chewy"], ["sweet", "chewy"], ["sweet", "chewy"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Coffee and Pi Market", "Ingram Building",
                         foodList=[])
masterListRestaurants.append(restaurantObject)












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
foodNames= ["Sausage, Egg & Cheese Sandwich", "Bacon, Egg & Cheese Sandwich", "Turkey Sausage, Egg & Cheese Sandwich", "Egg & Cheese Sandwich", "Sourdough Breakfast Sandwich", "Wake-Up Wrap", "Hash Brown", 
            "Muffins", "Donuts", "Munchkins Donut Hole Treats"]
foodPrices= [5.39, 5.39, 5.39, 4.39, 5.99, 1.59, 0.99, 1.35, 3.50]
foodIngredients= [["croissannt", "bagel", "english muffin", "sausage", "egg", "cheese"], ["bagel", "biscuit", "croissant", "english muffin", "bacon", "egg", "cheese"], 
                  ["english muffin", "turkey sausage", "egg", "cheese"], ["bagle", "croissant", "english muffin", "egg", "cheese"], ["sourdough bread", "egg", "bacon", "cheese"], ["tortilla", "egg" , "cheese", "bacon", "sausage", "turkey sausage"], 
                  ["potatoe"], ["buttermilk", "flour", "carrot", "blueberry", "chocolate chip", "coffee", "corn"], ["wheat flour" ,"yeast donut concentrate", "egg"], ["wheat flour" ,"yeast donut concentrate", "egg"]]
foodAllergens = [["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "pork"], ["dairy", "egg", "gluten", "soy"], 
                 ["starch"], ["egg", "chocolate", "dairy"], ["dairy", "egg", "gluten", "soy"], ["dairy", "egg", "gluten", "soy"]]
flavorProfile = [["savory", "cheesy"], ["savory", "cheesy"], ["savory", "cheesy"], ["savory", "cheesy"], ["savory", "cheesy", "meaty"], ["savory", "cheesy"], 
                 ["savory"], ["sweet", "savory"], ["sweet", "savory"], ["sweet", "savory"]]





KawaSushi=[]
foodNames= ["All American Roll", "All Star Combo", "Atomic Roll", "California Roll","California Combo",
            "California Roll Plus", "Caterpillar Roll", "Crunchy California Roll", "Crunchy Shrimp Roll", "Dragon Roll- Grilled Eel",
            "Dragon Roll- Salmon", "Dragon Roll- Tuna", "Dynamite Roll", "Grilled Eel Roll", "Inari Sushi",
            "Nigiri Delux", "Philadelphia Roll Imitation Crab", "Philadelphia Roll Smoked Salmon", "Potsticker- Chicken", "Potsticker- Pork",
            "Rainbow Roll", "Salmon & Avocado Roll", "Salmon Roll", "Salmon Lovers Combo", "Sashimi",
            "Shaggy Dog Roll", "South West Roll", "Spicy California Roll", "Spicy California Roll Plus", "Spicy Crab Roll Plus",
            "Spicy Shrimp Roll", "Spicy Tuna Roll", "Spring Roll- Shrimp", "Summer Roll", "Sushi & Nigiri Combo",
            "Sushi Delight Combo", "Sushi Combo", "Tailgater's Special", "Tempura Imitation Crab Roll", "Tempura Shrimp Roll",
            "Tuna & Avocado Roll", "Tuna Roll", "Tuna Lovers Combo", "Veggie Roll Plus", "Crunchy California Burrito",
            "Dynamite Tuna Burrito", "Volcano Burrito", "Salmon Poke Bowl", "Tuna Poke Bowl"]
foodPrices= [8.99, 11.99, 8.49, 8.49, 11.99, 8.99, 8.49, 8.49, 8.49, 8.49,
             8.49, 8.49, 8.49, 8.49, 8.49, 11.99, 8.49, 8.49, 5.99, 5.99,
             8.49, 8.49, 8.49, 11.99, 10.99, 8.49, 8.49, 8.49, 8.99, 8.99,
             8.49, 8.49, 8.49, 8.49, 11.99, 10.99, 11.99, 11.99, 8.49, 8.49,
             8.49, 8.49, 11.99, 8.49, 9.49, 9.49, 9.49, 9.49, 9.49]
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


McCoyCafe=[]
foodNames= ["parfait", "fruit", "pineapple", "chicken salad snacker", "apple snacker", "simply eggs", "grapes and cheddar",
            "pepperoni and cheese", "mediterranean dipper", "buffalo chicken wrap", "veggie and ranch wrap", "chicken BLT wrap",
            "big italy wrap", "oreo delight", "vanilla goodness", "apple pie trifle", "kickin chicken sandwich", "turkey swiss sandwich",
            "egg salad sandwich", "turkey and cheddar blt sandwich", "pb&j sandwich", "ham and cheese sandwich", "italian wedge sandwich",
            "chicken salad sandwich", "chicken caesar salad", "cobb salad", "southwest chicken salad", "the lil garden salad",
            "deluxe garden salad", "asian chicken salad", "bacon egg and cheese taco", "chorizo breakfast burrito", "sausage breakfast burrito"]
foodPrices= [4.69, 4.19, 4.69, 5.19, 4.29, 5.19, 3.99, 4.69, 5.49, 5.59, 5.59, 6.19, 6.19, 3.29, 3.29, 4.19, 6.19, 7.19,
             6.19, 6.69, 4.39, 6.49, 6.19, 9.19, 7.99, 7.99, 7.99, 5.59, 7.29, 7.69, 5.19, 4.99, 4.99]
foodIngredients= [["yogurt", "granola", "fruit"], ["fruit"], ["pineapple"], ["chicken", "mayo", "egg"], ["apple", "peanut butter"],
                  ["egg"], ["fruit", "cheese"], ["meat", "cheese"], ["hummus", "bread"], ["chicken", "bread"], ["vegetables", "ranch", "bread"],
                  ["chicken", "bacon", "vegetables"], ["sausage", "bread", "vegetables"], ["cookie"], ["sugar"], ["fruit", "bread", "sugar"],
                  ["chicken", "bread"], ["turkey", "bread"], ["egg", "bread"], ["turkey", "cheese", "bacon"], ["peanut butter", "jelly", "bread"],
                  ["ham", "cheese", "bread"], ["vegetables", "bread"], ["Chicken", "mayo", "bread"], ["chicken", "vegetables"],
                  ["vegetables"], ["vegetables", "chicken"], ["vegetables"], ["vegetables"], ["vegetables"], ["bacon", "egg", "cheese", "bread"],
                  ["chorizo", "bread", "cheese"], ["sausage", "bread", "cheese"]]
foodAllergens = [["nuts", "dairy"], [""], [""], ["dairy", "poultry"], ["nuts"], ["poultry"], ["dairy"], ["dairy"], ["gluten"],
                 ["gluten"], ["gluten"], ["gluten"], ["gluten"], ["dairy", "gluten"], ["dairy", "gluten"], ["dairy", "gluten"],
                 ["poultry", "gluten"], ["turkey", "gluten"], ["dairy", "gluten"], ["dairy", "gluten"], ["nuts", "gluten"],
                 ["dairy", "gluten"], ["gluten"], ["poultry", "gluten"], ["poultry"], [""], ["poultry"], [""], [""], ["poultry"],
                 ["dairy", "gluten"], ["dairy", "gluten"], ["dairy", "gluten"]]
flavorProfile = [["sweet", "healthy"], ["sweet", "healthy"], ["sweet", "healthy"], ["savory", "creamy"], ["helathy", "crunchy"],
                 ["savory"], ["savory", "sweet", "healthy"], ["meaty", "cheesy"], ["savory", "healthy"], ["meaty", "savory"],
                 ["savory", "healthy"], ["meaty", "crunchy"], ["meaty", "saucy"], ["sweet", "creamy"], ["sweet", "creamy"],
                 ["crunchy", "sweet", "fruity"], ["savory", "meaty"], ["savory", "meaty"], ["savory"], ["savory", "meaty"],
                 ["savory", "sweet"], ["savory", "meaty"], ["savory", "healthy"],  ["savory", "meaty"], ["savory", "healthy"],
                 ["savory", "healthy"], ["savory", "meaty"], ["savory", "healthy"], ["savory", "healthy"], ["savory", "healthy"],
                 ["savory", "cheesy"], ["savory", "meaty"], ["savory", "meaty"]]


EiensteinsBagels=[]
foodNames= ["Albuquerque Turkey", "Cheese Pizza Bagels", "Pepperoni Pizza Bagel", "Pepperoni Chicken Toasted Ciabatta", "Spicy Chicken Toasted Ciabatta", 
            "Cheesy Veggie Melt", "Noza Lox", "Turkey, Bacon, Avacado", "Tasty Turkey", "Avocado Veg Out", "Farmhouse 1 Egg", "Farmhouse 2 Egg", 
            "Garden Avocado 1 Egg", "Garden Avocado 2 Egg", "Big Breakfast Burrito", "All-Nighter", "Santa Fe 1 Egg White", "Santa Fe 2 Egg White", 
            "Bacon, Avocado & Tomato 1 Egg White", "Bacon, Avocado & Tomato 2 Egg White"]
foodPrices= [7.19, 5.99, 6.49, 7.19, 7.19, 6.79, 7.99, 7.19, 7.19, 6.79, 6.29, 7.29, 5.79, 6.79, 6.49, 6.99, 5.79, 5.99, 6.99, ]
foodIngredients= [["bacon", "cheddar", "lettuce", "tomato", "green chiles", "plain shmear on six cheese gourmet"], ["cheese", "bagle"], 
                  ["pepperoni", "cheese", "bagle"], ["swiss", "asiago cheese", "onion", "spleach", "tomato spread", "ciabatta"], 
                  ["bacon", "cheddar", "jalapenos", "onion", "jalapeno salsa","chicken", "ciabatta"], ["cheddar", "swiss", "tomato", "spinach", "tomato spread", "ciabatta"], 
                  ["onion", "capers", "tomato", "plain shmear"], ["lettuce", "tomato", "tomato spread", "ciabatta"], 
                  ["spinach", "cucumber", "lettuce", "tomato", "onion", "chive shmear", "asiago"], ["tomato", "cucumber", "onion", "spinach", "lettuce", "shmear", "sesame"], 
                  ["bacon", "ham", "cheddar", "schmear", "cheese", "hash brown", "egg"], ["bacon", "ham", "cheddar", "schmear", "cheese", "hash brown", "egg"], 
                  ["tomato", "spinach", "tomato spread", "egg", "avocado"], ["tomato", "spinach", "tomato spread", "egg", "avocado"], 
                  ["bacon", "turkey-sausage", "cheese", "green chiles", "hash browns", "salsa", "shmear", "tortilla", "egg"], 
                  ["bacon", "cheese", "Jalapeno garlic aioli", "hash brown", "egg"], ["egg", "turkey-sausage", "cheddar", "salsa", "shmear", "asiago"], 
                  ["egg", "turkey-sausage", "cheddar", "salsa", "shmear", "asiago"], ["egg", "avocado", "tomato", "bread", "bacon"], 
                  ["egg", "avocado", "tomato", "bread", "bacon"]]
foodAllergens = [["pork", "dairy"], ["dairy", "gluten"], ["pork", "dairy", "gluten"], ["dairy", "gluten"], ["pork", "dairy", "gluten"], 
                 ["dairy", "gluten"], ["gluten"], ["gluten"], ["gluten"], ["sesame", "gluten"], ["pork", "dairy", "gluten"], 
                 ["pork", "dairy", "gluten"], ["avocado", "egg"], ["avocado", "egg"], ["egg", "pork"], ["egg", "dairy", "pork"], 
                 ["egg", "dairy", "turkey"], ["egg", "dairy", "turkey"], ["egg", "avocado", "pork", "gluten"], ["egg", "avocado", "pork", "gluten"]]
flavorProfile = [["meaty", "savory"], ["cheesy", "savory"], ["meaty", "cheesy", "savory"], ["cheesy", "savory"],  ["meaty", "cheesy", "savory"], 
                 ["fresh", "savory"],["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"], 
                 ["cheesy", "savory", "meaty"], ["cheesy", "savory", "meaty"], ["fresh"], ["fresh"], ["cheesy", "savory"], ["savory"], 
                 ["savory", "cheesy"], ["savory", "cheesy"], ["fresh", "savory"], ["fresh", "savory"]]

MeltLab=[]
foodNames= ["Classic Sandwich", "Sunrise Sandwich", "The Italian Sandwich", "Mac Attack Sandwich", "The Big Cheese Sandwich", 
            "Lil Buffalo Sandwich", "Turkey Melt Sandwich", "Patty Melt", "Vegan Classic", "Vegan Patty Melt", "Vegan Eggplant Parm", 
            "Classic Mac & Cheese Bake", "Vegan Mac Bake", "Buffalo Mac Bake"]
foodPrices= [2.99, 4.99, 6.99, 6.49, 4.99, 6.49, 6.99, 10.99, 3.99, 9.99, 6.99, 5.99, 6.99, 6.99]
foodIngredients= [["cheese", "bread"], ["cheese", "hashbrowns", "egg", "bacon", "maple butter", "bread"], ["provolone", "salami", "pepperoni", "ham", "tomato", "arugula", "banana pepper", "garlic aioli", "bread"], 
                  ["mac and cheese", "chicken", "ranch", "jalapeno"], ["American", "cheddar", "swiss", "bread"], ["chicken", "buffalo sauce", "coleslaw", "blue cheese", "american", "bread"], 
                  ["turkey", "cheese", "avacado", "tomato", "arugula", "honey mustard", "bacon", "bread"], ["jalapenos", "cheese", "bacon", "tortilla chips", "cream cheese", "bread"], 
                  ["vegan cheese", "bread"], ["beyond patty", "vegan cheese", "vegan mayo", "pickles", "onion", "bread"], ["eggplant", "tomato", "vegan cheese", "garlic", "red pepper", "basil"], 
                  ["cheddar", "pasta"], ["vegan cheese", "pasta"], ["cheese", "pasta", "buffalo cheese sause", "bacon", "blue cheese", "onion" "chicken"]]
foodAllergens = [["dairy", "gluten"], ["dairy", "egg", "pork"], ["dariy", "pork", "garlic"], ["gluten", "dairy", "chicken",], ["dairy", "gluten"], 
                 ["chicken", "dairy", "gluten"], ["dariy", "turkey", "avacado", "pork", "gluten"], ["gluten"], ["gluten"], ["garlic", "basil"], 
                 ["gluten", "dairy"], ["gluten"],["dairy", "gluten", "chicken"]]
flavorProfile = [["cheesy", "fresh", "savory"], ["cheesy", "fresh", "savory"], ["meaty", "fresh", "savory"], ["savory" ,"cheesy"], ["savory" ,"cheesy"], 
                 ["sweet", "savory", "tangy", "meaty"], ["meaty", "savory"], ["savory" ,"cheesy", "meaty"], ["fresh", "savory"], ["fresh", "savory"], 
                ["fresh", "savory"], ["cheesy", "savory"], ["cheesy", "fresh", "savory"], ["sweet", "cheese", "tangy", "savory"]]


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


pizzahut=[]
foodNames =["Personal Pan Pizza - Cheese", "Personal Pan Pizza - Pepperoni", "Personal Pan Pizza - Italian Sausage", "Personal Pan Pizza - Supreme", "Meaty Marinara Pasta", "Chicken Alfredo Pasta", "Breadsticks", "6 Baked Wings"]
foodPrices =[4.79, 4.79, 4.79, 4.79, 5.49, 5.49, 3.19, 5.39]
foodIngredients=[["cheese", "bread", "tomato sauce"],["cheese", "bread", "tomato sauce", "pepperoni"],["cheese", "bread", "tomato sauce", "sausage"],["cheese", "bread", "tomato sauce", "mushroom"],["meat", "tomato sause"],["Chicken", "pasta", "sauce"],["bread", "tomato sauce"],["bread", "wings", "chicken"]]
foodAllergens =[["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"],["gluten", "dairy"]]
flavorProfile =[["savory", "cheesy"],["savory", "cheesy", "meaty"],["savory", "cheesy", "meaty"],["savory", "cheesy"],["savory", "meaty", "saucy"],["savory", "creamy"],["savory", "salty"],["savory", "saucy"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Pizza Hut", "LBJ Student Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


pomhoney=[]
foodNames= ["Salad", "Pita Wrap", "Grain Bowl"]
foodPrices= [7.99, 7.99, 7.99]
foodIngredients= [["Falafel", "Chicken", "Lamb", "Beef", "Hummus"], ["Falafel", "Chicken", "Lamb", "Beef", "Hummus"], ["Falafel", "Chicken", "Lamb", "Beef", "Hummus"]]
foodAllergens = [["dairy", "eggs", "gluten", "garlic"], ["dairy", "eggs", "gluten", "garlic"], ["dairy", "eggs", "gluten", "garlic"]]
flavorProfile = [["fresh", "savory"], ["fresh", "savory"], ["fresh", "savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Pom and Honey", "The Den Food Company",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


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

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Revolution Noodle", "LBJ Student Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)

thesaltymenu=[]
foodNames= ["Horchata", "Traditional Glazed", "Churro + Dulce de leche star", "Texas Chocolate sheet cake", "Boston Cream", "Ube Pina Colada(V)"]
foodPrices= [4.50, 3.50, 4.25, 4.25, 4.65, 4.75]
foodIngredients= [["brioche", "horchata mixture", "chocolate, cinnamon"],["dough", "vanilla bean glaze"],["broche", "cinnamon", "sugar", "coffee", "whipped cream"], ["chocolate", "dough", "sugar", "glaze"], ["brioche", "vinilla custard", "ganache glaze"], ["vegan brioche", "pineapple jam", "coconut milk glaze", "coconut streusel"]]
foodAllergens = [["gluten", ""],["gluten", ""],["gluten"],["gluten"], ["gluten"], ["gluten"]]
flavorProfile = [["sweet"], ["sweet"], ["sweet", "bitter"], ["sweet", "savory"], ["sweet"], ["sweet"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "The Salty", "Outside the Food Co Building",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


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

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Shake Smart", "Student Rec Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


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

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Starbucks", "Alkek Library/ LBJ Student Center",
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

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Tu Taco", "LBJ Student Center",
                         foodList=[])


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
                 ["fresh", "crunchy"], ["fresh", "crunchy"], ["Savory"]]

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Wing It", "Jones Dining Center",
                         foodList=[])


#Might have something Wrong, flavor profile was minus 1
WoodsStPizzaAndPasta=[]
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

restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
                        flavorProfile, "Woods St Pizza & Pasta", "Jones Dining Center",
                         foodList=[])
masterListRestaurants.append(restaurantObject)


#DO NOT DELETE NICK 4/17/2023
restaurantName = ""
restaurantLocation = "Click the buttons to begin"
dummyRestaurant=[]
foodNames= ["This is a Placeholder"]
foodPrices=[0.00]
foodIngredients =[[""]]
foodAllergens=[[""]]
flavorProfile=[[""]]

#restaurantObject =setRestaurantObject(foodNames, foodIngredients, foodAllergens,
#                        flavorProfile, "Placeholder", "",
#                         foodList=[])
#masterListRestaurants.append(restaurantObject)



