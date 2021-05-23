import os

os.system('export GITHUB_TOKEN=$token')
os.system('git remote set-url upstream https://$token:x-oauth-basic@github.com/hexa-one/mainline-builder.git')
os.system('git remote set-url origin https://$token:x-oauth-basic@github.com/hexa-one/mainline-builder.git')
os.system('git config --global user.email "action@github.com" && git config --global user.name "github-actions" && git clone --recurse-submodules https://github.com/hexa-one/ubuntumainline.git && cd ubuntumainline/mainline-builder && git pull origin main && cd .. && git add --all && git commit -m "Update submodule" && git push')