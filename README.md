

# Instructions to install and use UV to run these scripts
## (linux and mac)

curl -LsSf https://astral.sh/uv/install.sh | sh
# brew install uv (for mac)
## After you have installed this repo

# Install necessary dependencies to run script
uv sync

# Run the script
uv run local_thresholding_v2.py
