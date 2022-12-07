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
            print(f'>>> + {fileName} -> {dirName}')
        # copy to "All" directory
        destination = CURR_DIR.joinpath('All').joinpath(fileName)
        shutil.copy(fileLoc, destination)
        print(f'>>> + {fileName} -> All')
        self.deleteFile(fileLoc)
    
    def deleteFile(self, fileLoc):
        fileName = fileLoc.name
        destination = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('DATABASE').joinpath('BACKUP_FILES').joinpath(fileName)
        shutil.copy(fileLoc, destination)
        print(f'>>> + {fileName} -> BACKUP_FILES')
        os.remove(fileLoc)
        print(f'>>> - {fileName}')

    def deleteAllFiles(self) -> None:
        """
        This file will be used independently, and not during deployment
        """
        envFileLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('METADATA').joinpath('.env')
        ENV_VAR_DICT = dotenv_values(envFileLoc)

        TAG_LIST_TEMP = [key for key, val in ENV_VAR_DICT.items() if val.strip()=='tag']
        for tagName in TAG_LIST_TEMP:
            for fileLoc in CURR_DIR.joinpath(tagName).glob("*"):
                os.remove(fileLoc)
        
        self.recoverBackUpFiles()
    
    def recoverBackUpFiles(self) -> None:
        """
        This file will be used independently, and not during deployment
        """
        backUpDirLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('DATABASE').joinpath('BACKUP_FILES')
        destinationDirLoc = CURR_DIR.joinpath('LEETCODE_AUTOMATION').joinpath('QueueProblemFiles')
        for fileLoc in backUpDirLoc.glob('*'):
            fileName = fileLoc.name
            destinatin = destinationDirLoc.joinpath(fileName)
            shutil.copy(fileLoc, destinationDirLoc)








