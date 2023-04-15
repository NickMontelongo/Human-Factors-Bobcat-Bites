# Human-Factors-Bobcat-Bites
Bobcat Bites food recommendation website

#MAJOR TODOS --updated 4/14/2023
#1) Connect User favorited profile and connect search results to individual food items
#2) Hard Code all Restaurants EASY- BUT TEDIOUS Being Worked On
#3) TEST TEST TEST
#4) Implement Flashing Messages EASY

NOTE ON #1)
-NEED to Connect Individual item results
-Why do variables switch?
-Guards for lack of results

NOTE ON #2)
Need to take pictures of places on campus

NOTE ON #4) 
This should be easy MOST (not all) of the flashing messages are encoded in the groupapp.py file
and technically just need the appropriate code to display on the html side, need to
google how but should only require basic functionality
Flashing Messages should occur:
1) when user has cycled through all results in (recommend by restaurant) and will be reloaded x
2) when user is adding to their favorites, the item is added
3) when user is resetting information in (recommend by restaurant)
4) when the profile has been updated? x
Data Log 4/12/2023

NEXT UPDATE 
DUE: 4/15/2023?
IMPLEMENT USER FAVORITING SYSTEM
NEEDS TO DO:
- Link search query results to the individual results page
- Produce messages to the user (#4)
- Edit search algorithm to exclude favorite items saved by user (possibly implement a dictionary?)
- Write a loading function that sets every single food item to exist in Database
- Figure out how to pull food item and restaurant item from database
- Page Populates all results

LAST CONCRETE UPDATE
Due: 4/??/2023
QUALITY OF LIFE UPDATES
- Needs to be tested fully
- Needs to have all restaurant images put in image file
- All restaurants need to be hardcoded
- Connect image routes to automatically display images (easy)
- Make sure flash messages are implemented appropriately
- Bug fixes
- Make sure Works with and without Recommendations
- Links and error messages easy to see


FUTURE IMPROVEMENTS
- Technically the master list with recommendations is the same as the initial restaurant
master list that was imported just updated with a recommendation score because of this that
means that the master list of recommended foods is always sorted (since no item is deleted)
and is the re-edited master list because of this that means instead of evaluating each restaurant
in the master list for restaurant search we can just directly index ie Absurd bird is first so
masterListRecommendation[0] so on and so forth making it possible to actually utilize the best of arrays

-Comments could be added

-CSS can be cleaned up along with style sheets
