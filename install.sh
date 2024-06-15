#!/bin/bash

# Check if requirements.txt exists for Python setup
if [ -f "requirements.txt" ]; then
    echo "Setting up Python virtual environment in $(pwd)"
    python -m virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    deactivate
fi

# Check if package.json exists for Node.js setup
if [ -f "package.json" ]; then
    echo "Setting up Node.js environment in $(pwd)"
    npm install
fi

echo "Installation complete in $(pwd)"
