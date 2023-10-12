# Description
My website allspices.com is a online website that will allow user to browse recipes of different categories, see the details about them like ingredients and method to cook also user can publish their own recipe and write reviews on others recipes. This website have a Favourite section where user can add their favourite recipe.

## Technologies
* Python
* Django
* JavaScript
* HTML
* CSS

## Project details
* Allow user to login, logout and register.
* Show all recipes.
* Filter recipes by category.
* Show recipe details including their ingredients, method, comments or reviews they have.
* Add recipes to Favourites.
* Create own recipes.
## Models
#### User- This model is used for user profile as user can save their information and log in with it.
#### Recipe- This model contain main fields for recipe like ingredient, title, category, description and owner.
#### Favourite- This model have fields for save a specific recipe of user’s choice. User field are related to User model by foreign key.
#### Comment- This model have a comment field for comments made by users. Also user and recipe are related to recipe and user models by foreign key.
# Web pages
## Navigation bar
Customer can see all recipes, categories and if the user is logged in they can see their favourite recipes.
## Homepage
This is the landing page of the website. All recipes are displayed here.
## Log in page
If a user is not authenticated, a link for log in is shown on the navigation bar. Users can log in using the form on the log in page
## Log out page
When a user is authenticated, a log out link is shown on the navigation bar instead of log in link. When an authenticated user clicks on that link, he/she is logged out.
## Register page
If you are a new user you can register by clicking on register link on navigation bar.
## Viewing Favourites
User can see all the favourite recipe they added. When user click on any recipe listed in favourite, he/she directed to the page where they see the details of recipe.User can add their favourite recipe by clicking on 'Add to favourites' link on detais page of recipe.
## Details page
This page is about the details of the recipe including their ingredients, method, chef or owner. User can add their review at bottom in comment section also can add their recipe to favourite section by clicking the link 'Add to favourite'.
## Create
New recipe can be added using create page. User can access this page by simply clicking on it ‘Create’ on navigation bar. (User should be logged in).
## Finally
I'd like to thank all the people who made this great CS50's Web Programming with Python and JavaScript course possible and also thank you to Brian Yu for his fluency and easy-to-understand lectures.
