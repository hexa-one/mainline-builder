from .check_type import KERNEL_VER_INPUT

def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

VER_STAND = ('0')

if  (KERNEL_VER_INPUT).endswith('.0'): 
    VER_STR = (KERNEL_VER_INPUT).replace(".", "")  
    index = VER_STR.find('Cat')
    VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.1'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")  
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.2'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.3'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.4'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.5'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.6'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.7'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.8'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.9'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Cat')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('-rc1'):   
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc1", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc1')
elif (KERNEL_VER_INPUT).endswith('-rc2'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc2", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc2') 
elif (KERNEL_VER_INPUT).endswith('-rc3'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc3", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc3')
elif (KERNEL_VER_INPUT).endswith('-rc4'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc4", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc4')
elif (KERNEL_VER_INPUT).endswith('-rc5'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc5", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc5') 
elif (KERNEL_VER_INPUT).endswith('-rc6'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc6", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc6')
elif (KERNEL_VER_INPUT).endswith('-rc7'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc7", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc7') 
elif (KERNEL_VER_INPUT).endswith('-rc8'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc8", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc8') 
elif (KERNEL_VER_INPUT).endswith('-rc9'): 
        VER_STAND = (KERNEL_VER_INPUT).replace("-rc9", ".0")  
        VER_EDIT = ((VER_STAND)+'0')
        VER_STR = (VER_EDIT).replace(".", "")
        VER_STR = ((VER_STR)+'rc9')
else: VER_STR = (KERNEL_VER_INPUT).replace(".", "")
