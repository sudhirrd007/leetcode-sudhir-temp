from pathlib import Path
import os
import shutil
from SQLiteManager import SQLiteManager
import pandas as pd
import string


CURR_DIR = Path(os.getcwd()).parent
ALPHABET_LIST = list(string.ascii_lowercase)

class ReadMeGenerator:
    def __init__(self):
        self.dataDict = dict()
        self.generateTagWiseFiles()


    def introString(self) -> str:
        introStrLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('METADATA').joinpath('introString.txt')
        with open(introStrLoc, 'r') as file:
            return file.read()


    def indexString(self) -> str:
        INDEX_STRING = "# Index\n"

        for alphabet in ALPHABET_LIST:
            TEMP_INDEX_STRING = ""
            for tag in sorted(list(self.dataDict.keys())):
                if(tag[0].lower() == alphabet):
                    # folderName = self.dataDict[tag]['folderName']
                    title = tag
                    TEMP_INDEX_STRING += f'[{title}](#{title.lower()}) <br> \n'
            if(TEMP_INDEX_STRING):
                INDEX_STRING += f'{alphabet.upper()} <br> \n{TEMP_INDEX_STRING} \n'
        INDEX_STRING += '<hr> \n\n'
        return INDEX_STRING


    def tableString(self) -> str:
        TABLE_STRING = ""
        for tagName in self.dataDict.keys():
            TABLE_STRING += self.getTagWiseContentString(tagName)
        return TABLE_STRING


    def getTableHeaderString(self) -> str:
        introStrLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('METADATA').joinpath('tableHeaderString.txt')
        with open(introStrLoc, 'r') as file:
            return file.read()


    def getTagWiseContentString(self, tagName) -> str:
        ROOT_LOC = Path(__file__).resolve().parent

        CONTENT_STRING = f'# {tagName}\n'
        CONTENT_STRING += self.getTableHeaderString()

        # fileLoc = CURR_DIR.joinpath(tagName).joinpath('FILENAME')

        # TEMPLATE = "| 1 | [Two Sum](./data_files/PROGRAMS/EASY/0001_Two_Sum.py) | EASY | [python](./data_files/PROGRAMS/EASY/0001_Two_Sum.py) | 6948 ms | 46.8% | [Redirect](https://leetcode.com/problems/two-sum) | - |"
        for rowDict in self.dataDict[tagName]:
            fileLoc = f'./{tagName}/' + rowDict['FILENAME']
            # ROOT_LOC.joinpath(tagName).joinpath(rowDict['FILENAME'])

            # ! Custom Exception
            # raise Exception('Sudhir Exception')

            CONTENT_STRING += "| " + str(rowDict['NUMBER'])
            CONTENT_STRING += " | " + "[" + rowDict['TITLE'] + "](" + fileLoc + ")"
            CONTENT_STRING += " | " + str(rowDict['DIFFICULTY'])
            CONTENT_STRING += " | " + "[" + rowDict['LANGUAGE'] + "](" + fileLoc + ")"
            CONTENT_STRING += " | " + str(rowDict['ACCEPTANCERATE'])
            CONTENT_STRING += " | " + "[Redirect](" + rowDict['LEETCODELINK'] + ")"
            CONTENT_STRING += " | " + str(rowDict['NOTES']) + "|\n"

        CONTENT_STRING += "\n[:arrow_up: Back to index](#index) <br><br> \n\n"
        return CONTENT_STRING


    def generateTagWiseFiles(self) -> None:
        dataBaseLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('DATABASE').joinpath('leetcode.db')
        sqliteObj = SQLiteManager(dataBaseLoc)

        # fetching all the records from leetcode.db
        allRecordsDataFrame = sqliteObj.fetchAllRecords()
        
        for _, recordSeries in allRecordsDataFrame.iterrows():
            recordDict = dict(recordSeries)
            tagsList = [tag.strip() for tag in recordDict['TAGS'].split(',')]

            for tag in tagsList:
                if tag not in self.dataDict:
                    self.dataDict[tag] = [recordDict]
                else:
                    self.dataDict[tag].append(recordDict)
        sqliteObj.closeConnection()


    def updateReadMeFile(self) -> None:
        ROOT_LOC = Path(__file__).resolve().parent
        readMeLoc = ROOT_LOC.parent.joinpath('README.md')

        STRING = ""
        STRING += self.introString()
        STRING += self.indexString()
        STRING += self.tableString()

        print(STRING)
        with open(readMeLoc, 'w') as readMeFile:
            readMeFile.write(STRING)

if __name__ == '__main__':
    obj = ReadMeGenerator()
    obj.updateReadMeFile()

