import os

os.system('export GITHUB_TOKEN=$GITHUB_TOKEN')
os.system('export GITHUB_ACTOR=$GITHUB_ACTOR')
os.system('git config --global user.email "action@github.com" && git config --global user.name "github-actions" && git clone --recurse-submodules https://github.com/hexa-one/ubuntumainline.git && cd ubuntumainline/mainline-builder && git pull origin main && cd .. && git add --all && git commit -m "Update submodule" && git push "https://$GITHUB_ACTOR:$GITHUB_TOKEN@github.com/hexa-one/ubuntumainline/.git" main')