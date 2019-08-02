import os
import re

from flask import request
from flask_api import FlaskAPI
from werkzeug.utils import secure_filename

# from candidate import CandidateJson

import boto3

# from db.base import Base

app = FlaskAPI(__name__)

app.config['DEFAULT_PARSERS'] = [
    # 'flask.ext.api.parsers.JSONParser',
    # 'flask.ext.api.parsers.URLEncodedParser',
    'flask_api.parsers.MultiPartParser'
]

app.config.from_pyfile('app_config.cfg')


s3 = boto3.client('s3', endpoint_url='http://localhost:4567',
                  aws_access_key_id='123', aws_secret_access_key='abc')

s3.create_bucket(Bucket="candidates")

ALLOWED_EXTENSIONS = {"docx", "pdf"}

print(s3.list_buckets())

extension = re.compile("\.(pdf)$|(docx)$")


@app.route("/register", methods=["GET", "POST"])
def post():
    print(request)

    candidate = CandidateJson().load(request.data)

    if any(candidate.errors):
        return candidate.errors

    return candidate.data


@app.route("/upload", methods=["POST"])
def upload_cv():
    print(request)

    f = request.files["file"] # send this within  the request as a file field
    s3.upload_fileobj(f.stream, "BUCKET_NAME", f.filename)
    return 'file uploaded successfully'


@app.route("/list_all", methods=["get"])
def list_cvs():
    print(request)
    s3.upload_fileobj(f.stream, "BUCKET_NAME", f.filename)
    return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)



import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--run")
parser.add_argument("--migrate",
                    default=max,
                    help='migrate database tables')

args = parser.parse_args()
print(args.accumulate(args.integers))




# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to imp
#     # ort them first before calling init_db()
#     import candidate.models
#     Base.migrate()
