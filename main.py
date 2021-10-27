# import "packages" from flask
from flask import Flask, render_template, request
from algorithm.image import image_data
from pathlib import Path
import requests
from api.sportsapi import api_bp

# create a Flask instance
app = Flask(__name__)
app.register_blueprint(api_bp)


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


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        jean_bits_2 = request.form.get("jean_bits_2")
        if len(jean_bits_2) != 0:  # input field has content
            return render_template("binary.html", jean_bits_2=int(jean_bits_2))
    # starting and empty input default
    return render_template("binary.html", jean_bits_2=8)


@app.route('/greet_jean/', methods=['GET', 'POST'])
def greet_jean():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet_jean.html", nickname=name)
    # starting and empty input default
    return render_template("greet_jean.html", nickname="World")


@app.route('/jay/', methods=['GET', 'POST'])
def jay():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("jay.html", nickname=name)
    # starting and empty input default
    return render_template("jay.html", nickname="World")


@app.route('/alex/', methods=['GET', 'POST'])
def alex():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("alex.html", nickname=name)
    # starting and empty input default
    return render_template("alex.html", nickname="World")


@app.route('/allie_greet/', methods=['GET', 'POST'])
def allie_greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("allie_greet.html", nickname=name)
    # starting and empty input default
    return render_template("allie_greet.html", nickname="World")


@app.route('/how_its_made/', methods=['GET', 'POST'])
def how_its_made():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("how_its_made.html", nickname=name)
    # starting and empty input default
    return render_template("how_its_made.html", nickname="World")


@app.route('/jeanbinary/', methods=['GET', 'POST'])
def jeanbinary():
    # submit button has been pushed
    if request.form:
        jean_bits = request.form.get("jean_bits")
        if len(jean_bits) != 0:  # input field has content
            return render_template("jeanbinary.html", jean_bits=int(jean_bits))
    # starting and empty input default
    return render_template("jeanbinary.html", jean_bits=8)


@app.route('/jaybinary/', methods=['GET', 'POST'])
def jaybinary():
    # submit button has been pushed
    if request.form:
        jay_bits = request.form.get("jay_bits")
        if len(jay_bits) != 0:  # input field has content
            return render_template("jaybinary.html", jay_bits=int(jay_bits))
    # starting and empty input default
    return render_template("jaybinary.html", jay_bits=8)


@app.route('/allie_binary/', methods=['GET', 'POST'])
def allie_binary():
    # submit button has been pushed
    if request.form:
        allie_bits = request.form.get("allie_bits")
        if len(allie_bits) != 0:  # input field has content
            return render_template("allie_binary.html", allie_bits=int(allie_bits))
    # starting and empty input default
    return render_template("allie_binary.html", allie_bits=8)


@app.route('/alexbinary/', methods=['GET', 'POST'])
def alexbinary():
    # submit button has been pushed
    if request.form:
        alexbits = request.form.get("alexbits")
        if len(alexbits) != 0:  # input field has content
            return render_template("alexbinary.html", alexbits=int(alexbits))
    # starting and empty input default
    return render_template("alexbinary.html", alexbits=8)


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    rawList = image_data(path)
    colorList = []
    grayList = []
    for img in rawList:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])
    print(path)
    return render_template('rgb.html', images=rawList, colored=colorList, grayed=grayList)


@app.route('/unsigned_addition/', methods=["GET", "POST"])
def unsigned_addition():
    return render_template("unsigned_addition.html", path=Path, BITS=8)


@app.route('/colorcode/', methods=['GET', 'POST'])
def colorcode():
    # submit button has been pushed
    if request.form:
        jean_bits_3 = request.form.get("jean_bits_3")
        if len(jean_bits_3) != 0:  # input field has content
            return render_template("colorcode.html", jean_bits_3=int(jean_bits_3))
    # starting and empty input default
    return render_template("colorcode.html", jean_bits_3=8)


@app.route('/logicgates/')
def logicgates():
    return render_template("logicgates.html")


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())



@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())


@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("covid19.html", stats=response.json())

@app.route('/sportsinformation/')
def sportsinformation():
    return render_template("sportsinformation.html")

@app.route('/sport', methods=['GET', 'POST'])
def sport():
    url = "http://localhost:5000/api/sport"
    response = requests.request("GET", url)
    return render_template("sport.html", sport=response.json())

@app.route('/sports/', methods=['GET', 'POST'])
def sports():
    url = "http://localhost:5000/api/sports"
    response = requests.request("GET", url)
    return render_template("sports.html", sports=response.json())

@app.route('/sportspictures/')
def sportspictures():
    return render_template("sportspictures.html")

@app.route('/womensapparel/', methods=['GET', 'POST'])
def womensapparel():
    return render_template("womensapparel.html")

@app.route('/athletes/')
def athletes():
    return render_template("athletes.html")

@app.route('/mens_apparel/', methods=['GET', 'POST'])
def mens_apparel():
    return render_template("mens_apparel.html")

@app.route('/sportsscore', methods=['GET', 'POST'])
def sportsscore():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("sportsscore.html", stats=response.json())

@app.route('/practice/')
def practice():
    return render_template("practice.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    ),
