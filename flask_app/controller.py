from flask import request

from flask_app import flask_app
from flask_app.entities.candidate import CandidateJson


@flask_app.route("/register", methods=["GET", "POST"])
def post():
    candidate = CandidateJson().load(request.data)

    if any(candidate.errors):
        return candidate.errors

    return candidate.data


@flask_app.route("/upload", methods=["POST"])
def upload_cv():
    f = request.files["file"]   # send this within  the request as a file field
    # s3.upload_fileobj(f.stream, "BUCKET_NAME", f.filename)
    return 'file uploaded successfully'


@flask_app.route("/list_all", methods=["get"])
def list_cvs():
    print(request)
    # s3.upload_fileobj(f.stream, "BUCKET_NAME", f.filename)
    return 'file uploaded successfully'