from flask import Flask, render_template

app = Flask('Magic Install')


@app.route('/')
@app.route('/acasa')
def acasa():
    return render_template('acasa.html')


@app.route('/portofoliu')
def portofoliu():
    return render_template('portofoliu.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
