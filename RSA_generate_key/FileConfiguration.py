import os
import json
import re
from functools import reduce
import operator

class FileConfiguration:

    def __init__(self, path):
        self.path = path + ".json"
        self.writeFile = open(self.path, 'a')
        self.readFile = open(self.path, 'r')

        try:
            self.args = json.load(self.readFile)
        except:
            self.args = {}
    
    def getFromDict(self, dataDict, mapList):
        return reduce(operator.getitem, mapList, dataDict)

    def setInDict(self, dataDict, maplist, value):
        self.getFromDict(dataDict, maplist[:-1])[maplist[-1]] = value

    def set(self, path, arg):
        path2 = path.split('.')
        length = len(path2)
        try:
            self.setInDict(self.args, path2, arg)
        except:
            currentpath = []
            currentpath2 = [path2[0]]
            for i in range(len(path2)):
                currentpath.append(path2[i])
                try:
                    currentpath2.append(path2[i+1])
                except:
                    pass
                try:
                    self.setInDict(self.args, currentpath, {})
                    self.setInDict(self.args, currentpath2, path2[i+1])
                except:
                    pass
            self.set(path, arg)
        
    def get(self, path):
        path2 = path.split('.')
        #print(path2)
        data = self.args
        try:
            for p in path2:
                data = data[p]
            return data
        except:
            #print('Error')
            #s = input("error ")
            return None

    def save(self):
        self.writeFile.close()
        self.readFile.close()
        os.remove(self.path)
        self.writeFile = open(self.path, "a")
        json.dump(self.args, self.writeFile, indent=4)

    def print(self):
        print(json.dumps(self.args))

