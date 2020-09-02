# Commodities API

* Flask based API that fetches stock value for Crude oil, Brent oil, gold, Natural gas, silver, copper, US Soybeans from [investing.com](https://www.investing.com/)

## Installation and setup

* Create virtualenv
```
virtualenv venv
```

```
cd venv/Scripts/activate
```

* In root directory

```
pip install -r requirements.txt
```

```
python app.py
```
* API runs on your [localhost](http://localhost:5000/)

## Deploying to heroku

* Read this [document](https://devcenter.heroku.com/articles/getting-started-with-python) on deploying flask apps to heroku.

* Or simply click this button to deploy.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) [(Heroku instructions)]