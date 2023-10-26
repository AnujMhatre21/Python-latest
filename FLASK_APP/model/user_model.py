import mysql.connector
import json
from flask import make_response
from datetime import datetime, timedelta
import jwt
from config.config import dbconfig


class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host=dbconfig['hostname'], user=dbconfig['usename'], password=[dbconfig['password']], database=['database'])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connecction Successfull")

        except:
            print("Something went wrong during connection")

    def user_getall_model(self):
        self.cur.execute("SELECT * from user")
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({"payload": result}, 200)
        else:
            return make_response({"message": "No data Found"}, 204)

    def user_add_model(self, data):
        self.cur.execute(
            f"INSERT into user( name, email, phone, role, password) VALUES ('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return make_response({"message": "User added Successfully"}, 201)

    def user_update_model(self, data):
        self.cur.execute(
            f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' where id={data['id']}  ")
        if self.cur.rowcount > 0:
            return make_response({"message": "User Updated Successfully"}, 201)
        else:
            return make_response({"message": "Nothing to be updated"}, 202)

    def user_delete_model(self, id):
        self.cur.execute(f"DELETE from user where id = {id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "User has been Deleted"}, 200)
        else:
            return make_response({"message": "Nothing is deleted"}, 202)

    def user_patch_model(self, data, id):
        qry = "UPDATE user SET "
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {id}"

        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message": "User Updated Successfully"}, 201)
        else:
            return make_response({"message": "Nothing to be updated"}, 202)

    def user_pagination_model(self, limit, page):
        limit = int(limit)
        page = int(page)
        # formual toget the start of the page
        start = (page*limit) - limit
        qry = f"SELECT * FROM user LIMIT {start},{limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({"payload": result, "page_no": page, "limit": limit}, 200)
        else:
            return make_response({"message": "No data Found"}, 204)

    def user_upload_avatar_model(self, uid, finalFilePath):
        self.cur.execute(
            f"UPDATE user SET avatar ='{finalFilePath}' where id = {uid}")
        if self.cur.rowcount > 0:
            return make_response({"message": "File Uploaded Succesfully"}, 201)
        else:
            make_response({"message": "Nothing to be updated"}, 202)
        return "This is the avatar model"

    def user_login_model(self, data):
        self.cur.execute(
            f"SELECT id, name, email, phone, avatar, role_id from user where email='{data['email']}' and password = '{data['password']}' ")
        result = self.cur.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time = int(exp_time.timestamp())
        payload = {
            "payload": userdata,
            "exp": exp_epoch_time
        }
        jwtToken = jwt.encode(payload, "anuj", algorithm="HS256")
        return make_response({"token": jwtToken}, 200)
