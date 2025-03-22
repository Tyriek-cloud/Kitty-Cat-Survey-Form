# Kitty Cat Survey Form
<img width="383" alt="image" src="https://github.com/user-attachments/assets/e36898e6-3e0f-435e-baec-65580a373f38" />

This is a full-stack web application designed to collect user responses to a survey. The survey was designed to gather sentiments and opinions about domestic cats. The survey currently has the following features:

1. Two multiple choice questions pertaining to dog and cat breeds.
2. A series of drop-down menus to record responses.
3. The option for users to leave comments/inquiries.
4. A display at the bottom that will (eventually) show the most common user demographics.
5. The survey loads all its data into a PostgreSQL database. Said database is hosted on Supabase.

# Technologies Used to Build this Application
There were a series of different technologies that were used to build this web application:

*Programming & Scripting Languages*
This application used the following languages in its creation:

1. Python
2. JavaScript
3. HTML
4. CSS

*Libraries*
There were a series of libraries that were initiated in the "requirements.txt." file in the repository. The libraries include the following:

1. Flask version 3.1.0
2. Psycopg2 version 2.9.10
3. Flask_sqlalchemy version 3.1.1
4. Pandas version 2.2.3

*Hosting Services*
This application was built using the following free services:

1. Vercel: For website hosting.
2. Supabase: For a web version of the database.

I used the following SQL script to create the initial table to store user responses in the database:

<img width="179" alt="image" src="https://github.com/user-attachments/assets/91e2f54f-d693-4b1f-8c49-6003bd4b7c07" />

# Notes
This application is a recreation of an old application that I made several years ago. A link to that application can be found here: https://codepen.io/tyriek-cloud/full/jOMjxzL
Additionally, this application is somewhat of a work in progress. There are currently not enough users to display the average user demographics at the bottom of the application. As the number of visitors to the website continues to grow, so too will the numerical displays at the bottom of the website.
