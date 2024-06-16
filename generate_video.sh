#!/bin/bash

# Generate random scenarios (your existing script)
echo "Generating random scenarios..."
if [ -z "$1" ]; then
    ./generate-scenarios
else
    ./generate-scenarios "$1"
fi

# Shift arguments to remove the first argument (number of scenarios)
shift

# Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate

# Run the main script with all provided arguments
echo "Running the main script with generated scenarios..."
python base.py --record "$@"

# Post-process the video to meet the required specifications
echo "Post-processing video..."
for file in output/*.mp4; do
  ffmpeg -i "$file" -c:v libx264 -profile:v high -level 4.2 -pix_fmt yuv420p -vf "scale=-2:1080,setsar=1:1" -r 30 -b:v 5M -maxrate 5M -bufsize 10M -c:a aac -b:a 128k -ar 48000 -ac 2 -movflags +faststart "output/processed_${file##*/}"
done

# Deactivate the virtual environment
deactivate

echo "Execution complete!"
