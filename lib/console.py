import sys
sys.path.append('../')
from main import VERSION

def print_info():
    print("Version: "+(VERSION))

def get_kernel():
    KERNEL_VER_INPUT = input('Kernel version: ')
    return KERNEL_VER_INPUT