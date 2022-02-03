# [Flask Dashboard Boilerplate](https://appseed.us/boilerplate-code/flask-dashboard)

> Template [boilerplate code](https://appseed.us/boilerplate-code) used by [AppSeed](https://appseed.us) to generate simple admin dashboards coded in Flask - Features:

<br />

- `Up-to-date dependencies`
- [SCSS compilation](#recompile-css) via **Gulp**
- UI Kit: **Volt Dashboard** (Free Version) provided by **Themesberg**
- `DBMS`: SQLite, PostgreSQL (production) 
- `DB Tools`: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- `Session-Based` authentication, **Blueprints**
- `Deployment`: **Docker**, Gunicorn / Nginx, `HEROKU`
- `Database Provisioning` via custom commands
  - `flask load_data` parse and load the [sample file](./media/transactions_data.csv)
- Free [support](https://appseed.us/support) via `email` and [Discord](https://discord.gg/fZC6hup).

<br />

> Links

- 👉 [Boierplate Flask Dashboard](https://appseed.us/admin-dashboards/flask-dashboard-volt) - Product page
- 👉 [Boierplate Flask Dashboard](https://flask-volt-dashboard.appseed-srv1.com/) - LIVE Demo
- 👉 [Boierplate Flask Dashboard](https://docs.appseed.us/boilerplate-code/flask-dashboard/) - Documentation

<br />

## ✨ Quick Start in `Docker`

> Get the code

```bash
$ git clone https://github.com/app-generator/boilerplate-code-flask-dashboard.git
$ cd boilerplate-code-flask-dashboard
```

> Start the app in Docker

```bash
$ docker-compose up --build 
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

![Boierplate Code Django Dashboard - Template project provided by AppSeed.](https://user-images.githubusercontent.com/51070104/152407612-2c514657-4c49-44be-8bd4-29b939d3da21.jpg)

<br />

## ✨ **[Product Roadmap](https://github.com/app-generator/boilerplate-code-flask-dashboard/blob/master/SPECS.md)**

- [x] **Updated dependencies**
- [x] **Pythonic Footprint**
- [x] **Improved Authentication**: 
  - [x] `Password reset`
  - [x] `Email confirmation on register`
  - [x] `Extended user model`
    - [x] First, Last Name
    - [x] Birthday, Gender, Email, Phone
    - [x] User Photo
- [x] `Data Tables` - manages paginated information
  - [x] Data load via `Flask CLI`
    - Input: `media/transactions_data.csv`
    - Load CMD: `flask load_data` / values from input / random dates
    - Load CMD: `flask load_random_data` / randomize values and dates
  - [x] Pagination, Inline edit via Ajax
  - [x] Simple Search
  - [x] Export `PDF`/`xls`: one page, multiple pages, filtered by `search` 
- [x] `API` via Flask-RestX
- [x] `Sample Charts`
  - Main Dashbord updated to show case real data
- [WIP] `Social Login`
  - [WIP] *Google*
  - [WIP] *Github*
- [WIP] `Deployment`: 
  - [x] Docker 
  - [x] *HEROKU* 
  - [WIP] *AWS Ec2* 
- [WIP] `Payments`: One-time payments via [Stripe Checkout](https://stripe.com/payments/checkout)

<br />

## ✨ How to use it

> 👉 **Clone Sources** (this repo)

```bash
$ git clone https://github.com/app-generator/boilerplate-code-flask-dashboard.git
$ cd boilerplate-code-flask-dashboard
```

<br />

> 👉 **Install Modules** using a Virtual Environment

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

Or for **Windows-based Systems**

```bash
$ virtualenv env
$ .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
```

<br />

> 👉 **Set up the environment**

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

Or for **Windows-based Systems**

```bash
$ # CMD terminal
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> 👉 **Load Sample Data** `transactions_data.csv`

```bash
$ flask load_data        # with randomized timestamps
$ flask load_random_data # with randomized timestamps and transaction values
```

<br />

> 👉 **Start the APP**

```bash
$ flask run 
```

At this point we should be able to register new users, authenticate and access the API: 

- Register: `http://localhost:5000/register`
- Login: `http://localhost:5000/login`
- Access the public API
  - Get all items: `http://localhost:5000/api/data`
  - Get 1st item: `http://localhost:5000/api/data`
  - Get Sales Stats: `http://localhost:5000/api/sales`

<br />

![Flask Boilerplate Code - API Access.](https://user-images.githubusercontent.com/51070104/152408165-c6063314-564b-48ce-a092-bd33bb1f6fdb.png) 

<br />

## ✨ Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

> Simplified version

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- routes.py                 # Define authentication routes  
   |    |    |-- models.py                 # Defines models  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |    |    |-- includes/                 # HTML chunks and components
   |    |    |    |-- navigation.html      # Top menu component
   |    |    |    |-- sidebar.html         # Sidebar component
   |    |    |    |-- footer.html          # App Footer
   |    |    |    |-- scripts.html         # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt               # Production modules  - PostgreSql DMBS
   |
   |-- Dockerfile                           # Deployment
   |-- docker-compose.yml                   # Deployment
   |-- gunicorn-cfg.py                      # Deployment   
   |-- nginx                                # Deployment
   |    |-- appseed-app.conf                # Deployment 
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- `run.py` loads the `.env` file
- Initialize the app using the specified profile: *Debug* or *Production*
  - If env.DEBUG is set to *True* the SQLite storage is used
  - If env.DEBUG is set to *False* the specified DB driver is used (MySql, PostgreSQL)
- Call the app factory method `create_app` defined in app/__init__.py
- Redirect the guest users to Login page
- Unlock the pages served by *home* blueprint for authenticated users

<br />

## ✨ Recompile CSS

To recompile SCSS files, follow this setup:

<br />

> **Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

> **Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

> **Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

> **Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br />

## ✨ Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Heroku](https://www.heroku.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Heroku](https://www.heroku.com/)
---

Steps to deploy on **Heroku**

- [Create a FREE account](https://signup.heroku.com/) on Heroku platform
- [Install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) that match your OS: Mac, Unix or Windows
- Open a terminal window and authenticate via `heroku login` command
- Clone the sources and push the project for LIVE deployment

```bash
$ # Clone the source code:
$ git clone https://github.com/app-generator/boilerplate-code-flask-dashboard.git
$ cd boilerplate-code-flask-dashboard
$
$ # Check Heroku CLI is installed
$ heroku -v
heroku/7.25.0 win32-x64 node-v12.13.0 # <-- All good
$
$ # Check Heroku CLI is installed
$ heroku login
$ # this commaond will open a browser window - click the login button (in browser)
$
$ # Create the Heroku project
$ heroku create
$
$ # Trigger the LIVE deploy
$ git push heroku master
$
$ # Open the LIVE app in browser
$ heroku open
```

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

- 👉 [Flask Framework](https://www.palletsprojects.com/p/flask/) - The offcial website
- 👉 [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- 👉 [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
[Flask Dashboard Boilerplate](https://appseed.us/boilerplate-code/flask-dashboard) - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
