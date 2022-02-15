from flask import Flask, request

from service.check_prime import check_prime
from service.artist_service import get_all_artists
from service.song_service import get_all_song

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# test api
@app.route('/check-prime/<int:num>')
def check_prime_api(num):
    if check_prime(num):
        txt = str(num) + " is Prime Number"
        return txt
    else:
        return str(num) + " is not Prime Number"


@app.route('/artists', methods=['GET'])
def get_artists():
    return get_all_artists()


@app.route('/songs', methods=['GET'])
def get_songs():
    return get_all_song()


@app.route('/search', methods=['GET'])
def search_artist():
    args = request.args
    artist = args.get("name")
    return "you search for " + artist


if __name__ == '__main__':
    app.run()
