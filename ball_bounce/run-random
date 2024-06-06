#!/bin/bash

# Step 1: Generate random scenarios
echo "Generating random scenarios..."
if [ -z "$1" ]; then
    ./generate-scenarios
else
    ./generate-scenarios "$1"
fi

# Step 2: Shift arguments to remove the first argument (number of scenarios)
shift

# Step 3: Activate the virtual environment and run the main script
echo "Activating the virtual environment..."
source .venv/bin/activate

# Step 4: Run the main script with all provided arguments
echo "Running the main script with generated scenarios..."
python base.py "$@"

# Step 5: Deactivate the virtual environment
deactivate

echo "Execution complete!"
