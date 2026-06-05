from flask import *
import urllib.parse
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("main.html")


@app.route('/api/<set_name>/<int:card_number>')
def frame(set_name, card_number):
    sanitised_set_name = urllib.parse.quote_plus(set_name)
    url = f"https://api.scryfall.com/cards/{sanitised_set_name}/{card_number}"
    resp = requests.get(url).json()

    # foil = request.args.get('foil', False)

    data = {
        "price": resp["prices"]["usd"],
        "name": resp["name"],
        "rarity": resp["rarity"],
        "image": resp["image_uris"]["large"],
        # "foil": foil
    }

    print(data)

    return Response(json.dumps(data), mimetype='application/json')


if __name__ == '__main__':
    app.run()
