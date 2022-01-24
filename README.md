# Chocolate Factory
## **Code Institute - Portfolio Project 5: _E-commerce Application_** 
Chocolate Factory is an django e-commerce web app inspired by the Willy Wonka Franchise. 

This web app will allow users to explore the fond memories of their childhood and purchase the products they have always dreamed of!
## Demo

[View the Live Website Here](###############)

<img src="###############">


## Table of contents
+ [User Experience](#User-Experience)
     + [Project Goals](#Project-Goals)
     + [User Stories](#User-Stories)
     + [Strategy](#Strategy)
     + [Scope](#Scope)
     + [Structure](#Structure)
          + [Front end Pages](Front-end-Pages)
     + [Skeleton](#Skeleton)
          + [Wireframes](#Wireframes)
     + [Surface](#Surface)
+ [Features](#Features) 
     + [Existing Features](#Existing-Features)
     + [Features to Implement in the future](#Features-to-Implement-in-the-future)
+ [Database](#Database)
+ [Technologies Used](#Technologies-Used)
     + [General Resources](#General-Resources)
     + [Tools](#Tools)
+ [Testing](#Testing) ☞ **[Testing.md](TESTING.md)**
+ [Deployment](#Deployment)
     + [Heroku Deployment](#Heroku-Deployment)
     + [Forking the Repository](#Forking-the-Repository)
     + [Making a Local Clone](#Making-a-Local-Clone)
+ [Credits](#Credits)

***
# User Experience
## Project Goals
The primary goal of Chocolate Factory is to enable users to purchase Wonka inspired products through an fully functional ecommerce website. The goal for the design was to make it as easy as possible to access information, while striving for a minimalist and user-friendly layout without compromising on aesthetic!

## User Stories

As a Site User I want to be able to view posts by paginated listso that I can easily navigate posts
As a Site Admin I want to be able to approve or disapprove commentsso that I can filter out objectionable comments
As a Site Admin I want to be able to create draft postsso that I can finish writing the content later
As a Site Admin I want to be able to create, read, update and delete posts so that I can manage my blog content
As a Site User I want to be able to like or unlike a postso that I can interact with the content
As a Site User I want to be able to leave comments on a postso that I can be involved in the conversation
As a Site User I want to be able to register an accounso that I can comment and like
As a Site User / Admin I want to be able to view comments on an individual postso that I can read the conversation
As a Site User / Admin I want to be able to view the number of likes on each post so that I can see which is the most popular or viral
As a Site User I want to be able to click on a post so that I can read the full text
As a Site User I want to be able to view a list of postsso that I can select one to read
As a Store owner I want to be able to delete a product so that I can remove items that are no longer for sale.
As a store owner I want to be able to edit/update a product so that I can change product prices, descriptions, images and other product 
As a store owner I want to be able to add a product so that I can add new items to my store
As a shopper I want to be able to receive an email confirmation after checking out so that I can keep confirmation of what I’ve purchased for my records.
As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes
As a shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
As a shopper I want to be able to easily enter my payment information so that I can checkout quickly and with no hasslesAs a shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout
As a shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout
As a shopper I want to be able to view items in my bag to be purchasedso that I can identify the total cost of my purchase and all items I will receive
As a shopper I want to be able to view items in my bag to be purchasedso that I can identify the total cost of my purchase and all items I will receive
As a shopper I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase
As a shopper I want to be able to sort multiple categories of product's simultaneously so that I can find the best-priced or best-rated products across broad categories such as chocolate or hard candy
As a shopper I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specified category or sort the products in that category by name


[^ back to top ^](#Table-of-contents)
<br>

## Strategy
### — Project Planning —

Agile Development was used to plan the project. This was implemented using a kanban board in github issues and projects. 

The functionalities below are minimum requirements for the website to achieve the user's goals. 

<br>

[^ back to top ^](#Table-of-contents)
<br>


## Scope

To achieve user and owner’s goals, above are the minimum features to be included in this project. Also, **CRUD** Create, Read, Update, and Delete functions are required for this project so these are implemented as a part of the essential features.

- 3 Custom Django Models
- Ability to implement CRUD in products for site admin
- Register page where users can create an account.
- Sign in and sign out page where users can sign into and out of their accounts.
- Home Page
- Profile page 
- Product Management page 
- Search 
- 404 page that appears for invalid URL and takes users back to *Home* page of the website safely

> **Note:**<br>
> 

## Structure

The entire web app has the same menu and footer. 

The menu has the following navigation links:
- Title leads to Home Page
- All products button opens up a drop down menu that allows users to view products by price, category, rating or alternativly all the prodcuts. 
- Candy button opens up a drop down menu that allows users to view candy products by category 
- Merchandise button takes users to merchandise products page
- Updates button takes users to updates page
- Search bar which enables users to search for products
- My account button opens up a drop down menu that allows users to log out, view their profile or manage products depending on  
- Bag button takes users to the shopping bag page


The footer has the following navigation links:
- Basic newsletter sign up form powered by mailchimp
- Facebook icon that takes the user to Chocolate Factory Facebook Page
- Contact us button takes user to contact form
- Git hub icon and name takes user to developers github profile. 


The main pages of the website are:

- Homepage(index.html) - Which takes users to all products page through explore button
- All products page(products.html) - Which renders all products in store and enables users to sort products by price, rating, name or category and navigate to individual product pages
- Product page(product_detail.html) - Which renders a view a specific product, its reviews and it enables the user to add products to bag, navigate back to All products page or depending on user status, leave a review or edit/delete product. 
- Bag page(bag.html) - Renders the contents of the users bag, enbales the user to adjust products and product quantity, also enables users to return to all products page through keep shopping button or to check out. 
- Checkout page(checkout.html) - Allows users to adjust bag by redirecting back to bag page and allows users to input delivery information and securely checkout. 
- Updates page(index.html) - Enables users to view updates in blog format and and to navigate to individual updates. 
- Profile page(profile.html) - Enables users to edit their delivery information and view past orders.
<br>

[^ back to top ^](#Table-of-contents)
<br>


## Skeleton

### Wireframes

Input wireframes


## Surface

— **Colour** —

The colors for the webapp were used in inspiration of the purple and yellow theme in the Wonka franchise whilst keeping accesibility and contrast rules in mind. 
<br>
insert color palette 
[^ back to top ^](#Table-of-contents)
<br>



# FEATURES

## Existing Features 
#### **Navigation menu displayed across all pages**

Navigation menu
Search bar
Website Title that redirects to home page
A bag icon that reflects total amount in bag
Product management tool for site admin to implement CRUD functionality
Ability to pay securely through STRIPE
Contact Form
Updates page in blog style
Ability to review products and comment on update posts
Ability to sign in, sign out and register
Ability to view past orders and input default delivery information
    

## Features to Implement in the future 
A golden raffle ticket
A wonka inspired quiz
A wonka inspired playlist that users can play whilst shopping
Ability to edit and delete reviews 
Ability to edit and delete updates posts.
A wishlist

[^ back to top ^](#Table-of-contents)
<br>


# Database

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. 
Amazon Web Services is used for the hosting of all media and static files. 
<br>
The database contains three custom models - review, comment/post and contact. 

![database](##################)<br>

###

# Technologies Used

- [Django3](https://www.djangoproject.com/) framework
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Postgressql](https://www.postgresql.org/) for the database
- [Bootstrap 4 ](https://mdbootstrap.com/) for bulk of CSS
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [JQUERY](https://jquery.com/) for interaction
- [Python3](https://www.python.org/) as a backend 
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Amazon AWS](https://aws.amazon.com/) for image and static files hosting
- [Summernote](https://summernote.org/) editor for adding and editing updates
- [Gitpod](https://www.gitpod.io/) for cloud IDE
- [Git](https://git-scm.com/) for source control
- [GitHub](https://github.com/) for file and documents hosting
- [Heroku](https://www.heroku.com/) for website deployment
- [STRIPE](https://stripe.com/) for payments


## Resources used in project

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)
- [Twilio](https://www.twilio.com/)
- [Gmail](https://www.gmail.com/)


## Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Pixlr](https://pixlr.com/e/) for resizing images
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

***

<br>

[^ back to top ^](#Table-of-contents)
<br>

# Testing
The entirety of the testing was done manually. 

# Deployment
## Heroku Deployment
This project was deployed through Heroku in the following steps:

1) A repository was created in github using the student template
2) The repo was pushed to the cloud based IDE called GITPOD
3) In the GITPOD terminal, django and its supporting libraries were installed using pip3
4) The project is then created using using python3 manage.py startproject <project name>
5) The first app is then created using python3 manage.py createapp <app name>
6) The app is then registered in the setting file in the project level settings.py. 
7) An app is the created in heroku and the installation of postgres is done under resources making sure to add postgres url to config vars
8) Back in the GITPOD terminal, install Django Database and psycopg2
9) Import dj database url in your settings file and replace default database with dj database passing it postgres url
10) Migrate database and load data in gitpod terminal 
11) Create another super user
12) Create an if else statement that checks the database url and runs the correct database accordingly. 
13) Install gunicorn, create a procfile and log into heroku in the terminal. 
14) Disable the static files using heroku config:set, DISABLE_COLLECTSTATIC=1 --app <appname>
15) Add heroku app and localhost to allowed hosts in settings.py
16) Generate a secret key using Django secret key generator and add to config vars whilst linking it to settings.py
16) Add, commit and push changes to Github
17) Set heroku to automatically deploy but setting it to Github and searching/connecting to correct repo. 

<br>
[^ back to top ^](#Table-of-contents)
<br>

# Credits
### Code
* The Code Institute material was the main source of information used to create this project.
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [Twilio](https://getbootstrap.com/) for their contact form tutorial which was adapted to create mine
* [Code With Stein](https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg) for his ecommerce django tutorial which I adapted for my reviews model.
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [w3schools](https://www.w3schools.com/) was used as a general source of knowledge 
* [youtube](https://www.youtube.com/) 
* [Stack Overflow](https://stackoverflow.com/) 
* [MDN Web Docs](https://developer.mozilla.org/) for various tutorials and walkthroughs!
* [Django Docs](https://docs.djangoproject.com/en/3.2/) for django documentation.
* [Github Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) and (https://www.youtube.com/watch?v=3SKjPppM_DU) was used to create the 404 page.


### Media



### Acknowledgements
* I would like to thank the Slack Community, especially the women in my cohort, who went above and beyond to help me! 
* I would like to thank Kasia our class cohort facilitator for her tireless assistance and support! 
* I would like to thank my mentor Chris for his support, guidance and feedback
* I would like to also thank all my family, friends and associates who have supported me during the making of this project!
 
***
