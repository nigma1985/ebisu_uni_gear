import os
import json
# import psycopg2
# from psycopg2 import Error

def json2py(jsonPath):
    with open(jsonPath, 'r') as f:
        return json.load(f)
