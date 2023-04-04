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

#will hold all restaurants
masterListRestaurants = []



# Rules
# restaurant list names must equal query string on main page
# restaurant ingredients and info all lowercase
# acceptable allergens: dairy, eggs, fish, shellfish, tree nuts, peanuts, gluten, soybeans, mustard, cinnamin, (possibly other spices NOT HERBS, NOT SALT, NOT PEPPER< NOT POTATOES)
# tastes: sweet, salty, sour, bitter, and savory
#list objects for absurdbird creation
absurdbird = []
foodNamesAbsurdBird = ["3 chicken tender basket", "4 chicken tender basket", "5 chicken tender basket", "tender slider", "snack box", "fried oreo", "mac and cheese", "fries" ]
foodPriceAbsurdBird = [5.99, 6.99, 7.99, 2.99, 4.99, 2.99, 2.19, 2.99]
foodIngredientsAbsurdBird = [["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"], ["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"],
["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"], ["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"],
["chicken", "flour", "buttermilk", "cider vinegar", "garlic", "mustard", "dill", "red pepper", "potatoes"], ["oreos", "pancake mix", "oil"], ["cheese", "cheese sauce", "pasta"], ["potatoes"]]
foodAllergensAbsurdBird = ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chicken", "gluten", "dairy", "mustard"], ["chocolate", "sugar"], ["dairy", "gluten"], ["flour", "potatoes"]
flavorProfileAbsurdBird = [["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["savory", "salty"], ["sweet"], ["savory"], ["salty"]]

burger512 = []
foodNames =["korean flame", "blue mushroom", "guadalupe burger", "hays co burger", "the classic", "fiesta fries", "firebird fries", "disco fries", "fries", "chicken strips"]
foodPrices=[7.99, 7.99, 7.99, 7.99, 6.99, 6.19, 5.69, 4.69, 2.19, 5.99]
foodIngredients =[[]]
foodAllergens = []
flavorProfile = [["savory", "salty", "spicy"],["savory", "salty"]], ["savory", "salty"], ["savory", "sweet", "salty"], ["savory", "salty"], ["salty", "savory"], 
# Test looper
for i in range(len(foodAllergensAbsurdBird)):
    newItem = Food(foodNamesAbsurdBird[i], foodPriceAbsurdBird[i], foodIngredientsAbsurdBird[i], foodAllergensAbsurdBird[i], flavorProfileAbsurdBird[i])
    absurdbird.append(newItem)
    print(f' Name: {newItem.name}')
    print(f' Price: {newItem.price}')
    print(f' Ingredients: {newItem.ingredients}')
    print(f' Allergens: {newItem.allergens}')
    print(f' Flavors: {newItem.flavorProfile}')
    print("  ")


