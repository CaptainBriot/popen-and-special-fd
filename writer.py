import os
import subprocess
import threading
import sys

path = sys.argv[1]
r, w = os.pipe()

def write():
    with os.fdopen(w, 'w') as writer:
        with open(path) as reader:
            while True:
                data = reader.read(10*1024*1024)
                if not data:
                    break
                print('Writing data (size: {})'.format(len(data)))
                writer.write(data)
    print('Writer thread is done')

thread = threading.Thread(target=write)
thread.start()
process = subprocess.Popen(['python', 'reader.py', str(r)])
os.close(r)
thread.join()
process.communicate()

