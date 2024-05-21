from flask import Flask, render_template

app = Flask(__name__)

# Sample data
# tables = {
#     "Table1": [
#         {"id": 1, "name": "Alice", "age": 30},
#         {"id": 2, "name": "Bob", "age": 25}
#     ],
#     "Table2": [
#         {"id": 1, "product": "Widget", "price": 19.99},
#         {"id": 2, "product": "Gadget", "price": 22.50}
#     ]
# }


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
