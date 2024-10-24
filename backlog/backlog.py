import sys
import shutil
from datetime import datetime

backlogfile = "backlog.txt"
archivedfile = "backlog_done"
splitter = " ~ "

# Return a list of tuple
# First element is the flag, second element is the value


def getFlags(args: tuple) -> (list, str):
    flagged = False
    result = list()
    trimmedStr = ""
    for token in args:
        if flagged:
            result.append((flag, token))
            flagged = False
        elif token[0] == '~':
            flag = token[1:]
            flagged = True
        else:
            if (trimmedStr != ""):
                trimmedStr += " "
            trimmedStr += token
    return (result, trimmedStr)


def getBackLog(filename: str) -> str:
    try:
        result = ""
        stream = open(filename, "r")
        linenum = 0
        line = "/n"
        while True:
            line = stream.readline()
            if (line == ''):
                break
            linenum += 1
            result += str(linenum) + splitter + line
        stream.close()
        return result
    except:
        return ""


def showBackLog() -> None:
    print("\n## BACKLOG ##\n")
    print(getBackLog("backlog.txt"))
    print("\n## END ##\n")


def concatToFile(string: str, filename) -> bool:
    if (string == "" or string == "\n"):
        return True
    try:
        f = open(filename, "a")
        f.write(string)
        return True
    except Exception as ex:
        print(ex)
        return False
    finally:
        f.close()


def deleteLineNumber(filename: str, linenumber: int) -> str:
    toReturn = ""
    try:
        shutil.copyfile(filename, filename+".bac")
        data = getBackLog(filename)
        f = open(filename, "w")
        for item in data.split("\n"):
            num = item.split(splitter)
            if (num[0] == ''):
                break
            if (int(num[0]) == linenumber):
                toReturn = num[1]
                continue
            f.write(num[1]+"\n")
    except Exception as ex:
        print(ex)
        return ""
    finally:
        f.close()
    return toReturn


def markAsDone(inputFile: str, archiveFile: str, line: int):
    line = deleteLineNumber(inputFile, line) + splitter + str(datetime.now()) + "\n"
    return concatToFile(line, archivedfile)


(flagList, string) = getFlags(sys.argv[1:])
if not flagList and not string:
    showBackLog()
elif not flagList:
    concatToFile(string + "\n", backlogfile)
elif flagList[0][0] == "done":
    if (not markAsDone(backlogfile, archivedfile, int(flagList[0][1]))):
        print("Save failed")
elif flagList[0][0] == "del":
    deleteLineNumber(backlogfile, int(flagList[0][1]))
else:
    print("Invalid flag")