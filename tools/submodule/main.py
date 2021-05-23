import os

os.system('git config --global user.email "action@github.com" && git config --global user.name "github-actions" && git clone --recurse-submodules git@github.com/hexa-one/ubuntumainline.git && cd ubuntumainline/mainline-builder && git pull origin main && cd .. && git add --all && git commit -m "Update submodule" && git push')