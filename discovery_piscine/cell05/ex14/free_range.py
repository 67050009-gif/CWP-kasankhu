import sys

if len(sys.argv) == 3:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
    print(list(range(start_num, end_num + 1)))
else:
    print("none")