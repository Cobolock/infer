from flask import Flask
from response import Response

app = Flask(__name__)
response_obj = Response()

from infer import router
