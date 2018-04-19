import pandas as pd
import sqlalchemy as s
import numpy as np
import json

class THApi(object):
    """Uses TigerHacks database to return JSON data"""

    def __init__(self, dbstr):
        """
        Connect to database

        :param dbstr: The [database string](http://docs.sqlalchemy.org/en/latest/core/engines.html) to connect to the database
        """
        self.DB_STR = dbstr
        self.db = s.create_engine(dbstr, poolclass=s.pool.NullPool)
        #If doesn't work, run a test with a SQL command

    def test(self):
        data = {}
        data['test'] = 'success'
        return json.dumps(data)
    def getParticipant(self, id):
        data = {}
        data['id'] = id
        return json.dumps(data)