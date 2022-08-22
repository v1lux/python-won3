from flask import Flask
app = Flask('Magic Install')


@app.route('/')
@app.route('/acasa')
def acasa():
    return "Bine ati venit! Pagina este in constructie."


@app.route('/portofoliu')
def portofoliu():
    return "In curand"


if __name__ == '__main__':
    app.run(debug=True)
