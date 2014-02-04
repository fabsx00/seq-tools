#!/usr/bin/env python2

from lib.AlignedMeanSequences import AlignedMeanSequences

DESCRIPTION = """Incrementaly calculates a mean and standard deviation
sequence for a stream of sequences. In contrast to meanSequences, this
tool tries to align sequences to the current mean sequence before
updating mean and variance by measuring cross correlation."""

if __name__ == '__main__':
    tool = AlignedMeanSequences(DESCRIPTION)
    tool.run()
    
