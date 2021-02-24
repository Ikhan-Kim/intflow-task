from cowstate import db

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)

class CowObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_dt = db.Column(db.DateTime(), nullable=False)
    camera_id = db.Column(db.Integer, nullable=False)
    object_id = db.Column(db.Integer, nullable=False)
    activity = db.Column(db.Integer, nullable=False)
    feed = db.Column(db.Integer, nullable=False)
    drinking = db.Column(db.Integer, nullable=False)