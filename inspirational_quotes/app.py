from .tweetManagement import makeABunchOfTweets

from flask import Blueprint, render_template, jsonify

inspirational_quotes_blueprint = Blueprint('inspirational_quotes', __name__)


@inspirational_quotes_blueprint.route('/inspirational-quotes')
def return_inspirational_quotes():
    print('------------------------------inspirational quotes')
    aBunchOfTweets = jsonify(makeABunchOfTweets())
    print('aBunchOfTweets', aBunchOfTweets)
    return aBunchOfTweets
