from .tweetManagement import makeOneHundredTweetsBabyNames

from flask import Blueprint, render_template, jsonify

baby_names_blueprint = Blueprint('baby_names', __name__)


@baby_names_blueprint.route('/baby-names')
def return_baby_names():
    print('------------------------------baby names function')
    oneHundredTweets = jsonify(makeOneHundredTweetsBabyNames())
    print('oneHundredTweets', oneHundredTweets)
    return oneHundredTweets
