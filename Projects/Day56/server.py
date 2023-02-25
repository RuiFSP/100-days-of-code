import os
from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)
