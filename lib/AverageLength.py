
from lib.PipeTool import PipeTool

DESCRIPTION = """Calculates the average length of incoming sequences """

class AverageLength(PipeTool):
    
    def __init__(self):
        PipeTool.__init__(self, DESCRIPTION)

    def streamStart(self):
        self.lenSum = 0
        self.N = 0

    def processLine(self, line):
        seq = line.split(' ')[3:]
        self.lenSum += len(seq)
        self.N += 1
        
    def streamEnd(self):
        if self.N == 0:
            return
        
        average = float(self.lenSum) / self.N
        self.output(str(average) + '\n')
    
