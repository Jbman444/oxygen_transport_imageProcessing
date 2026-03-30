#This case uses UV python package manager

##Instructions to install and use UV to run these scripts (linux and mac instructions)

curl -LsSf https://astral.sh/uv/install.sh | sh

##After you have installed this repo

# Install necessary depedencies to run script
uv sync

# Run the script
uv run python local_thresholding_v2.py
