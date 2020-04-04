from server import server


class Point(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    smell = db.Column(db.Boolean(), nullable=False)
    taste = db.Column(db.Boolean(), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)