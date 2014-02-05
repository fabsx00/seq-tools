#!/usr/bin/env python2

from lib.PipeTool import PipeTool
from collections import defaultdict


DESCRIPTION = """Creates a combined histogram for all lines of the
input file in the format token_0:count_0 ...token_n:count_0 """

class Histogram(PipeTool):
    
    def __init__(self, description):
        PipeTool.__init__(self, description)

    def streamStart(self):
        self.d = defaultdict(int)

    def processLine(self, line):
        
        X = [float(x) for x in line.split(' ')]
        for x in X:
            self.d[x] += 1
    
    def streamEnd(self):

        items = [(x[1],x[0]) for x in self.d.iteritems()]
        items.sort()
        
        outStrings = ["%s:%s" % (count, token) for (count, token) in items]
        self.output(' '.join(outStrings) + '\n')


if __name__ == '__main__':
    tool = Histogram(DESCRIPTION)
    tool.run()
