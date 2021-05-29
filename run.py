from flask import Flask, render_template, request, abort, redirect, url_for, make_response


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', derp='deeeerp')

@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
