# Kyle Ziegler 2021
# Read last n lines of a file
# Python 3.9

import os
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--num-lines", help="Number of lines from the end of file to return", type=int, required=True)
parser.add_argument("-f", "--file-name", help="File name", type=str, required=True)

args = parser.parse_args()

# I used a memory profiler from: https://pypi.org/project/memory-profiler/ 
# pip install -U memory_profiler
# python setup.py install
@profile
def read_n_lines(num_lines:int, f_name:str):
    try:
        with open(f_name, 'rb') as f:
            # note that we have to open in binary mode in order to read from the end of the file
            # using readlines will open all lines into memory, how do we handle large files?
            f.seek(-2, os.SEEK_END)
            l = []
            # s = f.readline()
            string = ""

            while True:
                char = f.read(1)
                # print(char)
                
                if (char == b'\n'):
                    l.append(string[::-1])
                    string = ""
                else:
                    string += char.decode('utf8')
                
                f.seek(-2, os.SEEK_CUR)
                
                if (len(l) == num_lines):
                    print(l)
                    return l

                if(f.tell() == 0):
                    print("File is too short to print {} lines.".format(num_lines))
                    return ("File is too short to print {} lines.".format(num_lines))

    except:
        print(sys.exc_info()[0])
        raise
        return

if __name__ == "__main__":
    read_n_lines(args.num_lines, args.file_name)