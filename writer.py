import os
import threading
import sys

import subprocess32 as subprocess

path = sys.argv[1]
r, w = os.pipe()

def write():
    with os.fdopen(w, 'wb') as writer:
        with open(path, 'rb') as reader:
            while True:
                data = reader.read(10*1024*1024)
                if not data:
                    break
                print('Writing data (size: {})'.format(len(data)))
                writer.write(data)
    print('Writer thread is done')

thread = threading.Thread(target=write)
thread.start()

cmd = [sys.executable, 'reader.py', str(r)]
process = subprocess.Popen(cmd, pass_fds=[r])

os.close(r)
thread.join()
process.communicate()

