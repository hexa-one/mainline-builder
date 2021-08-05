import os
os.chdir('lib/')
KERNEL_VER_INPUT = input('Kernel version: ')

def main():
    if "rc" in (KERNEL_VER_INPUT):
        KERNEL_TYPE=("rc")
        return KERNEL_TYPE

    elif  (KERNEL_VER_INPUT).startswith('5.10'):
        KERNEL_TYPE=("LTS")
        return KERNEL_TYPE

    else: 
        (KERNEL_VER_INPUT) > ('5.10.9999')
        KERNEL_TYPE=("Mainline")
        return KERNEL_TYPE

def build():
    KERNEL_TYPE = main()
    RC=("rc")
    if KERNEL_TYPE == RC:
        from .build import buildrc
        from .build import buildreadme
        buildrc()
        buildreadme()
    else: 
        from .build import buildmain
        from .build import buildreadme
        buildmain()
        buildreadme()