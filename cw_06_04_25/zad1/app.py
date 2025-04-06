from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def hello():
    return ("<a href='/about'>O nas</a> <br>"
            "<a href='/users'>Użytkownicy</a> <br> ")


@app.route("/about")
def about():
    return "<h1>O nas</h1>"


@app.route("/users")
def users():
    return render_template_string(
        "<h1>Użytkownicy</h1>"
        "<h2>lista uzytkownikow:</h2> {{users}} <br>"
        "<a href='/user/1'>Użytkownik 1</a> <br>"
        "<a href='/user/2'>Użytkownik 2</a> <br>"
        "<a href='/user/3'>Użytkownik 3</a>", users=users
    )


@app.route("/user/<int:user_id>")
def user(user_id):
    user = users.get(user_id)
    if user:
        return render_template_string("<h1>{{ name }} {{ surname }}</h1><p>Wiek: {{ age }}</p>", **user)
    else:
        return "Uzytkownik nie istnieje", 404


users = {
    1: {
        "name": "Jan",
        "surname": "Kowalski",
        "age": 30,
    },
    2: {
        "name": "Anna",
        "surname": "Nowak",
        "age": 25,
    },
    3: {
        "name": "Piotr",
        "surname": "Zalewski",
        "age": 28,
    },
}

if __name__ == "__main__":
    app.run(debug=True)
