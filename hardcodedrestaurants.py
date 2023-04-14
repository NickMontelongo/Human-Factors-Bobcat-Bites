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


