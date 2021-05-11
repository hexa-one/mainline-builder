import os

os.system('git config user.name github-actions')
os.system('git config user.email "action@github.com"')
os.system('git clone https://github.com/hexa-one/ubuntumainline.git && cd ubuntumainline/mainline-builder && ls -lah && git pull && cd .. && git add --all && git commit -m "Update submodule" && git push')
