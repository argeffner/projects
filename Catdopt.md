## Catdopt

Catdopt is capstone designed as a project for the springboard software engineering track website. You can access the website by clicking 
[here](www/) (currently website is having issues with heroku I will fix in the future)  


### Purpose
This app emulates a cat adoption website. It gives the user the feeling a new experience where individual gets to name the cat of choice and cats are randomly presented per a selection of breed.

### Features
The app includes: 

- User accounts
	- hashed password stored into database with bcrypt
- Cat data base
	-  each user can name cat
	-  multiple tabless with ability to delete cat from database (and option to delete username).
- A nice User Interface 
  - [Bootstrap 4](https://getbootstrap.com) toolkit used to design UI
	- all selected cats have appealing card container
	- Search bar includes breed selection list
	- nice button icons from [google icons](https://fonts.google.com/icons)
	- navigation bar with different options for users and non users.

### Design
-  utilizes an API, in this case fetching a foreign API, stores data in the database and/or as a session.
- Utilizes back end routes for sending data to the app
- [PostgreSQL](https://postgresql.org) is the database managment system used for storing data
- Uses SQL and [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) to create classes and tables for storing data
- Creating a dynamic front end with multiple page routes.
- Utilizing forms with validation and application of bcrypt for user privacy and security with [WTForms](https://flask-wtf.readthedocs.io/en/stable/).

### Setup & Independant use
To try out this app in your own server and tinker with the code. Feel free to download the requirements.txt file to start playing with and editing the app. Don't forget to use a database management system (I recommend Postgress, but there are many options).

-
I would also like to thank [Springboard](https://springboard.com) and Ted Ly for providing the advice and knowledge neccessary for building this app. 

I will come back and improve the app in the near future. And if anyone has some sort of advice or suggestion to impove this app please feel free to drop a message to: <argeffner@gmail.com>