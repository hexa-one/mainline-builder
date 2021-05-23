empty = ''
empty1 = ' '
wget = '      wget'
cd = '      cd'

KERNEL_VER_INPUT = input('Kernel version: ')

def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

if  (KERNEL_VER_INPUT).endswith('.1'): 
    VER_STR = (KERNEL_VER_INPUT).replace(".", "")  
    index = VER_STR.find('Panda')
    VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.2'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.3'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.4'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.5'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.6'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.7'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.8'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
elif (KERNEL_VER_INPUT).endswith('.9'): 
        VER_STR = (KERNEL_VER_INPUT).replace(".", "")
        index = VER_STR.find('Panda')
        VER_STR = VER_STR[:index] + '0' + VER_STR[index:]
else: VER_STR = (KERNEL_VER_INPUT).replace(".", "")

COMMIT_MSG=('git commit -m "' + (KERNEL_VER_INPUT) + '"')
CONFIG_DIR = ('/.config/mainline/')
CONFIG_FILE = ('mainline.conf')

print("Type the amd64 kernel URL's.")
wget1 = input()
wget2 = input()
wget3 = input()
wget4 = input()
print("Type the arm64 kernel URL's.")
wget5 = input()
wget6 = input()
wget7 = input()


line1=('#! /usr/bin/env bash')
line3=('KERNEL_VER="' + (KERNEL_VER_INPUT) + '"')
line4=('VER_STR="' + '0' + (VER_STR) + '"')
line6=('while [[ $# -gt 0 ]]; do')
line7=('  PROG_ARGS+=("${1}")')
line8=('  case "${1}" in')
line9=('    -amd|--amd64)')
line10=('      mkdir /tmp/ubuntukernel$KERNEL_VER')
line11=('      cd /tmp/ubuntukernel$KERNEL_VER')
line16=('      sudo dpkg -i *.deb')
line18=('      rm -r /tmp/ubuntukernel$KERNEL_VER')
line19=('      if [ -f "/boot/initrd.img-$KERNEL_VER-$VER_STR-generic" ] ')
line20=('      then')
line21=('          echo linux $KERNEL_VER is successfully installed!')
line22=('      else')
line23=('          echo an error occurred while installing')
line24=('      fi')
line25=('      break')
line26=('      ;;')
line27=('    -arm|--arm64)')
line38=('    -r|--remove)')
line39=('      echo only remove kernel if you have a newer one!')
line40=('      sleep 2')
line41=('      sudo apt remove linux-headers-$KERNEL_VER-$VER_STR')
line42=('      sudo apt remove linux-image-unsigned-$KERNEL_VER-$VER_STR-generic ')
line43=('      sudo apt remove linux-modules-$KERNEL_VER-$VER_STR-generic')
line46=('          echo linux $KERNEL_VER is successfully removed!')
line48=('          echo an error occurred while removing linux $KERNEL_VER')
line52=('        esac')
line53=('done')

text1=('# linux ' + (KERNEL_VER_INPUT))
text3=('## amd64')
text5=('### install')
text6=('```bash')
text7=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/' + (KERNEL_VER_INPUT) +'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
text8=(text6).replace("bash", "")
text9=('### remove')
text11=(text7).replace("-amd", "-r")
text13=('## arm64')
text17=(text7).replace("-amd", "-arm")
text25=('kernel by [`https://kernel.ubuntu.com`](https://kernel.ubuntu.com/)')