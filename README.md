# Django Scrapper API
Hi! This project was created to fullfil recruitment task, which was mainly focused on creating web-scrapper using Django. My main goal was to scrape information from given URL, such as title, content and publication date. 
Those information are stored in PostgreSQL database and are exposed with REST API created with Django REST Framework.

# Features
- Extract HTML content, title and publication date using Playwright, BeautifulSoup, Trafilatura and HtmlDate
- Verification of duplicating elements
- Data contained in PostgreSQL database
- Endpoints expose data by Django REST Framework 
- Easy launching scrapping process using management command
- Filtering records by source domain

# Requirements
- Python 3.12.3
- Django 5.2.7
- Django REST Framework 3.16.1
- PostgreSQL
- BeautifulSoup
- Playwright
- Tdqm
- Trafilatura
- HtmlDate
- Dateparser
All packages installed are available in `requirements.txt`

# Install Guide
In order to use this scrapper, you have to clone this repository using: 

`git clone https://github.com/kacperPiech/Django-Scrapper.git`

To use this app, you have to download package from `requirements.txt` into your virtual environment. Therefore, you should apply those commands:

`python -m venv venv`
`source venv/bin/activate`

To finally install packages, you should use the following command:

`pip install -r requirements.txt`

To set up the database, you should set your environmental variables like in `.env.examples`. You should also remember to give proper permission to your `.pgpass` file. In case of any issues, visiting `https://docs.djangoproject.com/en/5.2/ref/databases/#postgresql-notes` could be helpful.

To verify your configuration, you have to make migrations:

`python manage.py makemigrations`
`python manage.py migrate`

Finally if everything went well, you can run server by:

`python manage.py runserver`

# Management Command

To start scrapping automatically, you could use following command:

`python manage.py scrape_articles`

If you would like to test it on different urls, you should modify `scrape_articles` file by putting your own url to `url_to_scrape` list

# Endpoints

To find scraped articles, you can use following endpoints:

- GET '/articles/' which returns all scraped articles
- GET '/articles/{id}/' which returns article with given id
- GET '/articles/?source=example' which filters articles by source domain

E.g

- http://localhost:8000/Articles/ 

This would return all articles (check whether your port is 8000)



