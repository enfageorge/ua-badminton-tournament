from app import db

"""
Class Result, stores the result corresponding to a Match
"""


class Result(db.Model):
    __tablename__ = "result"
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    result_name = db.Column(db.String(20), nullable=True)  # result obtained, results awaiting etc.
    result_score = db.Column(db.String(30), nullable=True)
    matches = db.relationship("Match", backref="result", lazy=True)

    def __init__(self, result_name: str = None, result_score: str = None) -> None:
        """
        Initialize a Result object with the given attributes.
        result_name: The name of the result (optional).
        result_score: The score of the result (optional).
        """
        self.result_name = result_name
        self.result_score = result_score

    def __repr__(self) -> str:
        """Return a string representation of the Result object."""
        return f"<Result {self.result_name}, Result score {self.result_score}>"
