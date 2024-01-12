# PDF Scraper
A tool by [jpacsta](https://github.com/jpacsta) for extracting data from PDF's.

## Project Structure
### `/archives`
The original scripts written by [jpacsta | github](https://github.com/jpacsta)

### `PDFScraper.py`
An encapsulated and slightly refactored version of the original scripts.

## Setup and Requirements
### Python Version
`v3.10.0`

### Requirements
```bash
# Installing a new package
pip install PACKAGE_NAME

# Updating requirements.txt
pip freeze -r requirements.txt
# Why do we do this?
#
# Because when somebody installs the project for the first time,
# They need to install all the same requirements
pip install requirements.txt
```

## Roadmap
### Configurability
- configure tool to accept path to different PDF's
- configure tool to handle different PDF's with unique instructions

### From Script -> Webapp
A script is meant to run once and be done.

To "encapsulate" the functionality of a script and put it in a webapp
(or any other environment) we can put the functionality in to a class.

Think of it as an "object" that contains the functionality of your script.
This lets us "import" the object to our webapp, and call a method to "run
the script".

We also need a web framework that handles
- listening to HTTP requests
- generating HTTP responses

Running a script from the command line might look something like this...
```bash
python script.py
```

"Running the script" from an object might look something like this...
```bash
python
```

```python
# Import the scraper
from PDFScraper import PDFScraper

# Run the scaper
PDFScraper.run(export=True)
```

### Web Framework
https://www.djangoproject.com/
- provide a minimal web interface
- handle HTTP requests

#### Development Steps
1. Install Django
2. start django project
3. define view for Form
4. build form (HTML)
5. define view to handle form submit
6. define routes to views

#### Deployment Steps
1. Configure .env library
2. Move SECRET_KEY to .env file
3. Move DEBUG to .env file
4. Provision Hosting (see [Heroku](https://www.heroku.com/python))
5. Add host to ALLOWED_HOSTS
6. Set SECRET_KEY in Heroku
7. Set DEBUG to False in Heroku
8. Define python version
9. Configure Procfile
10. Push to Heroku && deploy

### Flexibility
The script is somewhat brittle and specific to the PDF that one wants to extract data from.

We could...
- Try to make capable of handling any PDF
- Make it easy to extend to other use cases and accept the brittleness as-is
- Define a base scraper that all other scrapers inherit from