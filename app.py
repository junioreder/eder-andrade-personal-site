"""
Main file of the APP
"""

from flask import Flask, render_template
import qrcodegenerator # pylint: disable=unused-import

app = Flask(__name__)


@app.route("/")
def default():
    """Renders index.html on main route"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
