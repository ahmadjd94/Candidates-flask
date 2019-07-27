from flask import request
from flask_api import FlaskAPI

from Candidate import CandidateSchema

app = FlaskAPI(__name__)



@app.route("/register/", methods = ["GET", "POST"])
def post():
    print(request)

    candidate = CandidateSchema().load(request.data)

    if any(candidate.errors):
        return candidate.errors

    return candidate.data


if __name__ == "__main__":
    app.run(debug=True)
