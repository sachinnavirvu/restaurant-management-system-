from flask import Flask, render_template, request

app = Flask(__name__)

# Home page with menu
@app.route('/')
def home():
    return render_template('menu.html', menu=menu)

# Dummy menu data
menu = [
    {"id": 1, "name": "Burger", "price": 10},
    {"id": 2, "name": "Pizza", "price": 12},
    {"id": 3, "name": "Salad", "price": 8},
    {"id": 4, "name": "Pasta", "price": 15}
]

# Order page
# Order page
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        items = [int(item) for item in request.form.getlist('item')]  # Convert to integers here
        total = sum(menu[item - 1]['price'] for item in items)
        return render_template('order_summary.html', items=items, total=total, menu=menu)
    return render_template('order.html', menu=menu)


if __name__ == '_main_':
    app.run(debug=True)