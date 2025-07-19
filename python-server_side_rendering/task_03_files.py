from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []

    return render_template('items.html', items=item_list)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    try:
        if source == 'json':
            products = read_json('products.json')
        elif source == 'csv':
            products = read_csv('products.csv')
        else:
            error = "Wrong source. Use 'json' or 'csv'."
            return render_template('product_display.html', error=error)

        if id_param:
            try:
                product_id = int(id_param)
                products = [p for p in products if p['id'] == product_id]
                if not products:
                    error = "Product not found"
            except ValueError:
                error = "Invalid ID format. ID must be an integer."

        return render_template('product_display.html', products=products, error=error)

    except Exception as e:
        return render_template('product_display.html', error=f"Internal error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
