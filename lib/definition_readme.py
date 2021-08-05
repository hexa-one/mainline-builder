from .get_latest_release import get_latest

mainline, lts, rc = get_latest()

empty=('')

line1=('<div align="center">')
line2=('  <a align="center">')
line3=('    <center align="center">')
line4=('      <img src="assets/Mainline-pink.svg" alt="ubuntumainline" align="center">')
line5=('    </center>')
line6=('  </a>')
line7=('  <br>')
line8=('  <h1 align="center"><center>Ubuntumainline</center></h1>')
line9=('  <h3 align="center"><center>Script for installing the latest mainline kernel on ubuntu and ubuntu based distros.</center></h3>')
line10=line7
line11=line7
line12=('</div>')
line13=empty
line14=('## installation')
line15=empty
line16=('### requirements')
line17=empty
line18=('- You wanna have [curl](https://curl.haxx.se/) and [wget](https://www.gnu.org/software/wget/) installed. If not you can do it by `sudo apt install curl wget`.')
line19=('- Its recommended to make a backup of your grub.cfg you can do it by `sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg.bak`.')
line20=("- **!** Note these kernels don't work with nvidia drivers. Your pc won't display on boot.")
line21=empty
line22=('### amd64')
line23=empty
line24=('**mainline kernel '+(mainline)+'**')
line25=empty
line26=('```bash')
line27=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/'+(mainline)+'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
line28=('```')
line29=('**lts kernel '+(lts)+'**')
line30=empty
line31=line26
line32=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/'+(lts)+'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
line33=line28
line34=empty
line35=('**rc kernel '+(rc)+'**')
line36=line26
line37=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/'+(rc)+'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
line38=line28
line39=empty
line40=('### arm64')
line41=empty
line42=line24
line43=line26
line44=(line27).replace("-amd", "-arm")
line45=line28
line46=empty
line47=line29
line48=line26
line49=(line32).replace("-amd", "-arm")
line50=line28
line51=empty
line52=line35
line53=line26
line54=(line37).replace("-amd", "-arm")
line55=line28
line56=empty
line57=('## catalog')
line58=empty
line59=('- want a older kernel go to [`catalog page`](../catalog/README.md).')
line60=empty
line61=('## info')
line62=empty
line63=('- [`gitlab mirror`](https://gitlab.com/hexa-one/ubuntumainline)')
line64=('- kernel by [`https://kernel.ubuntu.com`](https://kernel.ubuntu.com/)')
line65=empty
line66=('# License')
line67=empty
line68=('<a href="https://opensource.org/licenses/MIT">')
line69=('  <img align="right" height="96" alt="MIT License" src="https://user-images.githubusercontent.com/58103738/119219770-af322980-bad6-11eb-9fa4-4273ca3993b5.png" />')
line70=('</a>')
line71=empty
line72=('Ubuntumainline and its components are licensed under the **MIT License**.')
line73=empty
line74=('The full text of the license can be accessed via [this link](https://opensource.org/licenses/MIT) and is also included in the [license.md](license.md) file of this software package.')