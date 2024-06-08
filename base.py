import argparse
import json
import os
import time
from display import Display
from shape import Shape
from boundary import Boundary
from recorder import Recorder
from sound import foo, print_collisions
import psutil
import asyncio

def load_scenarios(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["scenarios"]

async def run_scenario(config, output_dir, record, include_sound):
    display = Display(640, 480)
    boundary = Boundary(config["rect_x"], config["rect_y"], config["rect_width"], config["rect_height"])
    
    shapes = [Shape(shape_config) for shape_config in config["shapes"]]
    
    recorder = None
    output_file = None
    if record:
        output_file = os.path.join(output_dir, config["name"] + ".mp4")
        recorder = Recorder(640, 480, output_file)

    start_time = time.time()
    base_fps = 100
    while display.running and (time.time() - start_time < config["duration"]):
        display.handle_events()
        
        fps = base_fps

        for shape in shapes:
            shape.move()
            await shape.bounce(boundary)
        frame = display.update_display(shapes, boundary)
        if record:
            recorder.record_frame(display.window)
        display.tick(fps)
    
    if record:
        recorder.release()
    display.stop()
    
    # Collect collision data and pass it to foo()
    collision_data = []
    for shape in shapes:
        collision_data.extend(shape.get_collisions())
    if include_sound:
        foo(collision_data)
    print_collisions(collision_data)
    
    # Combine the recorded video with the generated audio if sound is included
    if record and include_sound:
        audio_file = "collision_sounds.wav"
        final_output_file = os.path.join(output_dir, config["name"] + "_with_audio.mp4")
        recorder.combine_video_audio(audio_file, final_output_file)
    elif record:
        final_output_file = output_file

def main(config_file, output_dir, record, include_sound):
    os.makedirs(output_dir, exist_ok=True)
    scenarios = load_scenarios(config_file)
    for config in scenarios:
        asyncio.run(run_scenario(config, output_dir, record, include_sound))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run bouncing object scenarios.")
    parser.add_argument('--config', type=str, default='scenarios.json', help='Path to the JSON configuration file.')
    parser.add_argument('--output', type=str, default='output', help='Directory to save the output videos.')
    parser.add_argument('--record', action='store_true', help='Specify this flag to record the simulation.')
    parser.add_argument('--sound', action='store_true', help='Include sound in the recorded video.')
    args = parser.parse_args()
    main(args.config, args.output, args.record, args.sound)
