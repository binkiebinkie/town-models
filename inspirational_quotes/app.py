from .tweetManagement import makeOneHundredTweetsInspirationalQuotes

from flask import Blueprint, render_template, jsonify

inspirational_quotes_blueprint = Blueprint('inspirational_quotes', __name__)


@inspirational_quotes_blueprint.route('/inspirational_quotes')
def return_inspirational_quotes():
    print('------------------------------inspirational quotes')
    oneHundredTweets = jsonify(makeOneHundredTweetsInspirationalQuotes())
    print('oneHundredTweets', oneHundredTweets)
    return oneHundredTweets
