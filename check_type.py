from line_con import KERNEL_VER_INPUT

if "rc" in (KERNEL_VER_INPUT):
    KERNEL_TYPE=("rc")
    print(KERNEL_TYPE)
elif  (KERNEL_VER_INPUT).startswith('5.10'):
    KERNEL_TYPE=("LTS")
    print(KERNEL_TYPE)
else: 
    (KERNEL_VER_INPUT) > ('5.10.9999')
    KERNEL_TYPE=("Mainline")
    print(KERNEL_TYPE)