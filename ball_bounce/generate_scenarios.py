import json
import random
import argparse

def generate_random_scenario():
    shapes = ['circle', 'rectangle', 'polygon']
    scenario = {
        "name": f"Scenario {random.randint(1, 1000)}",
        "shape": random.choice(shapes),
        "color_change": random.choice([True, False]),
        "size_change": round(random.uniform(-5.0, 5.0), 2),
        "duration": random.randint(5, 20),
        "rect_x": random.randint(50, 150),
        "rect_y": random.randint(50, 150),
        "rect_width": random.randint(300, 500),
        "rect_height": random.randint(200, 400),
        "speed_increase_factor": round(random.uniform(1.01, 1.05), 2),
        "growth_rate": round(random.uniform(0.01, 0.1), 2),
        "carrying_capacity": round(random.uniform(50.0, 300.0), 2),
        "sides_change": random.randint(0, 3),
        "position_change": random.choice([True, False]),
        "initial_size": round(random.uniform(10.0, 50.0), 2),
        "initial_speed_x": round(random.uniform(1.0, 10.0), 2),
        "initial_speed_y": round(random.uniform(1.0, 10.0), 2)
    }
    return scenario

def generate_scenarios(num_scenarios):
    scenarios = {"scenarios": [generate_random_scenario() for _ in range(num_scenarios)]}
    with (open('scenarios.json', 'w') as file):
        json.dump(scenarios, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random scenarios for bouncing objects.")
    parser.add_argument('num_scenarios', type=int, nargs='?', default=1, help='Number of scenarios to generate.')
    args = parser.parse_args()
    generate_scenarios(args.num_scenarios)
