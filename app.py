from flask import Flask, render_template, request, jsonify
from scraper import scrapeDetails

app = Flask(__name__)

@app.route('/')
def student():
   return jsonify(welcome = 'welcome to blah blah api')

@app.route('/crude-oil', methods = ['POST', 'GET'])
def crudeOil():
   if request.method == 'POST':
      result = scrapeDetails('crude-oil')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

@app.route('/brent-oil', methods = ['POST', 'GET'])
def brentOil():
   if request.method == 'POST':
      result = scrapeDetails('brent-oil')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

@app.route('/natural-gas', methods = ['POST', 'GET'])
def natGas():
   if request.method == 'POST':
      result = scrapeDetails('natural-gas')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

@app.route('/gold', methods = ['POST', 'GET'])
def gold():
   if request.method == 'POST':
      result = scrapeDetails('gold')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

@app.route('/silver', methods = ['POST', 'GET'])
def silver():
   if request.method == 'POST':
      result = scrapeDetails('silver')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

@app.route('/copper', methods = ['POST', 'GET'])
def copper():
   if request.method == 'POST':
      result = scrapeDetails('copper')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

@app.route('/us-soybeans', methods = ['POST', 'GET'])
def usSoybean():
   if request.method == 'POST':
      result = scrapeDetails('us-soybeans')
      return jsonify(commodity = result[0], price = result[1], change = result[2], changepercentage = result[3])

if __name__ == '__main__':
   app.run()