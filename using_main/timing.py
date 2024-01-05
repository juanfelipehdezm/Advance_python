print("Loading timing.....")
"""
Times how long a snippet of code takes to run
over multiple iterations
"""

import time
from collections import namedtuple
import argparse

Timing = namedtuple("Timing", "repeats elapsed average")

def timeit(code, repeats= 10):
    compile_code = compile(code, filename='<string>', mode="exec")
    start = time.perf_counter()

    for _ in range(repeats):
        exec(compile_code)

    end = time.perf_counter()

    elapsed = end - start
    average = elapsed / repeats

    return Timing(repeats, elapsed, average)

#this is used we execute the code from the console

if __name__ == "__main__":
    # get code, and repeat from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code",
                        type=str,
                        help="the python code snippet to time")
    parser.add_argument("-r", "--repeats",
                        type=int, default=10,
                        help="Number of time to repeat the code")
    
    args = parser.parse_args()
    #print(args.code)
    #print(args.repeats)

    print(f"timing... {args.code}")
    print(timeit(code=str(args.code), repeats=args.repeats))
    
    #code used : py timing.py "[x**2 for x in range(1000)]" -r 20