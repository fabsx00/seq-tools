#!/usr/bin/env python2

from lib.MeanSequences import MeanSequences

DESCRIPTION = """Incrementaly calculates a mean and standard deviation
sequence for a stream of sequences."""

if __name__ == '__main__':
    tool = MeanSequences(DESCRIPTION)
    tool.run()
