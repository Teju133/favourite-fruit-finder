from flask import Flask, render_template, request
import random  # Import random module

app = Flask(__name__)

# List of fruits
fruit_list = [
    'Apple 🍎', 'Banana 🍌', 'Cherry 🍒', 'Dragon Fruit 🐉', 'Elderberry 🍇',
    'Fig 🍈', 'Grapes 🍇', 'Honeydew 🍈', 'Indian Fig 🍐', 'Jackfruit 🍈',
    'Kiwi 🥝', 'Lemon 🍋', 'Mango 🥭', 'Nectarine 🍊', 'Orange 🍊',
    'Papaya 🍍', 'Quince 🍏', 'Raspberry 🍓', 'Strawberry 🍓', 'Tangerine 🍊',
    'Ugli Fruit 🍊', 'Vanilla Bean 🌿', 'Watermelon 🍉', 'Xigua 🍉',
    'Yellow Passionfruit 🥭', 'Zucchini 🍆'
]

@app.route("/", methods=["GET", "POST"])
def home():
    fruit = None
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            fruit = random.choice(fruit_list)  # Select a random fruit
    return render_template("index.html", fruit=fruit)

if __name__ == "__main__":
    app.run(debug=True)
