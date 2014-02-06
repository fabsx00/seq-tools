#!/usr/bin/env python2

from lib.PipeTool import PipeTool

DESCRIPTION = """Extracts sub sequences from sequence using a sliding
window"""

class SequencePartitioner(PipeTool):

    def __init__(self):
        PipeTool.__init__(self, DESCRIPTION)

        self.argParser.add_argument('-w', '--window', type=int,
                                    default=5,
                                    help="""The size of the sliding
                                    window. Default: 5.""")
        self.argParser.add_argument('-s', '--step', type=int,
                                    default=1,
                                    help="""The step size of the sliding
                                    window. Default: 1.""")

    def processLine(self, line):

        sequence = line.strip().split(' ')
        start = 0
        end = start + self.args.window

        while start < len(sequence) - self.args.window:
            window = sequence[start:end]
            start += self.args.step
            end = start + self.args.window
            win_str = ' '.join(window) + '\n'
            self.output(win_str)

if __name__ == '__main__':
    tool = SequencePartitioner()
    tool.run()
