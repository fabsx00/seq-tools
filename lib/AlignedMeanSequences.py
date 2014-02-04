

from lib.MeanSequences import MeanSequences
import numpy as np

class AlignedMeanSequences(MeanSequences):

    def __init__(self, DESCRIPTION):
        MeanSequences.__init__(self, DESCRIPTION)

    # @Override
    def _updateValues(self, seq):
        
        if np.sum(np.abs(self.mean)) == 0:
            self.mean = seq
        else:
            bestFitIdx = self._getBestAlignment(seq)
            shiftedSeq = self._shiftSequenceBy(seq, bestFitIdx)
            
            MeanSequences._updateValues(self, shiftedSeq)
    
    def _getBestAlignment(self, seq):
        
        if len(self.mean) < len(seq):
            r = np.correlate([1]*10 + self.mean + [1]*10, seq, 'valid')
        else:
            r = np.correlate(self.mean, [1]*10 + seq + [1]*10, 'valid')
        
        bestFitIdx = np.argmax(r)
        return bestFitIdx

    def _shiftSequenceBy(self, seq, amount):
        y = np.roll(seq, amount).tolist()
        if amount <= len(y):
            for i in range(amount):
                y[i] = 0
        return y
