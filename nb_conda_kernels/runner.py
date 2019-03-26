from __future__ import print_function

import os
import sys
import subprocess


def exec_in_env(conda_root, envname, *command):
    # Run the standard conda activation script, and print the
    # resulting environment variables to stdout for reading.
    command = subprocess.list2cmdline(command)
    if sys.platform.startswith('win'):
        activate = os.path.join(conda_root, 'Scripts', 'activate.bat')
        activator = subprocess.list2cmdline(['call', activate, envname])
        ecomm = '{} & {}'.format(activator, command)
        subprocess.Popen(ecomm, shell=True).wait()
    else:
        activate = os.path.join(conda_root, 'bin', 'activate')
        activator = subprocess.list2cmdline(['.', activate, envname])
        ecomm = '{} && exec {}'.format(activator, command)
        ecomm = ['sh' if 'bsd' in sys.platform else 'bash', '-c', ecomm]
        os.execvp(ecomm[0], ecomm)


if __name__ == '__main__':
    exec_in_env(*(sys.argv[1:]))
