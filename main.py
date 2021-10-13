# import "packages" from flask
from flask import Flask, render_template, request
from algorithm.image import image_data
from pathlib import Path
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

@app.route('/binary/')
def binary():
    return render_template("binary.html")

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

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)