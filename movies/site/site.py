from flask import Blueprint, jsonify, render_template, request

web_site = Blueprint('web_site', __name__ ,  url_prefix='/')

@web_site.route('/')
# go to the first view of the page, in this case index.html
def movie():
    return render_template('index.html')


