# Appbuilder9000

The purpose of this repository is for presentation of the first of two live projects of a two-week duration completed during the duration of my time whilst attending [The Tech 
Academy Software Developer Bootcamp](https://www.learncodinganywhere.com/codingbootcamps), based in Portland, Oregon and is a subsidiary of © Prosper Consulting Inc.


##Dependencies:

* [Windows 10 OS](https://www.microsoft.com/en-us/software-download/)
* [Python 3.9 64-Bit](https://)
* [HTML5](https://www.microsoft.com/en-us/p/html5-css-php-javascript/9nblggh08ltm?activetab=pivot:overviewtab)
* [CSS](https://www.microsoft.com/en-us/software-download/)
* [JavaScript](https://www.microsoft.com/en-us/software-download/)
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/download/)
* [PIP](https://pip.pypa.io/en/stable/installation/)
* [Pycharm Community Edition 2021.2.1](https://)
* [Django Rest Framework 3.11.0](https://)


## Overview

The Tech Academy created a Django-based based multi-application simulation website that would essentially serve as a landing page to which a user could navigate to multiple sites each of which would be built around a specific topic of each team member's choosing.  My application for this project was based on the topic of inline speed skating, a hobby with which I have participated since my youth.  The end product for the application would be a Django Rest Framework in Python. 

Requirements for this assignment included development of the site made up of the following: 

* Database collection manager
* Restful API inteface
* Data Scraping with Beautiful Soup

Working on multi-application project was a tremendous learning experience on many levels.

Stepping into a project that was already underway was (in my view) about as "real-world" of an experience as I can imagine to prepare me for my future roles in software developement.

Below are descriptions of the stories I worked on, along with code snippets and navigation links. I also have some full code files in this repo for the larger functionalities I implemented.  Please note, during the time that this project was ongoing, I experienced some personal challenges that impacted my ability to complete as many project stories as I had intended upon inception of the project.  However, I have attempted to provide perspective as it concerns the manner in which I approach and execute relative to the work that I produce. 

### Back End Stories

* Create The Model
* Edit and Delete Functions
* Parse Through HTML
* Connect to API

#### Create The Model: Story consisted of creating the collection model and migration, including an objects manager for accessing the database, creation of a model form including any inputs the user needs to make, addition of a template to the app for creation of new items, addition of a views function that renders the create page and utilizes the model form to save the collection item to the database, verification that item saved to database without errors, and add styling as needed.

#### Edit and Delete Functions: Story consisted of addition of edit page to templates, use of models and forms to display content of a single item from database, sending of views function to send the information for the single item and save any changes, include option to delete an item with confirmation, and add styling as needed. 

#### Parse Through HTML: Story consisted of getting objects out of Beautiful Soup object, send just the values as relevent dictionary objects to the template, display all items within the data scrape template, testing and error handling, linking of data scraping page to the app's home page, and add styling as needed.

#### Connect to API: Story consisted of creation of a new API template and render within a function, connect to API and write a basic JSON response, create a way to search specific terms through the API, getting all data for the search, and commenting of which elements from the JSON response for the desired value.


### Front End Stories
* Display All Items from Database
* Build the Basic App
* Details Page

#### Display All Items from Database: Story consisted of creation of a new HTML page and link it from my home page, add a function that gets all items fromthe database with some or all fields for the item displayed with labels/headers, and add styling as needed.

#### Build the Basic App: Story consisted of creation of a new app using manage.py startapp, registration of app from within [MainProject]>[MainProject]>settings.py, creation of base and home templates, addition of a function to views to render the home page, registration of urls with mainapp and create urls.py for my app and home page, and linking of the app's home page to the project's home page, addition of an image link on the project home page, and addition of minimal content some basic styling to base and home.  Must include least a navbar,  background, title, and footer.

#### Details Page: Story consisted of addition of a details template folder and register url pattern, creation of a views function to find a single item from the database and send it to the template, addition of a link on the *display all items* page that directs to the details page for that item, display details of the item on the details page, and add styling as needed.


## Additional Thoughts

Finally, utilizing a DevOps project management methodologies, incorporating Scrum task tracking, and Agile Boards was such a different experience from other projects I have participated that were not of a software development nature as it concerns.  I am astounded at the the effectiveness of these methods as it concerns efficiency, task management, accuracy and so on.  They are extremely powerful and I am very excited to venture into an industry that takes such a methodical and contrived approach to the work that I will do in the coming years. 

## Links: 
* GitHub: <https://github.com/EChristian74>
* LinkedIn: <https://www.linkedin.com/in/christianmethodical/>
* Email: <christianmethodical@gmail.com>

Jump to: [Dependencies](#dependencies), [Introduction](#introduction), [Features](#features), [Back End Stories](#back), [Front Back Stories](#front), [Additional Thougnts](#additional). [Page Top](#appbuilder9000)





