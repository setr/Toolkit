#!/usr/bin/env python2.7
#encoding=UTF-8

__author__ = 'setr'

from TreeGenerator import Node
from TreeGenerator import testCall
from os.path import exists
import codecs
from sys import argv

HEADER = "*"

def getText(fileIn):
    theText = []
    if exists(fileIn):
        with codecs.open(fileIn, 'r', encoding='UTF-8') as r:
            for line in r:
                theText.append(line.strip())
        return theText
    else:
        print "File does not exist"

def getLevel(line):
    if line[0] == HEADER:
        count = 0
        for char in line:
            if char == HEADER:
                count += 1
            else:
                break
        return count
    return None

def cleanLine(line, count):
    return line[count:]

def findPreviousLevelAndAttach(parent, newNode):
    if parent.level == newNode.level-1:
        parent.addChild(newNode)
        return parent
    else:
        return findPreviousLevelAndAttach(parent.Parent, newNode)

def levelChanged(level, lastLevel):
    if level == lastLevel:
        return False
    else:
        return True

def parseText(fileIn):
    theText = getText(fileIn)
    root = Node(None)
    Parent = root
    newNode = Node(None)
    lastLevel = 0

    for line in theText:
        level = getLevel(line)
        line = cleanLine(line, level)
        if level is not None:  # Happens when there's no HEADER on the line
            newNode = Node(line)
            newNode.level = level
            findPreviousLevelAndAttach(Parent, newNode)
            if levelChanged(level, lastLevel):
                Parent = newNode
            lastLevel = level
            if Parent is None:
                print "We shouldn't be here"
        else:
            print "IGNORED LINE:", line
    return root


if __name__ == "__main__":
    if len(argv) == 1:  # apparently an empty args is still of len 1
        testCall()
        root = parseText("testIN.tmp")
        root = root.printAll()
        root.encode("UTF-8")
        print root
    elif len(argv) == 2:
        fileIn = argv[1]
        root = parseText(fileIn)
        temp = root.printAll()
        temp.encode("UTF-8")
        print temp
    elif len(argv) == 3:
        fileIn = argv[1]
        fileOut = argv[2]
        root = parseText(fileIn)
        temp = root.printAll()
        temp.encode("UTF-8")
        with codecs.open(fileOut, 'w', encoding="UTF-8") as w:
            w.write(temp)
# with codecs.open('testOUT', 'w', encoding='UTF-8') as w:
#     w.write(tempStr)
