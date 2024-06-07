from pydub import AudioSegment
from pydub.generators import Sine
from datetime import datetime

def foo(collision_data):
    if not collision_data:
        return

    # Calculate the total duration of the sound based on the last collision timestamp
    start_time = collision_data[0][0]
    end_time = collision_data[-1][0]
    total_duration_ms = int((end_time - start_time).total_seconds() * 1000) + 1000  # Add 1 second buffer

    combined = AudioSegment.silent(duration=total_duration_ms)

    for collision in collision_data:
        time, shape_id, note = collision
        start_time_ms = int((time - start_time).total_seconds() * 1000)  # calculate start time in ms
        sine_wave = Sine(note).to_audio_segment(duration=100).apply_gain(-3)  # Generate a sine wave for the note
        combined = combined.overlay(sine_wave, position=start_time_ms)

    combined.export("collision_sounds.wav", format="wav")

def print_collisions(collision_data):
    for data in collision_data:
        print(f"Time: {data[0]}, Shape ID: {data[1]}, Note: {data[2]}")
