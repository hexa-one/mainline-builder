from .get_latest_release import get_latest

mainl, lts, rc = get_latest()

empty=('')

l1=('<div align="center">')
l2=('  <a align="center">')
l3=('    <center align="center">')
l4=('      <img src="assets/Mainl-pink.svg" alt="ubuntumainline" align="center">')
l5=('    </center>')
l6=('  </a>')
l7=('  <br>')
l8=('  <h1 align="center"><center>Ubuntumainline</center></h1>')
l9=('  <h3 align="center"><center>Script for installing the latest mainl kernel on ubuntu and ubuntu based distros.</center></h3>')
l10=l7
l11=l7
l12=('</div>')
l13=empty
l14=('## installation')
l15=empty
l16=('### requirements')
l17=empty
l18=('- You wanna have [curl](https://curl.haxx.se/) and [wget](https://www.gnu.org/software/wget/) installed. If not you can do it by `sudo apt install curl wget`.')
l19=('- Its recommended to make a backup of your grub.cfg you can do it by `sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg.bak`.')
l20=("- **!** Note these kernels don't work with nvidia drivers. Your pc won't display on boot.")
l21=empty
l22=('### amd64')
l23=empty
l24=('**mainl kernel '+(mainl)+'**')
l25=empty
l26=('```bash')
l27=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/'+(mainl)+'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
l28=('```')
l29=('**lts kernel '+(lts)+'**')
l30=empty
l31=l26
l32=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/'+(lts)+'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
l33=l28
l34=empty
l35=('**rc kernel '+(rc)+'**')
l36=l26
l37=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/'+(rc)+'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
l38=l28
l39=empty
l40=('### arm64')
l41=empty
l42=l24
l43=l26
l44=(l27).replace("-amd", "-arm")
l45=l28
l46=empty
l47=l29
l48=l26
l49=(l32).replace("-amd", "-arm")
l50=l28
l51=empty
l52=l35
l53=l26
l54=(l37).replace("-amd", "-arm")
l55=l28
l56=empty
l57=('## catalog')
l58=empty
l59=('- want a older kernel go to [`catalog page`](../catalog/README.md).')
l60=empty
l61=('## info')
l62=empty
l63=('- [`gitlab mirror`](https://gitlab.com/hexa-one/ubuntumainline)')
l64=('- kernel by [`https://kernel.ubuntu.com`](https://kernel.ubuntu.com/)')
l65=empty
l66=('# License')
l67=empty
l68=('<a href="https://opensource.org/licenses/MIT">')
l69=('  <img align="right" height="96" alt="MIT License" src="https://user-images.githubusercontent.com/58103738/119219770-af322980-bad6-11eb-9fa4-4273ca3993b5.png" />')
l70=('</a>')
l71=empty
l72=('Ubuntumainline and its components are licensed under the **MIT License**.')
l73=empty
l74=('The full text of the license can be accessed via [this link](https://opensource.org/licenses/MIT) and is also included in the [license.md](license.md) file of this software package.')