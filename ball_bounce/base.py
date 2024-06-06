import argparse
import json
import os
import time
from display import Display
from shape import Shape
from boundary import Boundary
from recorder import Recorder
import psutil

def load_scenarios(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["scenarios"]

def run_scenario(config, output_dir, record):
    display = Display(640, 480)
    boundary = Boundary(config["rect_x"], config["rect_y"], config["rect_width"], config["rect_height"])
    
    shapes = [Shape(shape_config) for shape_config in config["shapes"]]
    
    recorder = None
    if record:
        output_file = os.path.join(output_dir, config["name"] + ".mp4")
        recorder = Recorder(640, 480, output_file)

    start_time = time.time()
    base_fps = 100
    while display.running and (time.time() - start_time < config["duration"]):
        display.handle_events()
        
        # Check CPU usage and adjust FPS
        # cpu_usage = psutil.cpu_percent(interval=0.1)
        # if cpu_usage > 75:
        #     fps = max(20, base_fps - int((cpu_usage - 75) / 5))
        # else:
        #     fps = base_fps

        fps = base_fps

        for shape in shapes:
            shape.move()
            shape.bounce(boundary)
        frame = display.update_display(shapes, boundary)
        if record:
            recorder.record_frame(display.window)
        display.tick(fps)
    
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
    parser.add_argument('--config', type=str, default='scenarios.json', help='Path to the JSON configuration file.')
    parser.add_argument('--output', type=str, default='output', help='Directory to save the output videos.')
    parser.add_argument('--record', action='store_true', help='Specify this flag to record the simulation.')
    args = parser.parse_args()
    main(args.config, args.output, args.record)
