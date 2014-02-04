
from lib.PipeTool import PipeTool
import numpy as np

# This code is based on the online algorithm for calculation of sample
# variance given at:
# http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm

class MeanSequences(PipeTool):

    def __init__(self, DESCRIPTION):
        PipeTool.__init__(self, DESCRIPTION)
        
    def streamStart(self):
        self.maxLen = 0
        
        self.n = 0
        self.mean = []
        self.M2 = []
            
    def processLine(self, line):
        
        seq = [float(x) for x in line.split(' ')]
        seq = self._doPadding(seq)
        self._updateValues(seq)

    def _doPadding(self, seq):
        
        """
        Pad either new sample or current mean and M2 and return the
        (possibly padded) sequence in both cases.
        """
        
        seqLen = len(seq)

        if seqLen > self.maxLen:
            self.maxLen = seqLen
            self.mean = self._pad(self.mean, seqLen)
            self.M2 = self._pad(self.M2, seqLen)
        elif seqLen < self.maxLen:
            seq = self._pad(seq, self.maxLen)
        return seq
        
    def _pad(self, X, newLen):
        X += [float(0)]*(newLen - len(X))
        return X

    def _updateValues(self, seq):
        
        self.n += 1
        meanAr = np.array(self.mean)
        X = np.array(seq)
        delta = X - meanAr
        meanAr = meanAr + delta / float(self.n)
        self.M2 = (self.M2 + delta * (X - meanAr)).tolist()
        self.mean = meanAr.tolist()

    def streamEnd(self):
        
        self.standardDev = np.array([0]*len(self.mean))
        if self.n != 1:
            self.standardDev = np.sqrt(self._divideByScalar(self.M2, self.n - 1))
        
        self._outputMeanAndDeviation()

    def _outputMeanAndDeviation(self):
        print ' '.join([str(x) for x in self.mean])
        print ' '.join([str(x) for x in self.standardDev])
        
    def _divideByScalar(self, X, scalar):
        return [float(x) / float(scalar) for x in X]
