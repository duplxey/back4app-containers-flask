from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = '5b3cd5b80eb8b217c20fb37074ff4a33'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///default.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)

    is_watched = db.Column(db.Boolean, default=False)
    watched_at = db.Column(db.DateTime, default=None, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Movie %r>' % self.title


@app.route('/')
def index_view():
    return {
        'name': 'flask-watchlist',
        'description': 'a simple app for tracking the movies you want to watch',
        'version': 1.1,
    }


@app.route('/api/')
def list_view():
    json = [movie.as_dict() for movie in Movie.query.all()]
    return jsonify(json)


@app.route('/api/<int:movie_id>/', methods=['GET', 'DELETE'])
def detail_view(movie_id):
    movie = db.get_or_404(Movie, movie_id)

    if request.method == 'DELETE':
        db.session.delete(movie)
        db.session.commit()

        return {
            'detail': 'Movie has been successfully deleted.'
        }
    else:
        return movie.as_dict()


@app.route('/api/create/', methods=['POST'])
def create_view():
    title = request.form.get('title')
    release_date = request.form.get('release_date', type=float)

    if title is None or release_date is None:
        return {
            'detail': 'Please provide the title and release_date.'
        }, 400

    movie = Movie(title=title, release_date=datetime.fromtimestamp(release_date))
    db.session.add(movie)
    db.session.commit()

    return movie.as_dict()


@app.route('/api/watch/<int:movie_id>/')
def watch_view(movie_id):
    movie = db.get_or_404(Movie, movie_id)

    if movie.is_watched:
        return {
            'detail': 'Movie has already been watched.'
        }, 400

    movie.is_watched = True
    movie.watched_at = datetime.now()
    db.session.commit()

    return movie.as_dict()
