from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Videogame(db.Model):
    __tablename__ = "Videogame"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    PEGI = db.Column(db.Integer())
    mark = db.Column(db.Integer())

    def __init__(self, game_id, name, PEGI, mark):
        self.game_id = game_id
        self.name = name
        self.PEGI = PEGI
        self.mark = mark

    def __repr__(self):
        return f"{self.name}:{self.game_id}"
