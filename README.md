# Django Review Processing API

This Django project provides an API for uploading and processing review data from CSV files. The processed data is stored in a database and can be accessed via RESTful endpoints.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)

## Requirements

- Python 3.8+
- Django REST framework
- pandas

## Installation

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   
2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    venv\Scripts\activate

3. **Install dependencies**:

    ```sh
    pip install django djangorestframework pandas
    
## **Running the Project**

    ```sh
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver

## API Endpoints

1.**File Upload**
    URL: /api/upload/
    Method: POST
    Description: Upload a CSV file containing review data. The file will be processed and the data will be stored in the database.

2.**Review Data**
    URL: /api/reviews/
    Method: GET
    Description: Retrieve all processed review data.

## Testing the API
1.**Upload Data**:

  Use Postman or another tool to send a POST request to http://127.0.0.1:8000/api/upload/ with the CSV file.

2.**Retrieve Data**:

  Send a GET request to http://127.0.0.1:8000/api/reviews/ to retrieve the processed data.
