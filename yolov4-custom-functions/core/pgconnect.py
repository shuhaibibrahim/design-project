#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "d2a5rlf10s0ng3", user = "jvpnonleoxskdl", password = "9eaf12a5d8bcba98cad9cb022b5ba44c601b146aa6060c6d9e6692946f425fb1", host = "ec2-54-85-13-135.compute-1.amazonaws.com", port = "5432")
print("Opened database successfully")
