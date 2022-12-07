import sqlite3
from pathlib import Path
import os

class SQLiteManager:
    def __init__(self, dataBaseLoc):
        self.dataBaseLoc = dataBaseLoc
        self.dataBaseName = "leetcode.db"
        self.conn = None
        self.cursor = None
        self.createConnection()

        self.masterTableName = 'Problems'
        if(not self.checkMasterTable()):
            self.createMasterTable()

    def createConnection(self):
        self.conn = sqlite3.connect(self.dataBaseLoc)
        self.cursor = self.conn.cursor()

    def checkMasterTable(self):
        flag = self.cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="{self.masterTableName}"')
        return True if flag.fetchall() else False

    def createMasterTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Problems (NUMBER INTEGER PRIMARY KEY, \
        TITLE TEXT NOT NULL, \
        FILENAME TEXT NOT NULL, \
        DIFFICULTY TEXT NOT NULL, \
        LANGUAGE TEXT NOT NULL, \
        TAGS TEXT NOT NULL, \
        LEETCODELINK TEXT NOT NULL, \
        ACCEPTANCERATE INTEGER NOT NULL, \
        NOTES TEXT NOT NULL)")
        self.conn.commit()
        print(f'\n >>> Master Table Created Successfully')

    def insertIntoMasterTable(self, ATTRIBUTE_DICT):
        attributes = []
        values = []
        for key, val in ATTRIBUTE_DICT.items():
            attributes.append(key)
            if(val):
                values.append(f'"{val}"')
            else:
                values.append(f'""')

        query = f'INSERT INTO {self.masterTableName} (' + (", ".join(attributes)) + \
        ') VALUES (' + (", ".join(values)) + ')'

        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f'\n >>> Inserted into master table Successfully - {ATTRIBUTE_DICT["NUMBER"]}')
        except:
            print(f'\n>>> Error in insering (Duplicate Record) - {ATTRIBUTE_DICT["NUMBER"]}')
