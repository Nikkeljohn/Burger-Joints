# Burger-Joints





### Site-Goals

The site is aimed to help restaurant staff to easily manage the menus displayed on the website, as well as keeping track of upcoming bookings and capacity, editing and deleting as neccessary. 

The site also aims to provide customers with a simple, hassle free way to make reservations without the need to call the restaurant. They will also be able to cancel their bookings or update when needed.

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over four weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located [here](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak/projects/1) and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

![Kanban image](docs/readme_images/kanban.PNG)

#### Epics

The project had 7 main Epics (milestones):

**EPIC 1 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

**EPIC 2 - Stand alone Pages**

The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

**EPIC 3 - Authentication Epic**

The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it the staff would not be able to managed the bookings securely without regular site visitors also being able to see and perform actions.

**EPIC 4 - Menu**

The menu epic is for all stories that relate to the creating, deleting, editing and viewing of menus. This allows for regular users to view menus and for staff to manage them with a simple UI interface.

**EPIC 5 - Booking**

The booking epic is for all stories that relate to creating, viewing, updating and deleting bookings. This allows the staff to easily view upcoming bookings, manage the bookings and also for customers to book and manage their own reservations.

**EPIC 6 - Deployment Epic**

This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

**EPIC 7 - Documentation**

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

#### User Stories

The following user stories (by epic) were completed over the 3 sprints:

**EPIC 1 - Base Setup**

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

As a developer, I need to create static resources so that images, css and javascript work on the website

As a developer, I need to set up the project so that it is ready for implementing the core features

As a developer, I need to create the footer with social media links and contact information

As a developer, I need to create the navbar so that users can navigate the website from any device

**EPIC 2 - Stand alone Pages**

As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist

As a developer, I need to implement a 500 error page to alert users when an internal server error occurs

As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views

As a restaurant owner, I would like a home page so that customers can view information on my restaurant

**EPIC 3 - Authentication Epic**

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

As a Site Owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used.

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling

**EPIC 4 - Menu**

As a staff user, I want to be able to create a new menu when we have new dishes to offer

As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant

As a staff user, I want to be able to edit a menu when updates are needed

As a staff member, I would like to receive feedback when I create or update menus so that I can see they have worked

As a staff user, I want to be able to delete a menu when it is no longer used

**EPIC 5 - Booking**

As a user, I would like to be able to create a new booking when I want to visit the restaurant

As a user, I would like to view my bookings when I need to check the information

As a user, I would like to receive feedback when I create a booking or edit one so I know it was completed successfully


**EPIC 6 - Deployment Epic**

As a developer, I need to set up whitenoise so that my static files are served in deployment

As a developer, I need to deploy the project to heroku so that it is live for customers

**EPIC 7 - Documentation**

Tasks:

* Complete readme documentation
* Complete testing documentation write up

## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality on Menus and Bookings
* Restricted role based features
* Home page with restaurant information

## The-Structure-Plane

### Features

``USER STORY - As a developer, I need to create the navbar so that users can navigate the website from any device``

Implementation:

**Navigation Menu**

 The Navigation contains links for Home, Bookings, Menus and has allauth options.

The following navigation items are available on all pages:
  * Home -> index.html - Visible to all
  * Manage Bookings -> managebookings.html - Visible to logged in users
  * New Booking -> booking.html - Visible to logged in users
  * View Menus -> menus.html - Visible to all
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](docs/readme_images/navbar.PNG)

``USER STORY - As a restaurant owner, I would like a home page so that customers can view information on my restaurant``

Implementation:

**Home Page**

The home page contains a hero image of a seaside restaurant and the restaurant information at the top of the page. This will immediately make it evident to the user, what the purpose of the website is.

Under the information section are two buttons, 'Make a booking' and 'View Menus'. These buttons will allow the user a quick way to the respective pages if they wish to make a booking or view the restaurants active menus.

The last section of the home page contains a google map, marking the location of the restaurant and the opening hours of the restaurant. This will allow the user to locate the restaurant and operating times.

![Hero Image](docs/readme_images/hero.PNG)

![Welcome Section](docs/readme_images/welcome.PNG)

![Find Us](docs/readme_images/find-us.PNG)


``USER STORY - As a developer, I need to create the footer with social media links and contact information``

Implementation:

**Footer**

A footer has been added to the bottom of the site, this contains a Twitter and Facebook link so that users can follow the restaurant on social media if they want to keep up to date with special offers not advertised on the website. These icons have aria-labels added to ensure users with assistive screen reading technology know what the purpose of the links are for. They also open in new tabs as they lead users away from the site.

![Footer](docs/readme_images/footer.PNG)

``USER STORY - As a staff user, I want to be able to create a new menu when we have new dishes to offer``

Implementation:

**Create Menu Page**

A create menu page was implemented to allow staff users to create new menus via the UI without having to use the backend admin panel. This will allow staff the ability to quickly update menus when they have made changes to the food being offered.

![Create Menu](docs/readme_images/create-menu.PNG)

``USER STORY -As a user, I would like to be able to view menus so that I can decide if I would like to dine at the restaurant``

Implementation:

**View Menu Page**

A menu page has been implemented to allow users to see the current active menus and decide whether they are interested in the food we offer before booking. This is visible to all users regardless of logged in state as it is not user friendly to restrict core information from users to force them into signing up.

![View Menus](docs/readme_images/menus.PNG)

``USER STORY -As a staff user, I want to be able to edit a menu when updates are needed``

Implementation:

**Edit Menu Page**

On the manage menus page a button was added to allow staff members to edit a menu when changes need to be made.

![Edit Menu](docs/readme_images/edit-menu.PNG)

``USER STORY -As a staff member, I would like to receive feedback when I create or update menus so that I can see they have worked``

Implementation:

**Toasts**

Custom toasts were added on successful creation and deletion of menus which display success messages to the user to enable them to see that the action completed successfully.

![Menu Toasts](docs/readme_images/toast-menu.PNG)

``USER STORY -As a staff user, I want to be able to delete a menu when it is no longer used``

Implementation:

**Delete Menu Page**

On the manage menus page, a delete button has been implemented that will take staff users to a confirmation page to allow them to delete a menu. This will allow staff to delete menus when they are no longer needed

![Delete Menu](docs/readme_images/delete-menu.PNG)

``USER-STORY - As a user, I would like to be able to create a new booking when I want to visit the restaurant``

Implementation:

**Create booking page**

A booking page was implemented with a form that takes in the customer details and enables the user to easily make a booking through the UI. 

Extensive logic was added to the form validation to ensure that not only is there a table available for the users chosen time and date but also that it has enough seats for the amount of guests. If the form is successful with validation on the front end, logic is in place to find the lowest capacity table to seat the guests for the given date and time.

This allows for seat optimisation to ensure we do not have small amounts of guests at tables that could of been booked for larger groups. Ensuring table optimisation and revenue for the restaurant.

![Create Booking](docs/readme_images/create-booking.PNG)

``USER-STORY - As a user, I would like to view my bookings when I need to check the information``

Implementation:

**Manage bookings page**

A manage bookings page was implemented with validation checks on the user. This shows all of the users bookings. This will allow the user to view their upcoming bookings when needed.

For restaurant staff users, all bookings will be available to display so that staff can easily view numbers and future bookings.

![Manage Bookings](docs/readme_images/manage-bookings.PNG)

``USER-STORY - As a user, I would like to be able to edit a booking so that I can make changes when needed``

Implementation:

**Edit Booking Page**

On the manage bookings page an edit button is present that allows the user to direct to a form and update their booking when required. This will allow the user to easily manage their own booking.

For staff users, they can also edit bookings from the manage booking page, even if they did not create the reservation. This will allow restaurant staff to ammend details as needed.

![Edit Booking](docs/readme_images/edit-booking.PNG)

``USER-STORY - As a user, I would like to receive feedback when I create a booking or edit one so I know it was completed successfully``

Implementation:

**Toasts**

Custom toasts were implemented on the successful creation and editing of bookings. This will provide feedback to the user to relay information that the booking was successfully received or updated.

![Booking Toasts](docs/readme_images/booking-toast.PNG)

``USER-STORY - As a staff user, I want to be able to search a booking by reference to save time searching``

Implementation:

**Searchbox**

A search box was added to the manage bookings page that is only visible to staff users. This will allow the staff members to easily locate a booking by reference number if they need to find it quickly.

[Search Boxes](docs/readme_images/search.PNG)

``USER-STORY - As a user I would like to delete a booking when I no longer require it``

Implementation:

**Delete Booking Page**

A delete button was added to the manage bookings page that will allow customers to delete their booking should they no longer require it without the need to call the restaurant.

For staff members, they also have the abaility to delete any booking through the UI as well. This will allow staff to free up table capacity should a customer call to cancel their booking.

![Delete Booking](docs/readme_images/delete-booking.PNG)

Favicon
    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs open.

![Favicon](docs/readme_images/favicon.PNG)

**Error Pages**

``USER STORY - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist``

Implementation:

**404 Page**

As a developer, I need to implement a 404 error page to redirect users to

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need  of the browsers back button.

``USER STORY - As a developer, I need to implement a 403 error page to alert users when accessing a page/view that they do not have permission to view``

Implementation:

**403 Page**

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete or access pages that are restricted. 

This covers:

* Create Menu - Only authorized to staff
* Edit Menu - Only authorized to staff
* Delete Menu - Only authorized to staff
* Edit Booking - Only authorized to the customer who created the booking or a staff member
* Delete booking - Only authorized to the customer who created the booking or a staff member

``USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs``

Implementation:

**500 Page**

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

**Base Setup User Stories**

The following stories were implemented in order to set up a base structure for all the HTML pages and the core installations and configurations needed to run the application. While these do not show as individual features, they were stories completed that were needed to implement all of the stories above.

``As a developer, I need to create the base.html page and structure so that other pages can reuse the layout``

``As a developer, I need to create static resources so that images, css and javascript work on the website``

``As a developer, I need to set up the project so that it is ready for implementing the core features``

**Favicon**

A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

### Features Left To Implement
- In a future release I would like to implement a page which displays a table map of the restaurant with information displayed on each table of upcoming bookings. This feature would allow staff to easily see if there are any upcoming bookings on the each table and plan accordingly. 


## The-Skeleton-Plane

### Wireframes

- Home page


![Home Page](docs/wireframes/home.JPG)


- Signup page


![Sign up Page](docs/wireframes/register.JPG)

- Log in

![Login Page](docs/wireframes/login.JPG)

- Log Out

![Logout Page](docs/wireframes/logout.JPG)

- Create Booking

![Create Booking](docs/wireframes/create_booking.JPG)
