from server import db


class Point(db.Model):
    __tablename__ = "points"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(DateTime, default=datetime.datetime.utcnow)
    smell = db.Column(db.Boolean(), nullable=False)
    taste = db.Column(db.Boolean(), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
