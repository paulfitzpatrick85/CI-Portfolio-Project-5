

----------------------------------------------------------------------

# BluePrint WebDesigns

BluePrint WebDesigns is an online service for users to purchase four different levels of web development packages to help run there business. These range from simple sites for advertising services to full e-commerce/online shopping websites. User can browse the site owners existing body of work, purchase the available packages, and also leave reviews.


You can view the live site here ----deployed link-----

![amiresponsive](https://user-images.githubusercontent.com/55660566/206925022-9e51cb4f-fe6c-43de-ac24-3c089ac3887a.png)


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


If the user choses to proceed with payment they are taken to the checkout page, where are require to fill out a short form consisting of name, email, phone number which are required, and postcode along with a text area to input their credit card details, testing the payment functionality is done using the number '4242424242424242 42/42 424 2424'.

![checkout1](https://user-images.githubusercontent.com/55660566/206849837-8e7c1fe5-2bb0-48df-8382-9cf078f9f23b.png)

When the payment is processed, the user is brought to the checkout success page which displays and order summary including their order number.


![checkout success page](https://user-images.githubusercontent.com/55660566/207132810-061e41ab-4e8a-4bc7-88c3-120b4c3b99ff.png)


A message is also displayed temporarily informing the user the order was taken successfully.

![order message](https://user-images.githubusercontent.com/55660566/207132767-0250f03a-46cf-4b74-8f9c-f3c0ee357a32.png)

Should the processing of an order fail, a message is displayed to the user informing them.

![process error](https://user-images.githubusercontent.com/55660566/207133580-9c8093de-77b8-48d2-8efd-c2573d5d8421.png)


When the card number '4000002500003155 42/42 424 2424' is used the follow authentication model is displayed to the user to authenticate their order payment.

![auth modal](https://user-images.githubusercontent.com/55660566/207136021-0c127919-ef1b-4fa1-88fd-6f04eab9044b.png)

### Custom 404 Page
If a user should enter a url that does not exist as part of the site they will be directed to a custom 404 page, whichs displays the text 'Its Looks Like You're Looking For A Page That Doesn't Exist' along with a button/link back to the packages page.

![404](https://user-images.githubusercontent.com/55660566/207146141-51cc2b0d-4490-4295-9c04-60f1b4c3de15.png)


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
### Files for PEP8 validation checked through code institues own checker - https://pep8ci.herokuapp.com/
All files passed without errors, with some only displaying a warning of 'no new line at end of file', which when a new line is added only creates new warnings in the terminal of 'blank line at end of file', the other warnings being 'trailing whitespace', which for some reason in only a few files, which I 'backspace' the whitespace, the warning would not clear, so the files where left with these warnings.

+ CART APP

apps.py

![cart apps](https://user-images.githubusercontent.com/55660566/207112880-19ee4fba-5666-4a2e-8494-b54d968fedd4.png)

contexts.py

![cart contexts](https://user-images.githubusercontent.com/55660566/207112881-1f619f0e-db3e-463a-afc9-ed4edacfa61e.png)

![cart context](https://user-images.githubusercontent.com/55660566/207112019-bf2c8f11-2bf9-4875-a579-f963894fde3b.png)

urls.py

![cart urls](https://user-images.githubusercontent.com/55660566/207112023-a44c5be6-5ccf-4a0e-8501-abe4f502926c.png)

views.py

![cart view](https://user-images.githubusercontent.com/55660566/207112025-939fe339-2c90-460b-90ce-53dcb5b9afb3.png)

+ CHECKOUT APP

admin.py

![checkout admin](https://user-images.githubusercontent.com/55660566/207113636-4bbac11d-c94f-4489-ac85-667555f8c0a6.png)

apps.py

![checkout app](https://user-images.githubusercontent.com/55660566/207113657-f9e11011-0dfb-4cbd-8bf5-ab9080fc4977.png)

forms.py

![checkout forms](https://user-images.githubusercontent.com/55660566/207115170-77e42b53-bfd0-4e66-b95c-23028a220faf.png)

signals.py

![checkout signals](https://user-images.githubusercontent.com/55660566/207115174-e845f972-627c-4715-970f-aae723a6b4dd.png)

urls.py

![checkout urls](https://user-images.githubusercontent.com/55660566/207115177-240b4214-1e22-4fd5-abaf-01bab1828ab6.png)

views.py

![checkout views](https://user-images.githubusercontent.com/55660566/207115179-f6779f14-a5ee-44ee-ba9f-a6f640587ba4.png)

+ HOME APP

admin.py

![home admin](https://user-images.githubusercontent.com/55660566/207117538-04f453e9-c164-4941-a3b7-7e4a83ba9991.png)

apps.py

![home apps](https://user-images.githubusercontent.com/55660566/207117543-7f1a7314-b6a7-4a2c-9be3-17e38ca4fadc.png)

models.py

![home models](https://user-images.githubusercontent.com/55660566/207117544-f38498e6-3e97-4bef-a6a0-8c3edacdc474.png)

urls.py

![home urls](https://user-images.githubusercontent.com/55660566/207117546-73a37b51-3550-4f10-b36a-321153a8de39.png)

views.py

![home views](https://user-images.githubusercontent.com/55660566/207117547-1a9104f3-b0eb-44bf-8c71-ed1edea56008.png)

forms.py

![homoe forms](https://user-images.githubusercontent.com/55660566/207117549-c3776bdd-2cf6-4bef-b190-e8bbf32ecfff.png)

+ OURWORK APP

admin.py

![ow admin](https://user-images.githubusercontent.com/55660566/207119387-8258d190-c790-4e03-8c56-9fa73f56c42b.png)

apps.py

![ow apps](https://user-images.githubusercontent.com/55660566/207119390-4a55dcac-edef-4b41-b305-e4bec9385313.png)

models.py

![ow models](https://user-images.githubusercontent.com/55660566/207119392-65df8538-429f-469c-87a5-b9ad101d7b75.png)

urls.py

![ow urls](https://user-images.githubusercontent.com/55660566/207119393-924d0d17-8cab-4de8-986e-3540b9230dc9.png)

views.py

![ow views](https://user-images.githubusercontent.com/55660566/207119397-1ba9490d-2a3c-44d1-811e-12ecf8efcc09.png)


+ PACKAGES APP

admin.py

![p admin](https://user-images.githubusercontent.com/55660566/207122572-f746e067-46ab-4f3d-8bf9-575691b03d8b.png)

apps.py

![p apps](https://user-images.githubusercontent.com/55660566/207122576-981bc908-67f4-48a9-bb53-318ecd48da13.png)

models.py

![p models](https://user-images.githubusercontent.com/55660566/207122577-dc7e5210-dacc-4d82-9a63-9d82080abf1c.png)

urls.py

![p urls](https://user-images.githubusercontent.com/55660566/207122580-48478fa5-e829-49c2-a8ea-35238b1c26b4.png)

views.py

![p views](https://user-images.githubusercontent.com/55660566/207122582-99dceb9a-29de-4caf-9466-2d8043a25a0d.png)

+ REVIEW APP

admin.py

![r admin](https://user-images.githubusercontent.com/55660566/207128015-3abc19b4-e90b-4c63-b89c-21f3e749a9df.png)

apps.py

![r apps](https://user-images.githubusercontent.com/55660566/207128019-7c3adf0d-b780-432a-83ac-8075faebb932.png)

forms.py

![r forms](https://user-images.githubusercontent.com/55660566/207128021-36c1a7e0-c19b-4f9e-829c-b8ce6748f904.png)

models.py

![r models](https://user-images.githubusercontent.com/55660566/207128024-1831fdc2-8777-46d1-bbad-db7566451725.png)

urls.py

![r urls](https://user-images.githubusercontent.com/55660566/207128025-13da6714-de90-449a-92bb-70dc3a74dce8.png)

views.py

![r view](https://user-images.githubusercontent.com/55660566/207128471-cb85d99b-2990-4896-9c08-8f1a5547ccdb.png)

Checkout/models.py is the only file which an error shows in the terminal for a 'line too long' even after the line is split, when passed through CI's checker, the error is not picked up so the code is left as is. 

![checkout models ci linter](https://user-images.githubusercontent.com/55660566/207109911-02d9cd88-7877-4191-91bd-d00d569dfa42.png)
![checkout models](https://user-images.githubusercontent.com/55660566/207109916-c15d626a-1715-4428-8625-eeeb57d69465.png)

settings.py shows error for 'line too long' but these are the 'AUTH_PASSWORD_VALIDATORS', which I was told by tutors/leads on slack that as it's not our(students) own code this can be ignored.


## HTML validation

HTML validated at https://validator.w3.org/

All pages passed without errors.

![cart](https://user-images.githubusercontent.com/55660566/206921739-0570bdc5-82d6-4db8-a054-cb097b364a41.png)
![checkout](https://user-images.githubusercontent.com/55660566/206921741-e7221424-5b06-4e17-941f-02775f58e51e.png)
![checkout_success_payment_made](https://user-images.githubusercontent.com/55660566/206921742-6134eafa-24d3-49a0-8920-bebf0e50e6bf.png)
![homepage](https://user-images.githubusercontent.com/55660566/206921743-a010687b-9fcc-40db-bd4c-7eff506208c1.png)
![packages](https://user-images.githubusercontent.com/55660566/206921745-0b263727-33c9-41eb-9709-5a8a9e7cbc20.png)
![projects](https://user-images.githubusercontent.com/55660566/206921747-3597fc8b-87da-406d-be44-a01d780ff30e.png)
![reviews](https://user-images.githubusercontent.com/55660566/206921748-e9215dad-1a8f-436b-b005-069100a51363.png)
![subscribe](https://user-images.githubusercontent.com/55660566/206921749-247f7f4d-2256-409a-9d83-f770adca5e19.png)



## CSS validation
Css validated with jigsaw W3C CSS Validator

css checked through direct input with no errors

![val css](https://user-images.githubusercontent.com/55660566/206921806-0973a366-e01b-4935-991f-10579fae7289.png)



## Javascript validation 
validated at https://jshint.com/

Javascript files passed with only warnings relating to es6, which I was told by mentor during pp4, are ok to have.

![js](https://user-images.githubusercontent.com/55660566/206922122-e94430eb-dda8-4f2a-ac24-c2b7d76403e6.png)
![js-stripe](https://user-images.githubusercontent.com/55660566/206922125-ce11441f-09d3-43e4-ba12-54c2e3dbb2df.png)

## SEO

I used wordtracker.com to help choose the most relevant keywords for my site the were low competition but relatively high volume. 
Some examples of changes made to existing text in order to use relevant keywords include;
+ webdesign - added to the index h1 and packages h2
+ Grow Business Online - later added to the reviews page
+ Online Business - added to packages h3
+ best website builder for small business - implented to pacakes h3
+ and I also used google's suggestions after searching some the keywords myself.

Also some keywords where wrapped in 'strong' tags where they where not previously.
In socials links in the footer the 'rel' attribute was added as 'rel="noopener"'in order to tell search engines not to include the links when looking at the search engine ranking.
'Webdesign' was added to the alt attributes of the carosel from the index page, as opposed to the original 'first slide, second slide' etc.

I also added to the root folder, a sitemap.xml created and downloaded from www.xml-sitemaps.com  

To control search engine bot crawling, I added a robots.txt file, disallowing crawling of the accounts, cart and checkout pages.









## Accessibility
I tested the sites accessibility and SEO score through lighthouse.

![lighthouse](https://user-images.githubusercontent.com/55660566/206921804-0c9d10ea-e08a-4ffa-9321-b0f028756fe3.png)


## Responsiveness
The site is designed to be used on devices as small as 320px.

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





## Deployment 
To deploy the project:
+ In settings.py I set DEBUG to 'False' and added the code "X_FRAME_OPTIONS = 'SAMEORIGIN'"
+ I then pushed my work to github in the the gitpod terminal using the commands: 'git add .', git commit -m "commit message"', 'git push'.
+ In heroku settings I removed the config variable 'DISABLE_COLLECTSTATIC'
+ In the heroku deploy tab I connected my github repository for the project to the heroku app.
+ I enabled automatic deploys then clicked 'deploy branch' to build the live app.