from flask import Flask, render_template, request

app = Flask(__name__)

pizzas = [
    {'name': 'Маргарита', 'description': 'Помідори, моцарела, базилік', 'price': 120},
    {'name': 'Салямі', 'description': 'Салямі, моцарела, томатний соус', 'price': 140},
    {'name': 'Чотири сири', 'description': 'Моцарела, горгонзола, пармезан, дорблю', 'price': 160}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    reverse_sort = request.args.get('sort', 'asc') == 'desc'
    sorted_pizzas = sorted(pizzas, key=lambda x: x['price'], reverse=reverse_sort)
    return render_template('menu.html', pizzas=sorted_pizzas, reverse_sort='asc' if reverse_sort else 'desc')

if __name__ == '__main__':
    app.run(debug=True)
