from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)
url_database = {}

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get("url")
    short_url = generate_short_url()
    url_database[short_url] = original_url
    return jsonify({"short_url": f"http://localhost:5000/{short_url}"})

@app.route('/<short_url>')
def redirect_url(short_url):
    return f"Redirecting to {url_database.get(short_url, 'URL not found')}"

if __name__ == "__main__":
    app.run(debug=True)
