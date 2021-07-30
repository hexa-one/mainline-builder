from .check_type import KERNEL_VER_INPUT
from .definition import VER_STR, VER_STAND
import subprocess as sp
import os

VER_STR = ('0'+(VER_STR))
FILE = ('index.html')

def main():
    from .check_type import main
    KERNEL_TYPE = main()
    os.system('wget -O '+(FILE)+' https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/')
    RC=("rc")
    if KERNEL_TYPE == RC:
        rc()
    else: 
        mainline()

def mainline():
    amd64_1 = sp.getoutput('grep "amd64/linux-headers-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'-generic_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'" '+(FILE)+'')
    amd64_1 = (amd64_1).replace('&nbsp;&nbsp;<a href="', "")
    amd64_1, sep, tail = amd64_1.partition('">')
    amd64_1 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_1))
    amd64_2 = sp.getoutput('grep "amd64/linux-headers-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_2 = (amd64_2).replace('&nbsp;&nbsp;<a href="', "")
    amd64_2, sep, tail = amd64_2.partition('">')
    amd64_2 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_2))   
    amd64_3 = sp.getoutput('grep "amd64/linux-image-unsigned-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'-generic_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_3 = (amd64_3).replace('&nbsp;&nbsp;<a href="', "")
    amd64_3, sep, tail = amd64_3.partition('">')
    amd64_3 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_3))   
    amd64_4 = sp.getoutput('grep "amd64/linux-modules-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'-generic_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_4 = (amd64_4).replace('&nbsp;&nbsp;<a href="', "")
    amd64_4, sep, tail = amd64_4.partition('">')
    amd64_4 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_4))   
    arm64_1 = sp.getoutput('grep "arm64/linux-headers-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'-generic_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'." '+(FILE)+'')
    arm64_1 = (arm64_1).replace('&nbsp;&nbsp;<a href="', "")
    arm64_1, sep, tail = arm64_1.partition('">')
    arm64_1 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(arm64_1))    
    arm64_2 = sp.getoutput('grep "arm64/linux-image-unsigned-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'-generic_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'." '+(FILE)+'')
    arm64_2 = (arm64_2).replace('&nbsp;&nbsp;<a href="', "")
    arm64_2, sep, tail = arm64_2.partition('">')
    arm64_2 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(arm64_2))    
    arm64_3 = sp.getoutput('grep "amd64/linux-modules-'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'-generic_'+(KERNEL_VER_INPUT)+'-'+(VER_STR)+'." '+(FILE)+'')
    arm64_3 = (arm64_3).replace('&nbsp;&nbsp;<a href="', "")
    arm64_3, sep, tail = arm64_3.partition('">')
    arm64_3 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(arm64_3))    
    return amd64_1, amd64_2, amd64_3, amd64_4, arm64_1, arm64_2, arm64_3

def rc():
    amd64_1 = sp.getoutput('grep "amd64/linux-headers-'+(VER_STAND)+'-'+(VER_STR)+'-generic_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_1 = (amd64_1).replace('&nbsp;&nbsp;<a href="', "")
    amd64_1, sep, tail = amd64_1.partition('">')
    amd64_1 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_1))
    amd64_2 = sp.getoutput('grep "amd64/linux-headers-'+(VER_STAND)+'-'+(VER_STR)+'_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_2 = (amd64_2).replace('&nbsp;&nbsp;<a href="', "")
    amd64_2, sep, tail = amd64_2.partition('">')
    amd64_2 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_2))  
    amd64_3 = sp.getoutput('grep "amd64/linux-image-unsigned-'+(VER_STAND)+'-'+(VER_STR)+'-generic_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_3 = (amd64_3).replace('&nbsp;&nbsp;<a href="', "")
    amd64_3, sep, tail = amd64_3.partition('">')
    amd64_3 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_3))
    amd64_4 = sp.getoutput('grep "amd64/linux-modules-'+(VER_STAND)+'-'+(VER_STR)+'-generic_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    amd64_4 = (amd64_4).replace('&nbsp;&nbsp;<a href="', "")
    amd64_4, sep, tail = amd64_4.partition('">')
    amd64_4 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(amd64_4))
    arm64_1 = sp.getoutput('grep "arm64/linux-headers-'+(VER_STAND)+'-'+(VER_STR)+'-generic_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    arm64_1 = (arm64_1).replace('&nbsp;&nbsp;<a href="', "")
    arm64_1, sep, tail = arm64_1.partition('">')
    arm64_1 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(arm64_1))
    arm64_2 = sp.getoutput('grep "arm64/linux-image-unsigned-'+(VER_STAND)+'-'+(VER_STR)+'-generic_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    arm64_2 = (arm64_2).replace('&nbsp;&nbsp;<a href="', "")
    arm64_2, sep, tail = arm64_2.partition('">')
    arm64_2 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(arm64_2)) 
    arm64_3 = sp.getoutput('grep "arm64/linux-modules-'+(VER_STAND)+'-'+(VER_STR)+'-generic_'+(VER_STAND)+'-'+(VER_STR)+'." '+(FILE)+'')
    arm64_3 = (arm64_3).replace('&nbsp;&nbsp;<a href="', "")
    arm64_3, sep, tail = arm64_3.partition('">')
    arm64_3 = ('https://kernel.ubuntu.com/~kernel-ppa/mainline/v'+(KERNEL_VER_INPUT)+'/'+(arm64_3))
    return amd64_1, amd64_2, amd64_3, amd64_4, arm64_1, arm64_2, arm64_3