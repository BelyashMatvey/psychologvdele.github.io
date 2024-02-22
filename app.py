from flask import Flask, render_template

application = Flask(__name__)
application.config['DEBUG'] = False


@application.route('/')
def home():
    return render_template('index.html')


@application.route('/publications')
def publications():
    return render_template('my_publ.html')


@application.route('/videos')
def videos():
    return render_template('Videos.html')


@application.route('/contacts')
def contacts():
    return render_template('contacts.html')


@application.route('/education')
def education():
    return render_template('education.html')


@application.route('/documents')
def documents():
    return render_template('documents.html')


@application.route('/prices')
def prices():
    return render_template('prices.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
