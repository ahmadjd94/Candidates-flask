import re

from flask import request
from flask_api import FlaskAPI
from werkzeug.utils import secure_filename

from candidate import CandidateJson

import boto3

app = FlaskAPI(__name__)

app.config['DEFAULT_PARSERS'] = [
    # 'flask.ext.api.parsers.JSONParser',
    # 'flask.ext.api.parsers.URLEncodedParser',
    'flask_api.parsers.MultiPartParser'
]


s3 = boto3.resource('s3', endpoint_url='http://localhost:4567',
                    aws_access_key_id='123', aws_secret_access_key='abc')

s3.create_bucket(Bucket="candidates")

ALLOWED_EXTENSIONS = set(['pdf', 'docx'])

extension = re.compile("\.(pdf)$|(docx)$")


@app.route("/register/", methods = ["GET", "POST"])
def post():
    print(request)

    candidate = CandidateJson().load(request.data)

    if any(candidate.errors):
        return candidate.errors

    return candidate.data


@app.route("/upload", methods=["GET", "POST"])
def upload_cv():
    print(request)

    candidate = CandidateJson().load(request.data)

    f = request

    s3.upload_file(secure_filename(f.filename), "candidates", f.filename)
    return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)



# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument("--run")
# parser.add_argument("--migrate",
#                     default=max,
#                     help='migrate database tables')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))


# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     import candidate.models
#     Base.metadata.create_all(bind=engine)