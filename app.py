from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route("/movie", methods=["POST"])
def get_movie_data():
    api_key = "49001760686d3dc41d01a43ad332fc41"
    base_url = 'https://api.themoviedb.org/3/'

    movie_id = request.form.get("movie_id")
    url = f'{base_url}movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()

    return render_template('movie.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
