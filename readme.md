# Demo Data Cleaner for QuickFrame

### Instructions
I ran this locally on a Mac running MacOS 10.14.6 in a virtualenv using Python 3.7.4

First clone the repo then cd into it
`pip install -r requirements.txt`

Its not production ready so we can simply do the following
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`

Then load a browser to `localhost:8000/data` and you'll be presented with a link to clean the provided dataset. Click on it and wait for it to complete, it will redirect you to the same page this time showing the cleaned data solving problems one and two.


### Moving forward

This was tricky! For problem two in particular there are a lot of edge cases. I did my best to cover most of them but I did end up with a catch all noted as "error parsing {date}". For future growth on this project I would envision a more streamlined version of the date validater. Probably a model that includes all edge cases to be added to as necessary. 
