from pathlib import Path
import os
import shutil
from dotenv import dotenv_values

CURR_DIR = Path(os.getcwd()).parent

class FolderManager:
    def __init__(self, TAG_LIST):
        self.TAG_LIST = TAG_LIST

    def checkAllDirectory(self) -> bool:
        for tag in self.TAG_LIST:
            self.checkDirExistence(tag)

    def checkDirExistence(self, dirName) -> bool:
        if(not CURR_DIR.joinpath(dirName).exists()):
            os.mkdir(CURR_DIR.joinpath(dirName))

    def copyToDirs(self, fileLoc, dirNameList):
        fileName = fileLoc.name
        for dirName in dirNameList:
            destination = CURR_DIR.joinpath(dirName).joinpath(fileName)
            shutil.copy(fileLoc, destination)
        # copy to "All" directory
        destination = CURR_DIR.joinpath('All').joinpath(fileName)
        shutil.copy(fileLoc, destination)
        self.deleteFile(fileLoc)
    
    def deleteFile(self, fileLoc):
        fileName = fileLoc.name
        destination = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('DATABASE').joinpath('BACKUP_FILES').joinpath(fileName)
        shutil.copy(fileLoc, destination)
        os.remove(fileLoc)

    def deleteAllFiles(self) -> None:
        """
        This file will be used independently, and not during deployment
        """
        envFileLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('METADATA').joinpath('.env')
        ENV_VAR_DICT = dotenv_values(envFileLoc)

        print(CURR_DIR)
        TAG_LIST_TEMP = [key for key, val in ENV_VAR_DICT.items() if val.strip()=='tag']
        TAG_SET_TEMP = set(TAG_LIST_TEMP) - {'All'}
        for tagName in TAG_SET_TEMP:
            for fileLoc in CURR_DIR.joinpath(tagName).glob("*"):
                os.remove(fileLoc)
        








