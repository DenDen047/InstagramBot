import time
import subprocess


while True:

    try:
        res = subprocess.check_call('./run.sh')
    except:
        print("Error.")

    time.sleep(3600 * 1.5)
