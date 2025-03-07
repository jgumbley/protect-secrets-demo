#!/bin/bash
# Simple demo script showing how to run the secrets examples

# This is the key part showing how environment variables are passed to the Python script
# The variables are set just for this command and not persisted in the shell
API_URL="https://api.example.com/data" \
API_KEY="aJ2pRq7Xz9B4tY6vE8sK3dL5mN1oP0wQ_cF3gH5jI7kZ" \
python env_secrets.py