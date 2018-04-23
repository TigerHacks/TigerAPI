#SPDX-License-Identifier: MIT
import os
import sys
import ipdb
import traceback
if (sys.version_info > (3, 0)):
    import configparser as configparser
else:
    import ConfigParser as configparser

sys.path.append('..')

import thapi
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json

# Location to load configuration from
CONFIG_BAD = False
'''
make a try and accept condition
if its open the GH_DATA_ONFIG_FILE and then its open in read mode
and if the file does't open the it print Couldn\'t open config file, attempting to create.
'''
try:
    THAPI_CONFIG_FILE = open(os.getenv('THAPI_CONFIG_FILE', 'thapi.cfg'), 'r+')
except:
    print('Couldn\'t open config file, attempting to create.')
    THAPI_CONFIG_FILE = open(os.getenv('THAPI_CONFIG_FILE', 'thapi.cfg'), 'w+')
    CONFIG_BAD = True
# Options to export the loaded configuration as environment variables for Docker
THAPI_ENV_EXPORT = os.getenv('THAPI_ENV_EXPORT', '0') == '1'
if THAPI_ENV_EXPORT:
    THAPI_ENV_EXPORT_FILE = open(os.getenv('THAPI_ENV_EXPORT_FILE', 'lastrun.cfg.sh'), 'w+')

app = Flask(__name__)
CORS(app)# Try to open the config file and parse it
parser = configparser.RawConfigParser()
parser.readfp(THAPI_CONFIG_FILE)

if THAPI_ENV_EXPORT:
    THAPI_ENV_EXPORT_FILE.write('#!/bin/bash\n')

def read_config(section, name, environment_variable, default):
    global CONFIG_BAD
    value = default
    try:
        value = os.getenv(environment_variable, parser.get(section, name))
    except Exception as e:
        if not parser.has_section(section):
            parser.add_section(section)
        CONFIG_BAD = True
        print('[' + section + ']->' + name + ' is missing. Your config will be regenerated with it included after execution.')
        parser.set(section, name, default)
        value = default
    if THAPI_ENV_EXPORT:
        THAPI_ENV_EXPORT_FILE.write('export ' + environment_variable + '="' + value + '"\n')
    return value

host = read_config('Server', 'host', 'THAPI_HOST', '0.0.0.0')
port = read_config('Server', 'port', 'THAPI_PORT', '5000')

if (read_config('Development', 'developer', 'THAPI_DEBUG', '0') == '1'):
    debugmode = True
else:
    debugmode = False

dbstr = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    read_config('Database', 'user', 'THAPI_DB_USER', 'root'),
    read_config('Database', 'pass', 'THAPI_DB_PASS', 'password'),
    read_config('Database', 'host', 'THAPI_DB_HOST', '127.0.0.1'),
    read_config('Database', 'port', 'THAPI_DB_PORT', '3306'),
    read_config('Database', 'name', 'THAPI_DB_NAME', 'msr14')
)
api = thapi.THApi(dbstr=dbstr)

"""
ENDPOINTS
"""

@app.route('/test')
def test():
    return Response(response=api.test(),
                    status=200,
                    mimetype="application/json")


@app.route('/participant/<int:id>', methods=['GET', 'DELETE'])
def Participant(id):
    if request.method == 'GET':
        return Response(response=api.getParticipant(id),
                        status=200,
                        mimetype="application/json")
    if request.method == 'DELETE':
        return Response(response=api.deleteParticipant(id),
                        status=200,
                        mimetype="application/json")

@app.route('/participants')
def getParticipants():
    return Response(response=api.getParticipants(),
                    status=200,
                    mimetype="application/json")

@app.route('/prize/<int:id>', methods=['GET', 'DELETE'])
def Prize(id):
    if request.method == 'GET':
        return Response(response=api.getPrize(id),
                        status=200,
                        mimetype="application/json")
    if request.method == 'DELETE':
        return Response(response=api.deletePrize(id),
                        status=200,
                        mimetype="application/json")

@app.route('/prizes')
def getPrizes():
    return Response(response=api.getPrizes(),
                    status=200,
                    mimetype="application/json")
"""
END ENDPOINTS
"""

if (debugmode):
    app.debug = True

if read_config('Development', 'interactive', 'THAPI_INTERACTIVE', '0') == '1':
    ipdb.set_trace()

# Close files and save config
if (CONFIG_BAD):
    print('Regenerating config...')
    THAPI_CONFIG_FILE.seek(0)
    parser.write(THAPI_CONFIG_FILE)

THAPI_CONFIG_FILE.close()
if THAPI_ENV_EXPORT:
    THAPI_ENV_EXPORT_FILE.close()

def run():
    app.run(host=host, port=int(port), debug=debugmode)

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)
        type, value, tb = sys.exc_info()
        traceback.print_exc()
        if (debugmode):
            ipdb.post_mortem(tb)
        exit(1)
