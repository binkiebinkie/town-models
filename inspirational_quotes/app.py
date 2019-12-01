from .tweetManagement import getTweetThenCombine

from flask import Blueprint, render_template

inspirational_quotes_blueprint = Blueprint('inspirational_quotes', __name__)


@inspirational_quotes_blueprint.route('/inspiration')
def return_quote():
    print('----------------------------------------------------------holaaa')
    combinedTweets = getTweetThenCombine()
    print('combinedTweets', combinedTweets)
    return combinedTweets
