# from db.base import Base

# app = FlaskAPI(__name__)
#
# app.config['DEFAULT_PARSERS'] = [
#     # 'flask.ext.api.parsers.JSONParser',
#     # 'flask.ext.api.parsers.URLEncodedParser',
#     'flask_api.parsers.MultiPartParser'
# ]
#
# app.config.from_pyfile('app_config.cfg')
#
#
# s3 = boto3.client('s3', endpoint_url='http://localhost:4567',
#                   aws_access_key_id='123', aws_secret_access_key='abc')
#
# s3.create_bucket(Bucket="candidates")
#
# ALLOWED_EXTENSIONS = {"docx", "pdf"}
#
# extension = re.compile("\.(pdf)$|(docx)$")

#
# @app.route("/register", methods=["GET", "POST"])
# def post():
#     candidate = CandidateJson().load(request.data)
#
#     if any(candidate.errors):
#         return candidate.errors
#
#     return candidate.data
#
#
# @app.route("/upload", methods=["POST"])
# def upload_cv():
#     f = request.files["file"]   # send this within  the request as a file field
#     s3.upload_fileobj(f.stream, "BUCKET_NAME", f.filename)
#     return 'file uploaded successfully'
#
#
# @app.route("/list_all", methods=["get"])
# def list_cvs():
#     print(request)
#     s3.upload_fileobj(f.stream, "BUCKET_NAME", f.filename)
#     return 'file uploaded successfully'


     # app.run(debug=True)



import argparse

from flask_app import flask_app
from flask_app.db.base import Base


def migrate():
    pass

def run():
    flask_app.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--run",
                        action='store_const', const=True,
                        default=True,
                        help='run app')
    parser.add_argument("--migrate",
                        action='store_const', const=True,
                        default=False,
                        help='migrate database tables')

    a = parser.parse_args()

    if a.migrate:
        base = Base()
        res = base.migrate(Base.__class__, flask_app)
    if a.run:
        run()







# def init_db():
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to imp
#     # ort them first before calling init_db()
#     import candidate.models
#     Base.migrate()
