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
        SQL = s.sql.text(" SELECT * FROM Participants WHERE id=" + str(id))
        df = pd.read_sql(SQL, self.db)
        if df.empty:
            message = {}
            message['error'] = 'Not found error'
            return json.dumps(message)
        return df.to_json(orient='records', lines=True)

    def getParticipants(self):
        SQL = s.sql.text(""" SELECT * FROM Participants """)
        df = pd.read_sql(SQL, self.db)
        return df.to_json(orient='records')

    def deleteParticipant(self, id):
        SQL = s.sql.text(" DELETE FROM Participants WHERE id=" + str(id))
        result = self.db.engine.execute(SQL)
        message = {}
        if result.rowcount:
            message['success'] = 'delete success'
        else:
            message['error'] = 'Not found error'
        return json.dumps(message)

    def createPrize(self, description, how_to_win, number_of_prizes, sponsor_name):
        sid = s.sql.text(" SELECT id FROM Sponsors WHERE company_name=" + str(sponsor_name))
        sponsor_id = pd.read_sql(sid, self.db)
        if sponsor_id.empty:
            message = {}
            message['error'] = 'Sponsor not found error'
            return json.dumps(message)
        SQL = s.sql.text(" INSERT INTO Prizes (prize_description, description_to_win, number_of_prizes, sponsor_id) VALUES ('" + str(description) + "', '" + str(how_to_win) + "', " + number_of_prizes + ", " + sponsor_id + ");")
        result = self.db.engine.execute(SQL)
        df = pd.read_sql(SQL, self.db)
        return df.to_json(orient='records')

    def getPrize(self, id):
        SQL = s.sql.text(" SELECT * FROM Prizes WHERE id=" + str(id))
        df = pd.read_sql(SQL, self.db)
        if df.empty:
            message = {}
            message['error'] = 'Not found error'
            return json.dumps(message)
        return df.to_json(orient='records', lines=True)

    def getPrizes(self):
        SQL = s.sql.text(""" SELECT * FROM Prizes """)
        df = pd.read_sql(SQL, self.db)
        return df.to_json(orient='records')

    def deletePrize(self, id):
        SQL = s.sql.text(" DELETE FROM Prizes WHERE id=" + str(id))
        result = self.db.engine.execute(SQL)
        message = {}
        if result.rowcount:
            message['success'] = 'delete success'
        else:
            message['error'] = 'Not found error'
        return json.dumps(message)   

