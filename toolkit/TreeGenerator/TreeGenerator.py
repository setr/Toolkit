#!/usr/bin/env python2.7
# encoding=UTF-8
from sys import argv
from os.path import exists
import codecs
__author__ = 'setr'

TOP_L_CORNER        = u"\u250C"  # ┌
BOTTOM_L_CORNER     = u"\u2514"  # └
VERT_R_SPLIT        = u"\u251C"  # ├
HOR_BOTTOM_SPLIT    = u"\u252C"  # ┬
HORIZONTAL          = u"\u2500"  # ─
VERTICAL            = u"\u2502"  # │

class Node:
    def __init__(self, name):
        self.name = name
        self.children = list()
        self.Parent = None
        self.level = 0

    def addChild(self, node):
        node.Parent = self
        self.children.append(node)

    def find(self, name):
        if self.name == name:
            return self
        elif len(self.children):
            for c in self.children:
                found = c.find(name)
                if found is not None:
                    return found
        return None

    def headerPrint(self, index, end):
        tempString = ""
        iHaveSiblings = True
        if index == 0:
            tempString += TOP_L_CORNER
        elif index == end:
            tempString += BOTTOM_L_CORNER
            iHaveSiblings = False
        else:
            tempString += VERT_R_SPLIT
        tempString += HORIZONTAL + " "
        return tempString, iHaveSiblings

    def normalPrint(self, index, end):
        tempString = ""
        iHaveSiblings = True
        if index == end:
            tempString += BOTTOM_L_CORNER
            iHaveSiblings = False
        else:
            tempString += VERT_R_SPLIT
        tempString += HORIZONTAL + " "
        return tempString, iHaveSiblings

    def vertLine(self, hasSiblings, level):
        tempString = "\n"
        for i in range(0, level-1):
            if hasSiblings[i]:
                tempString += VERTICAL
            else:
                tempString += " "
            tempString += "  "
        return tempString


    def printAll(self):
        tempStr = self.printer("", 0, [])
        return tempStr

    def printer(self, printString, level, siblings):
        end = len(self.children) -1
        if level != 0:
            printString += self.name
        level += 1
        first = True
        if first and len(self.children) == 1:  # In the special case that the header has no siblings
            soloHeader = True
        else:
            soloHeader = False
        for index, node in enumerate(self.children):
            hasSiblings = list(siblings)
            if level == 1:
                if first and len(self.children) == 1:
                    first = False
                    tmpStr, iHaveSiblings = "", False
                else:
                    if not first:  # don't want a newline for the very first header
                        printString += "\n"
                    else:
                        first = False
                    tmpStr, iHaveSiblings = self.headerPrint(index, end)
            else:
                printString += self.vertLine(hasSiblings, level)
                tmpStr, iHaveSiblings = self.normalPrint(index, end)
            printString += tmpStr
            hasSiblings.append(iHaveSiblings)
            printString = node.printer(printString, level, hasSiblings)
        return printString

def testRun():
    root = Node(None)
    H1 = Node("H1")
    data11 = Node("data11")
    data111 = Node("data111")
    data1111 = Node("data1111")
    data111.addChild(data1111)
    data11111 = Node("data11111")
    data1111.addChild(data11111)
    data112 = Node("data112")
    data11.addChild(data111)
    data11.addChild(data112)
    data12 = Node("data12")
    H1.addChild(data11)
    H1.addChild(data12)

    H2 = Node("H2")
    data21 = Node("data21")
    data211 = Node("data211")
    data212 = Node("data212")
    data21.addChild(data211)
    data21.addChild(data212)
    H2.addChild(data21)

    H3 = Node("H3")
    data31 = Node("data31")
    data311 = Node("data311")
    data31.addChild(data311)
    H3.addChild(data31)

    H4 = Node("H4")
    data41 = Node("data41")
    H4.addChild(data41)

    root.addChild(H1)
    root.addChild(H2)
    root.addChild(H3)
    root.addChild(H4)

    temp = root.printAll()
    temp.encode("UTF-8")
    print temp
    return temp

def testCall():
    tempStr = testRun()
    # with codecs.open('testOUT', 'w', encoding="UTF-8") as f:
    #     f.write(tempStr)
