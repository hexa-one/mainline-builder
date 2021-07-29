import os
os.chdir('lib/')
KERNEL_VER_INPUT = input('Kernel version: ')

def main():
    if "rc" in (KERNEL_VER_INPUT):
        KERNEL_TYPE=("rc")
        if os.path.isfile('cache.py'):
           os.remove('cache.py')
           line1 = ("KERNEL_TYPE = ('")
           out = open("cache.py", 'w')
           head1 = lambda *x, **y: print(*x, **y, file=out)  
           head1((line1)+(KERNEL_TYPE)+"')")   
        else:
           line1 = ("KERNEL_TYPE = ('")
           out = open("cache.py", 'w')
           head1 = lambda *x, **y: print(*x, **y, file=out)  
           head1((line1)+(KERNEL_TYPE)+"')")   
    elif  (KERNEL_VER_INPUT).startswith('5.10'):
        KERNEL_TYPE=("LTS")
        if os.path.isfile('cache.py'):
           os.remove('cache.py')
           line1 = ("KERNEL_TYPE = ('")
           out = open("cache.py", 'w')
           head1 = lambda *x, **y: print(*x, **y, file=out)  
           head1((line1)+(KERNEL_TYPE)+"')")   
        else:
           line1 = ("KERNEL_TYPE = ('")
           out = open("cache.py", 'w')
           head1 = lambda *x, **y: print(*x, **y, file=out)  
           head1((line1)+(KERNEL_TYPE)+"')")       
    else: 
        (KERNEL_VER_INPUT) > ('5.10.9999')
        KERNEL_TYPE=("Mainline")
        if os.path.isfile('cache.py'):
           os.remove('cache.py')
           line1 = ("KERNEL_TYPE = ('")
           out = open("cache.py", 'w')
           head1 = lambda *x, **y: print(*x, **y, file=out)  
           head1((line1)+(KERNEL_TYPE)+"')")   
        else:
           line1 = ("KERNEL_TYPE = ('")
           out = open("cache.py", 'w')
           head1 = lambda *x, **y: print(*x, **y, file=out)  
           head1((line1)+(KERNEL_TYPE)+"')")   

def build():
    from .cache import KERNEL_TYPE
    RC=("rc")
    if KERNEL_TYPE == RC:
        from .build import buildrc
        buildrc()
    else: 
        from .build import buildmain
        buildmain()