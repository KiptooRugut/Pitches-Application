# Pitches-Application

#### Author: [KiptooRugut](https://github.com/kiptooRugut)


## Description
This is an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them. The pitches are organized by category. You can have different categories like pickup lines, interview pitch, product pitch, promotion pitch.
As a user of the web application you will be able to:

1. Sign up and log in
2. View pitches posted by other users
3. Post pitches
4. Edit your profile

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/KiptooRugut/Pitches-Application.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
`

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)

       
## Built With

* [Python3.6](https://docs.python.org/3/)
* Flask3.8
* Postgresql 
* Boostrap
* HTML
* CSS


### License

#### LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE).
