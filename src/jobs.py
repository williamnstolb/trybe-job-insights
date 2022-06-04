from functools import lru_cache
import csv


@lru_cache
def read(path):
    list = []
    with open(path, encoding="utf-8") as file:
        readerFile = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = readerFile

    for dataRow in data:
        dataDict = {}
        for index in range(len(header)):
            dataDict[header[index]] = dataRow[index]
        list.append(dataDict)
    return list
