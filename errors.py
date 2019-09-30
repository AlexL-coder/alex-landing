from flask import render_template,redirect, url_for

from flask_app import app
from flask_app import db

@app.errorhandler(404)
def not_found_error(error):
    #return render_template('errors/404.html'), 404
     return redirect(url_for('index'))
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
