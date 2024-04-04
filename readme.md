# Flask Web Service

This is a simple Flask web service that provides an endpoint for downloading a data file (`data.csv`). It also includes a Swagger UI page for API documentation and testing.

## Deployment URL's

Deployment is done using (https://render.com/) a free cloud hosting platform for web apps
 1. Web Interface- https://nrc-t3.onrender.com/
 2. Swagger UI for Testing - https://nrc-t3.onrender.com/apidocs/
 3. Direct API - https://nrc-t3.onrender.com/download

 ## Github URL
 - https://github.com/paramCAD/nrc_T3

 ## Dependencies
 - Python (3.11.3)
 - pip (22.3.1)

## Installation Locally

1. Clone the repository to your local machine:
 
git clone https://github.com/paramCAD/nrc_T3

cd .\nrc_T3\flask_app\

2. Install the required dependencies:

pip install -r requirements.txt


## Usage

### Running the Flask Application

To run the Flask application, execute the following command:

python app.py

The application will start running on http://localhost:5000 by default.

### Accessing the Swagger UI

Once the Flask application is running, you can access the Swagger UI page by navigating to:

http://localhost:5000/apidocs

The Swagger UI page provides documentation for the `/download` endpoint and allows you to test it interactively.

### Testing the `/download` Endpoint

To test the `/download` endpoint programmatically, you can use the tester module. Follow below steps:

1. Ensure that the Flask application is running.
2. Open a terminal.
3. Navigate to the repository directory.
    - Command: cd .\nrc_T3\tester_module\
4. Run the tester module by executing the following command:
    - Command: python tester.py

This will download the `data.csv` file and save it as `downloaded_file.csv` in your current directory.

Alternatively, you can use the provided HTML interface to test the endpoint by opening `index.html` in a web browser.



