#!/usr/bin/env python

# Generated by mock-builder

from flask import Flask, request

app = Flask(__name__)

@app.route("/v1/AUTH_<test>/<uuid1>", methods=["PUT"])
def put_v1_AUTH__test___uuid1_(test, uuid1):
    return ('''''', 201, {'Content-Length': '0', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Sat, 26 Oct 2013 23:39:41 GMT'})

@app.route("/v1/AUTH_<test>/<uuid1>", methods=["DELETE"])
def delete_v1_AUTH__test___uuid1_(test, uuid1):
    return ('''''', 204, {'Content-Length': '0', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Sat, 26 Oct 2013 23:39:44 GMT'})

@app.route("/auth/v1.0", methods=["GET"])
def get_auth_v1_0():
    return ('''''', 200, {'X-Storage-Url': 'http://127.0.0.1:8081/v1/AUTH_test', 'X-Auth-Token': 'AUTH_tkee6681f4d95a41bdad5cdc99d7da3d5d', 'Content-Type': 'text/html; charset=UTF-8', 'X-Storage-Token': 'AUTH_tkee6681f4d95a41bdad5cdc99d7da3d5d', 'Content-Length': '0', 'Date': 'Sat, 26 Oct 2013 23:39:43 GMT'})

@app.route("/v1/AUTH_<test>/<uuid1>/<uuid2>", methods=["GET"])
def get_v1_AUTH__test___uuid1___uuid2_(test, uuid1, uuid2):
    return ('''00''', 200, {'Content-Length': '2', 'X-Object-Meta-Key-Id': '12345', 'Last-Modified': 'Sat, 26 Oct 2013 23:39:43 GMT', 'Etag': 'b4b147bc522828731f1a016bfa72c073', 'X-Timestamp': '1382830783.60222', 'Content-Type': 'application/octet-stream', 'Accept-Ranges': 'bytes', 'Date': 'Sat, 26 Oct 2013 23:39:43 GMT'})

@app.route("/v1/AUTH_<test>/<uuid1>/<uuid2>", methods=["PUT"])
def put_v1_AUTH__test___uuid1___uuid2_(test, uuid1, uuid2):
    return ('''''', 201, {'Last-Modified': 'Sat, 26 Oct 2013 23:39:43 GMT', 'Content-Length': '0', 'Etag': 'b4b147bc522828731f1a016bfa72c073', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Sat, 26 Oct 2013 23:39:43 GMT'})

@app.route("/v1/AUTH_<test>/<uuid1>/<uuid2>", methods=["DELETE"])
def delete_v1_AUTH__test___uuid1___uuid2_(test, uuid1, uuid2):
    return ('''''', 204, {'Content-Length': '0', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Sat, 26 Oct 2013 23:39:43 GMT'})

if __name__ == "__main__":
    app.run(host="127.1", debug=True, port=8081)
