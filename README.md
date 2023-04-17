# Human-Factors-Bobcat-Bites
Bobcat Bites food recommendation website

#MAJOR TODOS --updated 4/14/2023
#1) Hard Code all Restaurants EASY- BUT TEDIOUS Being Worked On
#2) TEST TEST TEST
#3) correct value amounts to $x.00 instead of $x.0


NOTE ON #1)
Need to take pictures of places on campus
-KOLBY AND WILLIAM ARE ON THIS



NEXT UPDATE 
LAST CONCRETE UPDATE
Due: 4/??/2023
QUALITY OF LIFE UPDATES
- Messages implemented for user interaction
    Blue for errors
    Green for Successes  xx done
- Needs to be tested fully
- Needs to have all restaurant images put in image file
- All restaurants need to be hardcoded
- Bug fixes

QUALITY OF LIFE IMPROVEMENTS TO CONSIDER (AS OF 4/16/2023)
1) Modify image sizes so uniform not stretched/distorted/ugly NEEDS TO BE DONE
2) Resize search bar to be larger (maybe not worried about)
3) Have some form of distinction betweeen pages ie 
    redirect links that indicate previous page to current page example:
    <recommendbysearch main page>/<searchResults (currentPage)>
4) Implement a x/5 stars user review button (maybe done by me idk)
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
