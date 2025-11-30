#Lightweight Portfolio Website Backend

This project implements a simple backend for a personal portfolio website using Python's Flask framework. It features clean separation of concerns using Object-Oriented Programming (OOP) and persists contact form submissions using TinyDB, a lightweight JSON-based database.


#Features

RESTful Routes: Simple routes for Home, Portfolio, and Contact pages.

OOP Data Model: Uses Python dataclasses (objekts.py) to define the Contact model.

Data Persistence: Contact form submissions are saved to a file (db.json) using TinyDB.

API Endpoint: An /api/contacts endpoint to fetch all stored contact submissions in JSON format.

Form Handling: Handles POST requests from the contact form and validates inputs.


#Installation

Prerequisites

Python 3.8+

pip (Python package installer)


#Setup Steps

Clone the repository or download the files:

git clone [your-repo-link]
cd [your-project-directory]


Install dependencies:
You will need Flask and tinydb.

pip install Flask tinydb


Ensure required templates are present:
The application expects the following files in a templates/ subdirectory:

index.html

portfolio.html

contact.html (Must contain the form posting to the /submit route)


#Usage Guide

1.Run the Flask application:

Open your terminal in the project directory and execute the main application file:

python contact.py


The console will display the running URL (e.g., http://127.0.0.1:5000/).

2.Access the Website:

Open your web browser and navigate to the application URL.

3.Test the Contact Form:

Go to /contact.

Fill out the form fields (Name, Email, Message).

Click "Send Message".

You should be redirected back to the /contact page with a success message.

4.Verify Data Storage:

A new file named db.json will be created in your project directory containing the submitted contact data.

5.Access the API:

To view all stored contacts, navigate to the API endpoint:
http://127.0.0.1:5000/api/contacts
