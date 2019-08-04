### Candidates-flask
dummy project for flask with marhmallow


steps to run the project : 

first you will need to create a new virtualenv to separate dependencies of the project

``
virtualenv env - python3.7 //this assumes you have python 3.7 installed
``

next you will need to activate the fresh virtual environment:

``
source env/bin/activate
``

install the project dependencies by running the following command:

``
pip3 install - r requirements.txt
``

install fake S3
````
gem install fakes3
````
note that fakeS3 might require sudo privileges to be ran on some devices

before running FakeS3, obtain a free license key from  the following [link](https://supso.org/projects/fake-s3/register)

running fakeS3
````
fakes3 -r /mnt/fakes3_root -p 4567 --license 6930221557
````

download the mariaDb Docker image by running the following command:

``
docker-compose up
``

next you can run the project:

``
python app.py
``