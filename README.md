<p align="center">
  <img src="https://user-images.githubusercontent.com/214063/46479857-4cd66e80-c7f0-11e8-9585-5748409c9490.png" width="60%">
</p>
-------

## Commodities API
![alt text for screen readers](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQT-1K3ZDb7HD-lB6Putm40XhTHwfgDRkKmgw&usqp=CAU)


* Flask based API that fetches stock value for Crude oil, Brent oil, gold, Natural gas, silver, copper, US Soybeans from [investing.com](https://www.investing.com/)

### End points
* Method: POST
* Example request:
```
curl - X POST "http://investingdotcom.herokuapp.com/natural-gas"
```
* Example response:
```
{
    "change": "-0.069",
    "changepercentage": "-2.73%",
    "commodity": "Natural Gas",
    "price": "2.458"
}
```

```
http://investingdotcom.herokuapp.com/
http://investingdotcom.herokuapp.com/crude-oil
http://investingdotcom.herokuapp.com/brent-oil
http://investingdotcom.herokuapp.com/natural-gas
http://investingdotcom.herokuapp.com/gold
http://investingdotcom.herokuapp.com/silver
http://investingdotcom.herokuapp.com/copper
http://investingdotcom.herokuapp.com/us-soybeans
```
### Installation and setup

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

### Deploying to heroku

* Read this [document](https://devcenter.heroku.com/articles/getting-started-with-python) on deploying flask apps to heroku.

* Or simply click this button to deploy \
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) 