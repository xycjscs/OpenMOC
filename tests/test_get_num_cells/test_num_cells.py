#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.pardir)
sys.path.insert(0, os.path.join(os.pardir, 'openmoc'))
from testing_harness import TestHarness
from input_set import PinCellInput


class PinCellTestHarness(TestHarness):
    """An eigenvalue calculation in a pin cell with 7-group C5G7 data."""

    def __init__(self):
        super(PinCellTestHarness, self).__init__()
        self.input_set = PinCellInput()

    def _get_results(self, num_iters=True, keff=True, fluxes=False,
                    num_fsrs=False, num_tracks=False, num_segments=False,
                    hash_output=False):
        result_str = str(self.input_set.geometry.getNumCells())
        return result_str

    def _create_trackgenerator(self):
        pass

    def _generate_tracks(self):
        pass

    def _run_openmoc(self):
        pass


if __name__ == '__main__':
    harness = PinCellTestHarness()
    harness.main()
