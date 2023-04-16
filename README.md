# Human-Factors-Bobcat-Bites
Bobcat Bites food recommendation website

#MAJOR TODOS --updated 4/14/2023
#1) Hard Code all Restaurants EASY- BUT TEDIOUS Being Worked On
#2) TEST TEST TEST
#3) Implement Messages EASY


NOTE ON #1)
Need to take pictures of places on campus
-KOLBY AND WILLIAM ARE ON THIS

NOTE ON #3) 
This should be easy MOST (not all) of the flashing messages are encoded in the groupapp.py file
and technically just need the appropriate code to display on the html side, need to
google how but should only require basic functionality
Flashing Messages should occur:
1) when user has cycled through all results in (recommend by restaurant) and will be reloaded x
2) when user is adding to their favorites, the item is added
3) when user is resetting information in (recommend by restaurant)
4) when the profile has been updated? x --Done
--NICK IS WORKING ON SHOULD FINISH 4/17/2023
Data Log 4/12/2023

NEXT UPDATE 
LAST CONCRETE UPDATE
Due: 4/??/2023
QUALITY OF LIFE UPDATES
- Messages implemented for user interaction
    Blue for errors
    Green for Successes
- Needs to be tested fully
- Needs to have all restaurant images put in image file
- All restaurants need to be hardcoded
- Connect image routes to automatically display images (easy)
- Make sure flash messages are implemented appropriately
- Bug fixes
- Make sure Works with and without Recommendations
- Links and error messages easy to see

QUALITY OF LIFE IMPROVEMENTS TO CONSIDER (AS OF 4/16/2023)
1) Modify image sizes so uniform not stretched/distorted/ugly
2) Make sure the website looks normal on mobile devices and is easily accessible
3) Make sure blue->error messages green->success messages
4) change the color of the redirect links (ex on title, login pages to be more noticable)
5) Resize search bar to be larger
6) Have some form of distinction betweeen pages ie 
    redirect links that indicate previous page to current page example:
    <recommendbysearch main page>/<searchResults (currentPage)>
7) Implement a x/5 stars user review button (maybe done by me idk)
(Any more can be discussed)

FUTURE IMPROVEMENTS
- Technically the master list with recommendations is the same as the initial restaurant
master list that was imported just updated with a recommendation score because of this that
means that the master list of recommended foods is always sorted (since no item is deleted)
and is the re-edited master list because of this that means instead of evaluating each restaurant
in the master list for restaurant search we can just directly index ie Absurd bird is first so
masterListRecommendation[0] so on and so forth making it possible to actually utilize the best of arrays

-Comments could be added showcasing all user's using the apps comments on a food item

-Probably should implement the entire master restaurant list into a database since recommendation 
score is being modified and thusly if multiple users access the site there runs the possibility
of data racing and corruption of recommendation score information

-CSS can be cleaned up along with style sheets
