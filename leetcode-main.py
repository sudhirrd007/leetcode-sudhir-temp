import sys
import json
import os
from pathlib import Path
from dotenv import dotenv_values
import shutil
import string
import sqlite3
import pandas as pd
from _LEETCODE_AUTOMATION.SQLiteManager import SQLiteManager
from _LEETCODE_AUTOMATION.Problem import Problem

CURR_DICT = Path(os.getcwd())

# > Environment File Load
# Load Environment Variables from .env file
envFileLoc = CURR_DICT.joinpath('.env')
ENV_VAR_DICT = dotenv_values(envFileLoc)

# attribute list (Case Sensitive)
ATTRIBUTE_LIST = [key for key, val in ENV_VAR_DICT.items() if val.strip()=='attribute']
ATTRIBUTE_DICT = None
TAG_LIST = [key for key, val in ENV_VAR_DICT.items() if val.strip()=='tag']
DB_NAME = ENV_VAR_DICT['DBNAME']

# > Fetch files from QueueProblemFiles Dir
# Go through every file in "QueueProblemFiles"
CURR_DICT = Path(os.getcwd())
queueProblemFilesLoc = CURR_DICT.joinpath('./_LEETCODE_AUTOMATION/QueueProblemFiles')
if(not queueProblemFilesLoc.exists()):
    raise Exception('QueueProblemFiles does not exist')

dataBaseLoc = CURR_DICT.joinpath('_LEETCODE_AUTOMATION').joinpath('leetcode.db')
sqliteObj = SQLiteManager(dataBaseLoc)

# > Creating "Problem" Object for each file in QueueProblemFiles Dir
# > insert all the attributes of files in SQLite dataBase
for fileLoc in queueProblemFilesLoc.glob('*.py'):
    problemObj = Problem(fileLoc, ATTRIBUTE_LIST)
    ATTRIBUTE_DICT = problemObj.ATTRIBUTE_DICT

    sqliteObj.insertIntoMasterTable(ATTRIBUTE_DICT)





sqliteObj.conn.close()

# Load the SQLite DB file from the local file system




