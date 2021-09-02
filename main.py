# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/greet_jean', methods=['GET', 'POST'])
def greet_jean():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet_jean.html", nickname=name)
    # starting and empty input default
    return render_template("greet_jean.html", nickname="World")



@app.route('/jay', methods=['GET', 'POST'])
def jay():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("jay.html", nickname=name)
    # starting and empty input default
    return render_template("jay.html", nickname="World")

@app.route('/alex', methods=['GET', 'POST'])
def alex():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("alex.html", nickname=name)
    # starting and empty input default
    return render_template("alex.html", nickname="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
