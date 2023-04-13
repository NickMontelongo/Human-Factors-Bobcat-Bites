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

def setFoodForRestaurant(restaurant, foodNamesList, foodPricesList,
                         foodIngredientsList, foodAllergensList, foodTastesList):
    for eachEntry in range(len(foodNamesList)):
        newItem = Food(foodNamesList[eachEntry], foodPricesList[eachEntry], foodIngredientsList[eachEntry],
                        foodAllergensList[eachEntry], foodTastesList[eachEntry])
        restaurant.append(newItem)
    return restaurant


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

foodlist =setFoodForRestaurant(absurdbird,foodNames, foodPrices, foodIngredients,
                                                  foodAllergens, flavorProfile)
masterListRestaurants.append(Restaurant("Absurd Bird", foodlist, "The Den Food Company" ))


burger512 = []
foodNames =["korean flame", "blue mushroom", "guadalupe burger", "hays co burger", "the classic", "fiesta fries", "firebird fries", "disco fries", "fries", "chicken strips"]
foodPrices=[7.99, 7.99, 7.99, 7.99, 6.99, 6.19, 5.69, 4.69, 2.19, 5.99]
foodIngredients =[["bread", "fried onions", "pico de gallo", "cheese", "kimchi", "beef", "gochujang mayo"], ["blue cheese", "bread", "beef", "mushrooms", "bacon"], ["cheese", "guacamole", "pico de gallo", "tortilla strips", "bread", "black bean", "beef"], 
                  ["cheese", "fried onions", "barbeque sauce", "bacon", "bread", "beef", "gochujang mayo"], ["black beans", "cheese", "guacamole", "potatoes", "flour", "pico de gallo"],["pickles", "tomatoes", "beef", "bread", "lettuce", "cheese"], ["teriyaki", "chicken", "flour", "cilantro", "kimchi", "gochujang mayo", "potatoes"],
                  ["cheese", "bacon", "potatoes", "flour", "fried onions"], ["potatoes", "flour", "seasoning"], ["chicken", "flour", "seasoning"]]
foodAllergens = [["gluten", "beef", "dairy", "eggs"], ["gluten", "beef", "dairy", "pork"], ["dairy", "gluten", "beef", "beans"], ["dairy", "gluten", "pork", "beef", "eggs"], ["dairy", "beef", "gluten" ],["beans", "dairy"], ["chicken", "eggs"], ["dairy", "pork"], ["none"], ["gluten", "chicken"]]
flavorProfile = [["savory", "salty", "spicy"],["savory", "salty"], ["savory", "salty"], ["savory", "sweet", "salty"], ["savory", "salty"], ["salty", "savory"], ["salty"], ["salty"], ["salty"], ["salty", "savory"]]

foodlist = setFoodForRestaurant(burger512,foodNames, foodPrices, foodIngredients,
                                                  foodAllergens, flavorProfile)
masterListRestaurants.append(Restaurant("Burger 512", foodlist, "LBJ Student Center"))

teaco=[]
foodNames= ["vietnamese sandwich", "spring rolls", "egg rolls"]
foodPrices= [4.95, 4.49, 3.25]
foodIngredients= [["bread", "pork", "mayo", "cilantro", "vinegar", "onion", "carrot", "cilantro", "chilies"],["rice wrapper", "rice noodle", "carrot", "cucumber", "shrimp", "mint", "basil", "cilantro"], ["pork", "garlic", "ginger", "coleslaw", "onion", "soy sauce", "egg roll wrapper", "egg", "sesame oil"]]
foodAllergens = [["pork", "eggs", "gluten", "chilies"],["gluten", "shrimp"],["pork", "egg", "garlic"]]
flavorProfile = [["savory", "spicy"], ["savory"], ["savory"]]

foodlist = setFoodForRestaurant(teaco,foodNames, foodPrices, foodIngredients,
                                                  foodAllergens, flavorProfile)
masterListRestaurants.append(Restaurant("Tea Co", foodlist, "The Den Food Company"))

trashArray = [1,2,3,4,5,6,7]




# pizzahut=[]
# foodNames =["Personal Pan Pizza - Cheese", "Personal Pan Pizza - Pepperoni", "Personal Pan Pizza - Italian Sausage", "Personal Pan Pizza - Supreme", "Meaty Marinara Pasta", "Chicken Alfredo Pasta", "Breadsticks", "6 Baked Wings"]
# foodPrices =[4.79, 4.79, 4.79, 4.79, 14.99, 11.99, 14.99]
# foodIngredients=[["cheese", "bread", "tomato sauce"],["cheese", "bread", "tomato sauce"],["cheese", "bread", "tomato sauce"],["cheese", "bread", "tomato sauce"],["cheese", "bread", "tomato sause"],["cheese", "bread", "tomato sause"],["cheese", "bread", "tomato sause"],]
# foodAllergens =[["gluton", "dairy"],["gluton", "dairy"],["gluton", "dairy"],["gluton", "dairy"],["gluton", "dairy"],["gluton", "dairy"],["gluton", "dairy"]]
# flavorProfile =[["savory", "cheesey"],["savory", "cheesey"],["savory", "cheesey"],["savory", "cheesey"],["savory", "cheesey"],["savory", "cheesey"],["savory", "cheesey"]]

thesaltymenu=[]
foodNames= ["Horchata", "Traditional Glazed", "Churro + Dulce de leche star", "Texas Chocolate sheet cake", "Boston Cream", "Ube Pina Colada(V)"]
foodPrices= [4.50, 3.50, 4.25, 4.25, 4.65, 4.75]
foodIngredients= [["brioche", "horchata mixture", "chocolate, cinnamon"],["dough", "vanilla bean glaze"],["broche", "cinnamon", "sugar", "coffee", "whipped cream"], ["chocolate", "dough", "sugar", "glaze"], ["brioche", "vinilla custard", "ganache glaze"], ["vegan brioche", "pineapple jam", "coconut milk glaze", "coconut streusel"]]
foodAllergens = [["gluten", ""],["gluten", ""],["gluten"],["gluten"], ["gluten"], ["gluten"]]
flavorProfile = [["sweet"], ["sweet"], ["sweet", "bitter"], ["sweet", "savory"], ["sweet"], ["sweet"]]

pomhoney=[]
foodNames= ["Salad", "Pita Wrap", "Grain Bowl"]
foodPrices= [7.99, 7.99, 7.99]
foodIngredients= [[""]]
foodAllergens = [[""]]
flavorProfile = [[""]]

ourfavorite=[]
foodNames= [""]
foodPrices= [6.99]
foodIngredients= [[""]]
foodAllergens = [[""]]
flavorProfile = [[""]]

# Test looper
#for i in range(len(foodNames)):
#    newItem = Food(foodNames[i], foodPrices[i], foodIngredients[i], foodAllergens[i], flavorProfile[i])
#    teaco.append(newItem)
#    print(f' Name: {newItem.name}')
#    print(f' Price: {newItem.price}')
#    print(f' Ingredients: {newItem.ingredients}')
#    print(f' Allergens: {newItem.allergens}')
#    print(f' Flavors: {newItem.flavorProfile}')
#    print("  ")


