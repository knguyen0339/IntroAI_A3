
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, mac
from backtrack import backtracking_search


for puzzle in [easy1, harder1]:
    s = Sudoku(puzzle)  # construct a Sudoku problem

    # solve as much as possible by AC3 then backtrack search if needed
    # using MRV and MAC.

    AC3_results = AC3(s)

    if not AC3_results:
        print("{}/{}: this sudoku has no solution".format(index, total))
    else:
        if s.isFinished():
            print("{}/{}: AC3 solved this sudoku".format(index, total))
            print("{}/{}: Results: \n{}".format(index, total, s))
        else:
            print("{}/{}: AC3 finished. Backtracking will start".format(index, total))

            assignment = {}

            for cell in s.cells:
                if len(s.possibilities[cell]) == 1:
                    assignment[cell] = s.possibilities[cell][0]

            assignment = backtracking_search(assignment, s)

            for cell in s.possibilities:
                s.possibilities[cell] = assignment[cell] \
                    if len(cell) > 1 \
                    else s.possibilities[cell]

            if assignment:
                print("{}/{}: Results: \n{}".format(index, total, s))
            else:
                print("{}/{}: No solution exists".format(index, total))
    

