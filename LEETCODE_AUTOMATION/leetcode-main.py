import sys
import json
import os
from pathlib import Path
from dotenv import dotenv_values
import shutil
import string
import sqlite3
import pandas as pd
from SQLiteManager import SQLiteManager
from Problem import Problem
from FolderManager import FolderManager

CURR_DIR = Path(os.getcwd())
ALL_DIR = CURR_DIR.parent.joinpath('All')

# > Environment File Load
# Load Environment Variables from .env file
envFileLoc = CURR_DIR.joinpath('METADATA').joinpath('.env')
ENV_VAR_DICT = dotenv_values(envFileLoc)

# attribute list (Case Sensitive)
ATTRIBUTE_LIST = [key for key, val in ENV_VAR_DICT.items() if val.strip()=='attribute']
ATTRIBUTE_DICT = None
TAG_LIST = [key for key, val in ENV_VAR_DICT.items() if val.strip()=='tag']
DB_NAME = ENV_VAR_DICT['DBNAME']

# > Fetch files from QueueProblemFiles Dir
# Go through every file in "QueueProblemFiles"
queueProblemFilesLoc = CURR_DIR.joinpath('QueueProblemFiles')
if(not queueProblemFilesLoc.exists()):
    raise Exception('QueueProblemFiles does not exist')

dataBaseLoc = CURR_DIR.joinpath('DATABASE').joinpath('leetcode.db')
sqliteObj = SQLiteManager(dataBaseLoc)

folderManagerObj = FolderManager(TAG_LIST)
folderManagerObj.checkAllDirectory()


# > Creating "Problem" Object for each file in QueueProblemFiles Dir
# > insert all the attributes of files in SQLite dataBase
for fileLoc in queueProblemFilesLoc.glob('*.py'):

    problemObj = Problem(fileLoc, ATTRIBUTE_LIST)
    ATTRIBUTE_DICT = problemObj.ATTRIBUTE_DICT

    sqliteObj.insertIntoMasterTable(ATTRIBUTE_DICT)

    tagsList = [tag.strip() for tag in ATTRIBUTE_DICT['TAGS'].split(',')]
    folderManagerObj.copyToDirs(fileLoc, tagsList)


sqliteObj.closeConnection()

# raise Exception('Sudhir Stopped the program')
