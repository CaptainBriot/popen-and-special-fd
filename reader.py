import os
import sys

fd = int(sys.argv[1])
total = 0

with os.fdopen(fd, 'rb') as fileobj:
    while True:
        data = fileobj.read(1024*1024)
        if not data:
            break
        total += len(data)
        print(total)
print('Reader done')

