

Program live link: The app has succesfully been deployed and can be viewed on <a href="https://grocerystore1-74caed983ca3.herokuapp.com/">Heroku</a>


---

## Contents
[Overview](#overview)
* Usage Scenario

[Features](#features)
* Display Program Introduction

[Testing](#testing)
* User Stories Testing

[Validation and Version Control](#validation-and-version-control)

[Bugs and Known issues](#bugs-and-known-issues)
* Bugs
* Known Issues


[Deployment](#deployment)


[Technologies Used](#technologies-used)


[Credits](#credits)

[Acknowledgement](#acknowledgement)

---

## Overview

<a href="https://grocerystore1-74caed983ca3.herokuapp.com/">Welcome to the Local Grocery Store</a>

This app is a data-driven Python program . The aim is to boost efficiency in the store for shoppers, allowing users to shop for items needed and self-checkout.

#### Usage Scenario
This app will be used in a grocery store where you can add the needed items in your cart, where you will be updated with price for each items added to your cart.
You can also select the total amount you want of certain items or wants to remove certain items from your cart, it will update those prices too.
At the you can self-checout by simply exiting the program where the app will show your subtotal.



## UX
The program flow is clear and asks the user for minimal information with minimal text. The program is designed to be simple to use and easy for the user to update the inventory.

## User Stories
### User goals:

* Add a new item you want to add to your cart.
* Continue shopping
* Remove items from your cart
* Your total

## Design Process

### Main Function:

 My initial goal for this project was to have 1 columns on items. As it will made user experience bad I decided to add a two seperate columns of items will price tags for each item.
Also added function where user can be updated with their current condition of their cart.
 Added a function where if user wants to remove items from their cart they can remove number of items to that of total item added.

 
### Flowchart for design process 
![Lucidchart](/images/lucidchart.png)
</details>

## Features
This section will cover how and why each step in the program is included. The below will have screenshots in chronological order of output. Starting with the correct inputs for: item name, quantity, remove item. The validation messages will be shown in the validation testing section, found in the TESTING.md.

### Display Program Introduction:

On program start, the user will be presented with the list of shop items and option to add a item to shopping cart, add item or "exit" shopping. 

![intro](/images/home.png)

#### Quantity:
Once user decides the item to add in cart than program will ask for quantity of items.
The quantity of item is set to 100 maximum per item for program running smoothly.

![Quantity](/images/quantity.png)

#### User Cart:
Once the item and quantity both is added then the program will display users cart to update the price of items and reminder.
And once again program will ask if user wants to continue shopping on not.

![Cart](/images/cart.png)

#### Remove item from cart:

If the user wants to remove items from the shopping carts the program will ask for name of item user wants to reomove from their cart.

![Remove item](/images/reomve.png)

#### Quantity of items user wants to remove form cart:

Once user decides which item they want to remove now program will ask for the quantity of items user wants to remove.
The items quantity cannot be more than added quantity and less than 0.

![Remove item quantity](/images/removeqnt.png)

#### User sub-total:

At the end if user no more wants to shop and wants to exit , users can end the shopping loop and the program will print out tha subtotal of all items.

![Sub-total](/images/total.png)




## Testing

## Validation and Version Control

By following best practice guidelines throughout development, my code has fully
passed through the [CI Python Linter](https://pep8ci.herokuapp.com/) with no errors found.
This can be verified by pasting the 'run.py' file through the CI Python Linter link:

![PEP8 Validator](/images/pythonlinter.png)

## Bugs and Known issues
### Bugs
Testing was done thorough during development as different bugs came up. Issues as follows:
* Remove item quantity was accepying negative inputs 
* Sub-total was also printing in negative values
* Incorrect user inputs breaking the code

*All issues that were found and fixed before final deployment.*

### Known issues
There are no issues that have been found and are unresolved.

## Deployment
The program was hosted on Heroku due to its ability to handle dynamic content.
I integrated my code with the CI Python template to create the 'mock-terminal' feature seen on the live site.
This feature enables users to engage directly with the code, similar to executing the run.py file in an IDE.

Deploying this project involved multiple steps, which are more intricate compared to deploying from GitHub Pages.
By adhering to these steps sequentially, you can deploy the application to the web:

1. Generate a list of requirements for Heroku. These are the dependencies used in the Gitpod VS Code workspace.
To generate, ensure there is a requirements.txt file in your project root.
Then enter pip3 freeze > requirements.txt into your terminal.
This will build a list of dependencies that Heroku will use to build the project.

2. Login or Sign up 

3. Ensure that your account is set up correctly and your Eco Dynos plan is active in Heroku

4. Select 'Create new app' from your Heroku Dashboard.

5. Create a unique name for your app and select your region. Select 'Create app'.

8. Select 'Add buildpack'. Add the following buildpack in order.
These can be re-ordered by drag-and-drop if needed.
    1. heroku/python
    2. heroku/nodejs

9. In the "Deploy" tab. Under 'Deployment method', select 'GitHub' and proceed to follow the prompts to establish a connection.

10. When the correct repo is located, select 'Connect'.

11. Finally, under "Manual deploy", select the correct branch and click 'Deploy Branch'.
A build log will begin running. A link will be provided to the site after this process.

12. Click the "View" button to view the deployed app.

## Technologies Used
[Code Institute Python Template](https://github.com/Code-Institute-Org/python-essentials-template)
\- This formed the foundation for the project, which integrated with the CI mock
terminal that the project is presented in


Deployment Platform: [Heroku](https://www.heroku.com/)

Flowchart Editor: [Lucidchart](https://www.lucidchart.com/pages/templates/login-or-sign-up-page-wireframe)

Language: Python 3.8.11

Python Libraries - latest versions imported and installed from terminal:


## Future Ideas

Future ideas I have had for this project are as follows:
1. Create a user account to hold user info for futher purchases.
2. Create different sales depending on season or holidays sales for item.
3. Add a feature to accept coupons or clubcards for shop.

## Credits
Sites used:
1. [CI Python Linter](https://pep8ci.herokuapp.com/)
2. [Youtube](https://www.youtube.com/watch?v=kbyHLU9JqjE)

## Acknowledgement
 Massive thank you to my mentor, Adegbenga Adeye, for helping me figuring out to debug and providing feedback on my code
