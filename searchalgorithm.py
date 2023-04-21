import math


#Note valuecase does matter KEEP EVERYTHING LOWERCASE WHEN CREATING RESTAURANT FOOD LISTS

#Default argument is userSavedFavorites, a List containing dictionaries of favorited food items
# in [{'name': '<foodnamestring>', 'restaurantName' : '<restaurantnamestring>'}]
def food_recommendation(restaurant, minprice, maxprice, userPreferredIngredients,
                        userAllergens, userTastePreferences,userSavedFavorites=[],restaurantName=''):
    #uses restaurant object to produce list
    restaurantFoodList = restaurant.foodList
    #edited list for foods of a selected restaurant that doesn't have allergens
    restaurantFoodListEdited = []
    if "none" not in userAllergens:
    #1) filter restaurant foods based on allergens
        for eachFoodItem in restaurantFoodList:
            noAllergens = False
            for eachAllergen in eachFoodItem.allergens:
                if eachAllergen in userAllergens:
                    noAllergens = True
            if noAllergens == False:
                restaurantFoodListEdited.append(eachFoodItem)
    else:
        restaurantFoodListEdited = restaurantFoodList
    #re-edits restaurantFoodListEdited to remove all favorited Food items
    for eachFavoritedFoodItem in userSavedFavorites:
        for eachFoodItem in restaurantFoodListEdited:
            if (eachFavoritedFoodItem.get('name') == eachFoodItem.name) and (eachFavoritedFoodItem.get('restaurantName') == restaurantName):
                restaurantFoodListEdited.remove(eachFoodItem)
    #Test to evaluate edited list with items that have matching allergens removed
    #for eachItem in restaurantFoodListEdited:
    #    print(eachItem.name)
    if "none" in userPreferredIngredients:
        userPreferredIngredients =[]
    if "none" in userTastePreferences:
        userTastePreferences = []

    #2) Update individual food item's score based on ingredients that match 
    for eachFoodItem in restaurantFoodListEdited:
        #Recommendation Score variable
        foodRecommendationScore = 0.0
        for eachIngredient in eachFoodItem.ingredients:
            if eachIngredient in userPreferredIngredients:
                foodRecommendationScore += 0.5
    #3) Update individual food item's score based on flavor profile
        for eachFlavor in eachFoodItem.flavorProfile:
                if eachFlavor in userTastePreferences:
                    foodRecommendationScore += 1
    #4) Update individual food item's score based on price range +2 if in range
        if eachFoodItem.price <= maxprice and eachFoodItem.price >= minprice:
            foodRecommendationScore += 2
    #   +1 if the food item is less than maxprice but not in minimum range ie cheaper than budget
        elif eachFoodItem.price <= maxprice:
            foodRecommendationScore += 1.5
        else:
            #average distance calculates the average between the max/min and the larger the gap
            #between the food item's price and the median score the lower the score is added
            avgDistance = 1/( .001 + abs(((minprice + maxprice)/2) - eachFoodItem.price))
            foodRecommendationScore += avgDistance
            # truncates to two decimal places
            if foodRecommendationScore > 10:
                foodRecommendationScore = 10
            foodRecommendationScore = math.floor(foodRecommendationScore * (10 ** 2)) / (10 ** 2)

        eachFoodItem.recommendationScore = foodRecommendationScore
        #If food recommendation score > 1 then food item has more in common beyond  price range and can be added
#        if foodRecommendationScore > 1:
#            userReccomendationList.append(UserRecommendedFoods(eachFoodItem.name, foodRecommendationScore, restaurant.restaurantName))
        
    #filter results according from largest to smallest score
    restaurantFoodListEdited.sort(key=lambda x: x.recommendationScore, reverse=True)

    #TEST FOR RESULTS
#    for eachitem in restaurantFoodListEdited:
#        print(f'Food name: {eachitem.name} Score: {eachitem.recommendationScore} Parent List: {restaurant.restaurantName}')
    
    #Note this is used to quickly find the recommended items of a restaurant
    #sorted from largest dishScore to smallest DishScore
    # do I need to jasonify?
    # needs to be stored in database
    return restaurantFoodListEdited

def calculateRecommendationMasterList(userRestaurantMasterList, minBudget, maxBudget,
                                      userPrefIngred, userTastes, userAllergens, userFavoriteFoodsList=[]):
    for eachRestaurant in userRestaurantMasterList:
        #calculate for each sublist the appropriate recommendation ist
        sortedRecommendationsIndividualRestaurantList = food_recommendation(eachRestaurant, minBudget, maxBudget,
                                                             userPrefIngred, userAllergens,userTastes, userFavoriteFoodsList, 
                                                             eachRestaurant)
        eachRestaurant.foodList = sortedRecommendationsIndividualRestaurantList
    return userRestaurantMasterList

# Needs another argument that is defaulted to FALSE, if FALSE returns that specific restaurant result
# if TRue returns the largest result  
# To DO: Figure out how to get images                                   
def stringToArray(stringToParse):
    lowercaseString = stringToParse.lower()
    lowercaseString = lowercaseString.strip()
    convertedList = lowercaseString.split(', ')
    return convertedList

def stringToArrayNoLower(stringToParse):
    stringToParse = stringToParse.strip()
    convertedList = stringToParse.split(', ')
    return convertedList






#Note - maybe user recommended list needs to be a linked list


################################## MODEL DEFINITION #########################################################################
#user Recommendation Food Items used in database stored list
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


######################################### RUNNABLE TEST CODE ###############################################################################
food_list = []
foodnames = ["Grilled Chicken" , "Spaghetti Carbonara", "Veggie Stir Fry", "Steak Fajitas", "Shrimp Scampi"]
foodprice = [12.99, 15.99, 10.99, 18.99, 20.99]
foodingredients = [["chicken", "olive oil", "salt", "pepper", "garlic"], ["spaghetti", "bacon", "eggs", "parmesan cheese", "black pepper"],
["broccoli", "carrots", "mushrooms", "onion", "garlic", "soy sauce"], ["steak", "bell pepper", "onion", "garlic", "cumin", "chili powder"],
["shrimp", "butter", "garlic", "white wine", "lemon", "parsley"]]
foodallergens = [["chicken"], ["eggs", "dairy"], ["mushrooms"], [""], ["shrimp"]]
flavorprofile = [["savory", "salty"], ["savory"], ["crunchy"], ["salty", "spicy"], ["savory"]]


for i in range(5):
    newItem = Food(foodnames[i], foodprice[i], foodingredients[i], foodallergens[i], flavorprofile[i])
    food_list.append(newItem)
restaurant = Restaurant("Ginos Italian", food_list, "123 Coding way")
userAllergens = ["gluten", "dairy", "shrimp"]
userTastePreferences = ["salty", "spicy"]
userMaxPrice= 15
userMinPrice = 10
userPreferredIngredients = ["garlic", "onion"]

food_recommendation(restaurant, userMinPrice, userMaxPrice, userPreferredIngredients, userAllergens, userTastePreferences)

