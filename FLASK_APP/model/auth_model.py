from functools import wraps
import mysql.connector
import json
from flask import make_response, request
import jwt
import re
from config.config import dbconfig


class auth_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host=dbconfig['hostname'], user=dbconfig['usename'], password=[dbconfig['password']], database=['database'])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connecction Successfull")

        except:
            print("Something went wrong during connection")

    def token_auth(self, endpoint=''):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                # automaically fetches the api called 
                endpoint = request.url_rule
                print(endpoint)
                authorization = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+ *$)", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        jwt_decoded = jwt.decode(
                            token, "anuj", algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR": "TOKEN EXPIRED"}, 401)

                    role_id = jwt_decoded['payload']['role_id']
                    self.cur.execute(
                        f"SELECT roles from accessibility_view where endpoint = '{endpoint}'")
                    result = self.cur.fetchall()
                    if len(result) > 0:
                        allowed_roles = json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR": "INVALID ROLE"}, 404)
                    else:
                        return make_response({"ERROR": "Unknown Endpoint"}, 404)
                else:
                    return make_response({"ERROR": "Invalid Token"}, 401)
            return inner2
        return inner1
