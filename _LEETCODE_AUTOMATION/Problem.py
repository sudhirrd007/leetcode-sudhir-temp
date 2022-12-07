from pathlib import Path

class Problem:
    def __init__(self, fileLoc, ATTRIBUTE_LIST) -> None:
        if(not Path(fileLoc)):
            raise Exception(f"{fileLoc} does not exist")
        self.fileLoc = fileLoc

        self.ATTRIBUTE_DICT = self.listToDict(ATTRIBUTE_LIST)
        self.fetchFileData()
        
        # self.organizeAttributeDict() # ! commenting this line for now

    def listToDict(self, ATTRIBUTE_LIST) -> dict:
        """
        This function takes the list of attributes and returns a dictionary with the attributes as keys
        """
        return {attribute: None for attribute in ATTRIBUTE_LIST}

    def fetchFileData(self) -> None:
        """
        This function reads the file and returns the data in {ATTRIBUTE_DICT}.
        """
        with open(self.fileLoc, 'r') as file:
            # go through each line in the file
            for line in file:
                # go through each attribute
                for attribute in self.ATTRIBUTE_DICT.keys():
                    # get the value of the attribute and store it in the dictionary
                    if(attribute in line):
                        # attributr name is case sensitive
                        self.ATTRIBUTE_DICT[attribute] = line.split('=')[1].strip()
                        break
                if('END-SRD' in line):
                    break

    
    def organizeAttributeDict(self) -> None:
        """
        This function organizes the values of attributes in the {ATTRIBUTE_DICT}
        """
        for attribute in self.ATTRIBUTE_DICT.keys():
            # attributr name is case sensitive
            if(attribute == 'TAGS'):
                    tagsStrTmp = self.ATTRIBUTE_DICT[attribute].split(',')
                    self.ATTRIBUTE_DICT[attribute] = [tag.strip() for tag in tagsStrTmp]