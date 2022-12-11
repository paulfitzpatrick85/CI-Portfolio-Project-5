

----------------------------------------------------------------------

# BluePrint WebDesigns

BluePrint WebDesigns is an online service for users to purchase four different levels of web development packages to help run there business. These range from simple sites for advertising services to full e-commerce/online shopping websites. User can browse the site owners existing body of work, purchase the available packages, and also leave reviews.


You can view the live site here ----deployed link-----

-----am i responsive image-------

## User Storys
+ Github UserStories URL: https://github.com/users/paulfitzpatrick85/projects/11?add_cards_query=is%3Aopen

+ As a user I want to register for an account with the website.
+ As a user I want to see my logged in or logged out status.
+ As a user I want to view all products.
+ As a user I want to be able to filter products by the criteria I choose.
+ As a user I want to add products to my cart.
+ As a user I want to be able to edit and update the contents in my cart.
+ As a user I want to be able to delete the contents in my cart.
+ As a user I want the ability to contact the site owner through a form where I can attach my details.
+ As a user I want to add review/testimonial 



## How To Use The Website
 When a user visits the page, they can navigate to the menu in the top of the page where they can browse product packages, past work in 'our work' and the reviews page.
+ Full screen

![nav](https://user-images.githubusercontent.com/55660566/201520038-5d497ab3-9042-4cc3-86bc-ae1475bd9849.png)

 + Mobile view

 ![mob nav](https://user-images.githubusercontent.com/55660566/201520036-9dd3d778-36fd-44d7-b65e-9a24acb03120.png)

The user can choose to sign in if they have an account, or sign up if they have yet to, by clicking on account/person icon.

![acc](https://user-images.githubusercontent.com/55660566/201520232-049b0f73-b5d1-4e44-b115-7f2f8878c544.png)

![sign in](https://user-images.githubusercontent.com/55660566/201520235-232b72d6-9c18-4ba0-8276-a745e6f00f28.png)


If the user chooses to register for an account they are presented with a form where they must provide a user name, an email - which will be used to match them to the reviews they have left in order to allow them to edit a previously added review, or delete it if the so choose, and lastly a password. If the user already has an account, the option to login is built into the form to save the user returning to the home page to select login from the menu, and vice versa, that if a use trys to login without an account the option to navigate to the register page is also in the login form.

![reg](https://user-images.githubusercontent.com/55660566/201520234-9aa35f3c-c8f3-4e5d-83a9-713eb78e3d24.png)


*I have setup profiles under two fictitious users for testing the 'review' CRUD functionality

The details should they be needed are as follows:
1. email: 'paulf@gmail.com', username: 'paulf', password: 'passpfpf'

+ username: testuser2, email: user2@gmail.com, password: testpassword2

+ Admin/superuser details: username: ------------, email: fitzer99@gmail.com, password: ----------------

Once the user has registered, a message is displayed to the user informing them they have successfully logged in, this same message appears for all user login's.

![log in message](https://user-images.githubusercontent.com/55660566/201520769-78038b33-4d84-4c00-a938-fe08ded6e80b.png)

A similar message is displayed when the user logs out.

![log out message](https://user-images.githubusercontent.com/55660566/201520770-45977f3f-66af-40c9-a5ad-f330da84da8c.png)


The user's login status is displayed in the drop down menu when the account icon is clicked

![login status](https://user-images.githubusercontent.com/55660566/201520866-fc1d7311-29f5-46f8-96a1-f681161c3966.png)


# Full CRUD Fuctionality - Reviews
When the user is logged in and navigates to the 'reviews' page, if no reviews have been left yet, a message is displayed saying 'There are no reviews to display just now', this message is removed once a review is added and approved.
The link/button to add a review does not display if a user is not logged in.

![add review-logged in](https://user-images.githubusercontent.com/55660566/201521214-e6029cbd-5242-4375-ac83-e541f9f2aefe.png)

![no review- not logged in](https://user-images.githubusercontent.com/55660566/201521216-9af5f763-b2bb-4cdd-ab02-0499e9dbf30c.png)


Once the user clicks the 'add review' button, they are brought to another page to fill out the review form, all fields are required to be filled.


![review form 1](https://user-images.githubusercontent.com/55660566/201521467-bfd5837b-d275-4917-bace-3d97050dcb17.png)


When the user has finished filling out the form and the 'submit' button is clicked, the form is submitted for approval by the admin and the user is shown a message telling them their form must be reviewed before it is displayed on the reviews page. To prevent a duplicate form being submitted on refresh of the page, the user is prompted to click a link in the message which is simply an empty anchor tag with an empty href, when clicked the message disappears and if the user should eventually refresh the page, the form is not re-submitted.

![add review message](https://user-images.githubusercontent.com/55660566/201521465-057bddbe-7f74-4643-ba4f-9d325a3c9e88.png)

In the Admin panel, accessed by adding '/admin' to the end of the home page url, eg. 'https://------------.herokuapp.com/admin' and once logged in as the admin/superuser, the admin can by navigate to the 'reviews' tab  on the left to view the details added in the submitted form. If all details are found to be okay to be displayed on the site, the admin can change the review's status by checking the 'review approved' check box, and then clicking 'save'.

![admin review approve](https://user-images.githubusercontent.com/55660566/201521666-186f3373-4cec-43ef-af6b-28c2dadae7b8.png)


On return to the webpage, the review is now displayed on the reviews page, and if logged in as user who left the review, two buttons, 'edit review' and 'delete review' will be displayed under the review text.

![review buttons](https://user-images.githubusercontent.com/55660566/201521891-342b4e60-c190-4bfa-a7be-2b1175607e19.png)

Note if a user is not logged in, the buttons are not displayed.

![no review button-not logged in](https://user-images.githubusercontent.com/55660566/201522489-cc693112-bbe7-4ed0-80f5-558e761b8962.png)


To edit a review, only the user who wrote the review can use the 'edit review' button which will bring them to a new page where they can see a form prepopulated with the information they originally inputted.

![edit review pre-pop](https://user-images.githubusercontent.com/55660566/201522485-65438073-a84e-44c0-84e4-ac191aedcd14.png)


The user can then change one or all fields as required, not all are required as before. (in this example the text just being shortened.)

![edit form edited](https://user-images.githubusercontent.com/55660566/185779332-d4e5c9fe-61b9-41b5-b9bc-4284b92072b0.png)

Once the user is finished making changes and clicks 'edit review', the form is submitted and a message is displayed to the user informing them their details have been edited and they should return to the reviews page.

![review edited message](https://user-images.githubusercontent.com/55660566/201522496-bcb5eb76-a90f-4292-a37a-a6a37a06bc19.png)

Once back in the Reviews page, the user can see the updated review.

![edited review](https://user-images.githubusercontent.com/55660566/201522488-418fb8fa-4901-471c-b59c-1b1ecd306a0d.png)

If the user chooses to delete their review, they can click the 'delete review' button beneath their review.
upon clicking the button, a modal will open asking the user 'Are you sure you want to delete this review?' The user can then either cancel the action by clicking cancel or proceed with the deletion and click 'delete'.

![delete modal](https://user-images.githubusercontent.com/55660566/187296690-69238cd4-16e8-4cb7-a12b-d347852a56f2.png)

When the review is confirmed for deletion in the modal, a message is displayed informing the user the review has been deleted.

![review deleted message](https://user-images.githubusercontent.com/55660566/201522493-cb50b1a7-791e-4ab2-a31d-d1bb34b1de05.png)

### Authentication
If a another user is logged in, and trys to edit the review left by 'paulf' in this case, a message is displayed telling the user this is not thier review to edit.

![not your to edit message](https://user-images.githubusercontent.com/55660566/201522490-1f9c17b0-bdd3-4b5f-b892-d8fd75c0c2d4.png)

The same applies when another user trys to delete a review left by someone else, the delete modal will open as the first 'delete review' button is only a link to the modal, but if the 'delete review' button is clicked inside the modal to confirm deletion, no deletion will occur and a message will be displayed to tell the user that the review is not theirs to delete.

![not yours to delete message](https://user-images.githubusercontent.com/55660566/201522492-f03cae0d-5b8f-4c4b-a51a-6f198981ff2e.png)

## Our Work Page
Visitors to the site can view an exisiting body of work without the need to register or be signed in.
The Our Work page displays images and info from the projects model in the 'ourwork' app.
Users can view a large thumbnail of the home page of one of eight sites, each with a short description of the sites purpose, the coding languages used, and a link to the site itself.

![ourwork](https://user-images.githubusercontent.com/55660566/205742427-1359dd40-df3a-4e28-beb7-04f577ef8ff5.png)


## Contact and NewsLetter Sign Up Form

Users can contact the site owner using the form on the 'Get In Touch' page. A user can fill in a short form: name, email and message in order to both subscribe to the sites newsletter and to enquire about potential collaboration.

![contact](https://user-images.githubusercontent.com/55660566/205743232-f5f1e3e7-8ed5-445e-8db5-76b3e2ff6fe6.png)

## Packages Page
The Packages pages provides details of the products/web-dev packages available for purchase, the information is delivered to the site through the package model in /admin rather than a json file as used in the walkthrough project Boutique Ado. Users will see four different packages, each with their own unique title to somewhat describe them at a glance, along with a short description, the price excluding tax.

![placeholder](https://user-images.githubusercontent.com/55660566/205745295-52af91b8-5cbf-4a15-8cb7-468e0f1c4516.jpg)----package page

Clicking a package title or image will bring the user to the package detail page where a longer and more in depth description is displayed along with two buttons giving the option to add the package to their cart or return to the packages page.

![placeholder](https://user-images.githubusercontent.com/55660566/205745295-52af91b8-5cbf-4a15-8cb7-468e0f1c4516.jpg) ---package detail

If the user adds the item to their cart, a message will appear inform them the item is now in their cart.

![added to cart](https://user-images.githubusercontent.com/55660566/205747826-c832986a-a43b-4c32-9c76-37bcabe0f03b.png)

Given the nature of the product/packages for purchase, a user should have no reason to purchase more than one of the same tier package, so an attempt to add the same item twice, a message will be displayed informing the customer the package is already in their cart and it will not be added again.

![already in cart](https://user-images.githubusercontent.com/55660566/205747827-55f97605-2bc9-4e7c-bc8b-38550a9ff615.png)

If a user who is not registered or logged in navigates to the packages page, the button to add to cart will not be displayed. In its place the button will display text to the user that they must register/log in to add items, the button will bring the user to the sign in page.

![log in to add item](https://user-images.githubusercontent.com/55660566/205748228-c44ccc48-93dc-4823-af8a-d724bc8027f8.png)



## Cart and Checkout Pages

To view user cart and its items, the user will navigate to the account icon at the top right of the page. If the user has no items added to the cart, the space at the bottom of the dropdown will appear blank, but when hovered over the amount/price of the users cart will be displayed.

![empty cart not hovered](https://user-images.githubusercontent.com/55660566/205751620-f29377d3-3237-4988-b307-ea793e6da313.png)

![empty cart  hover](https://user-images.githubusercontent.com/55660566/205751629-1f2d488c-bc9e-4b68-9a44-2806808ed12d.png)

And when the cart does have items added the carts price will display in the dropdown without the need to hover over.

![item in cart dropdown](https://user-images.githubusercontent.com/55660566/205751934-9847d015-6d39-42e1-b971-9cc1149156a0.png)

The cart page, once items are added will display the chosen package title and its price, and the option to remove the item.
A breakdown of the amount to be paid is shown above the 'proceed to payment' button.

![cart](https://user-images.githubusercontent.com/55660566/205752861-06ff8401-6589-46f8-84ca-5804d065b132.png)

If the user should remove all items in their cart, the page will display to the user that the cart is empty and a button to return to packages is made available.

![cart emptied](https://user-images.githubusercontent.com/55660566/205752859-ac5b559f-e814-4617-9f5c-71812addaf87.png)

If an admin is logged in, an extra option will be available in the dropdown to access the admin panel in a new window.

![dropdown admin option](https://user-images.githubusercontent.com/55660566/206844061-9c0e5d77-a46e-4210-94ff-1b40df2c2b62.png)


If the user choses to proceed with payment they are taken to the checkout page, where are require to fill out a short form consisting of name, email, phonenumber which are required, and postcode along with a text area to input their credit card details.

![checkout1](https://user-images.githubusercontent.com/55660566/206849837-8e7c1fe5-2bb0-48df-8382-9cf078f9f23b.png)


## User Story Testing

+ The site is made and layed out in a way that is easy to use and does not bombard the user with too many or needless details. 
+ Registering for an account with the website in easy and login/ log out status and messages are displayed cleary and the user is made aware they are logged in or out by clciking the account icon
+ Packages available to purchase along with their price and other details are displayed in a clear manner.
+ Users can add and remove packages from their cart easily.
+ Users can sign up to a news letter and attached a message to the site owner.
+ Users Can leave reviews of the service, which can later be edited or deleted.


## Bugs
Webhooks are not used as I continued to get an 404 error telling me the url checkout/wh/ could not be found. I ran this problem through two tutors and my mentor and still could not solve the issue.


## Code Validation
### Files for PEP8 validation checked through http://pep8online.com/
All files passed without errors, with some only displaying a warning of 'no new line at end of file', which when a new line is added only creates new warnings of 'blank line at end of file', the other warning being 'trailing whitespace', which for some reason in only a few files, which I 'backspace' the whitespace, the warning would not clear, so the files where left with these warnings.

Any other warnings that occured in individual files are mentioned below their image.





## HTML validation

HTML validated at https://validator.w3.org/



The above url (https://ci-pp4-unsigned-ireland.herokuapp.com/Instrumental/) tests the same code for /metal, /rock, /pop etc.

## CSS validation
Css validated with jigsaw W3C CSS Validator




## Javascript validation 
validated at https://jshint.com/

![js test](https://user-images.githubusercontent.com/55660566/187523340-c8a9f252-327e-43f3-af4b-33efffac2efc.png)

## Accessibility
I tested the sites accessibility through lighthouse

--lighthouse image---


## Responsiveness
The site is designed to be used on devices as small as 300px.

## Mockup Images

![mockup home](https://user-images.githubusercontent.com/55660566/193449720-0c2cd888-724e-4bbf-b7d4-088bd518a727.jpg)

![mockup products page](https://user-images.githubusercontent.com/55660566/193449675-9247bc33-49d0-4df7-aad0-3c25b6f1c03d.jpg)

![mockup review](https://user-images.githubusercontent.com/55660566/193449676-9c6acc80-9711-48ce-b37a-7bba0ed90dc1.jpg)

![mockup contact page](https://user-images.githubusercontent.com/55660566/193449680-d73b0359-d56c-482e-bdca-2fde3bc1ee22.jpg)


## Credits
+ checkout models - most of code take from b/a project but changed slightly
signals.py taken from b/a
checkout/forms - taken from b/a
stripe elements.js code - b/a
checkout success - bs used from b/a
webhook handler.py
webhooks.py - though most is stripes own code




## Deployment 
To deploy the project:
+ In settings.py I set DEBUG to 'False' and added the code "X_FRAME_OPTIONS = 'SAMEORIGIN'"
+ I then pushed my work to github in the the gitpod terminal using the commands: 'git add .', git commit -m "commit message"', 'git push'.
+ In heroku settings I removed the config variable 'DISABLE_COLLECTSTATIC'
+ In the heroku deploy tab I connected my github repository for the project to the heroku app.
+ I enabled automatic deploys then clicked 'deploy branch' to build the live app.