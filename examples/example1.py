from flask import Flask,jsonify,request,render_template,redirect

#app = Flask(__name__)
app = Flask("myapp")

stores = [
    {
        'name': "My WOnderful Store",
        'items': [
            {
                'name': "My item",
                'price': 17.99
            }
        ]
    },
    {
        'name': "Second store",
        'items': [
            {
                'name': "My second item",
                'price': 3.80
            }
        ]
    }
]

#@app.route('/')
#def home():
#    return "<h1>Welcome to the API!</h1>"

@app.route('/')
def home():
  return render_template('index.html')

#@app.route('/redirect')
#def redirect():
#    return redirect("https://www.github.com", code=302)

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  #pass

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})
  #pass

# GET /store
@app.route('/store') 
def get_stores():
    return jsonify({'stores':stores})

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

  #pass

app.run(host='0.0.0.0',port=5000,debug=True)