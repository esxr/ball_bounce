import argparse
import json
import os
import time
from display import Display
from shape import Shape
from boundary import Boundary
from recorder import Recorder

def load_scenarios(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["scenarios"]

def run_scenario(config, output_dir, record):
    display = Display(640, 480)
    shape = Shape(config)
    boundary = Boundary(config["rect_x"], config["rect_y"], config["rect_width"], config["rect_height"])
    recorder = None
    if record:
        output_file = os.path.join(output_dir, config["name"] + ".mp4")
        recorder = Recorder(640, 480, output_file)

    start_time = time.time()
    while display.running and (time.time() - start_time < config["duration"]):
        display.handle_events()
        shape.move()
        shape.bounce(boundary)
        display.update_display(shape, boundary)
        if record:
            recorder.record_frame(display.window)
        display.tick(60)
    
    if record:
        recorder.release()
    display.stop()

def main(config_file, output_dir, record):
    os.makedirs(output_dir, exist_ok=True)
    scenarios = load_scenarios(config_file)
    for config in scenarios:
        run_scenario(config, output_dir, record)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run bouncing object scenarios.")
    parser.add_argument('--config', type=str, required=True, help='Path to the JSON configuration file.')
    parser.add_argument('--output', type=str, default='output', help='Directory to save the output videos.')
    parser.add_argument('--record', action='store_true', help='Specify this flag to record the simulation.')
    args = parser.parse_args()
    main(args.config, args.output, args.record)
