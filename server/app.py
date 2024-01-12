#!/usr/bin/env python3

from flask import Flask, make_response, render_template
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    return(
        f'<li>ID:{animal.id}</li><br/>'
        f'<li>Name:{animal.name}</li><br/>'
        f'<li>Species:{animal.species}</li><br/>'
        f'<li>Zookeeper:{animal.zookeeper_id}</li><br/>'
        f'<li>Enclosure:{animal.enclosure_id}</li><br/>'
    )

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    return(
        f'<li>ID:{zookeeper.id}</li><br/>'
        f'<li>Name:{zookeeper.name}</li><br/>'
        f'<li>Birthday:{zookeeper.birthday}</li><br/>'
    )

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    return(
        f'<li>ID:{enclosure.id}</li><br/>'
        f'<li>Environment:{enclosure.environment}</li><br/>'
        f'<li>Open to visitors:{enclosure.open_to_visitors}</li><br/>'
    )


if __name__ == '__main__':
    app.run(port=5555, debug=True)
