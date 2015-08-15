from flask import Flask, session
from infer.response import Response

app = Flask(__name__)
response_obj = Response()

from infer import router
