# Ball Bounce

![](/example.gif)

This project simulates bouncing shapes within a defined boundary. Each shape is assigned a unique piano note that plays when the shape collides with the boundary. The shapes can grow, change color, and vary in speed. The game speed adjusts dynamically based on CPU usage to prevent crashes.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Configuration](#configuration)
- [Scripts](#scripts)
- [Contributing](#contributing)
- [License](#license)

## Features

- Simulates multiple shapes (circle, rectangle, polygon) bouncing within a boundary.
- Shapes can grow, change color, and vary in speed.
- Each shape is assigned a unique piano note that plays upon collision with the boundary.
- Supports generating random scenarios with customizable parameters.
- Ability to record the simulation.
- Dynamic game speed adjustment based on CPU usage to prevent crashes.

## Prerequisites

- Python 3.7+
- `pydub` library
- `psutil` library
- `ffmpeg` for audio processing

## Installation

##### TL;DR

Run

```bash
./install
```

##### Full

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/bouncing-shapes-with-sound.git
    cd bouncing-shapes-with-sound
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install pydub numpy psutil
    ```

4. **Install `ffmpeg`:**
    - **On macOS:**
      ```bash
      brew install ffmpeg
      ```
    - **On Ubuntu:**
      ```bash
      sudo apt-get install ffmpeg
      ```
    - **On Windows:**
      Download and install `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html).

## Usage

### Running the Simulation

- **Run with default settings:**

    ```bash
    ./run
    ```

- **Run and generate random scenarios:**

    ```bash
    ./run-random
    ```

- **Run and generate a specific number of random scenarios:**

    ```bash
    ./run-random 20
    ```

- **Run with recording enabled:**

    ```bash
    ./run --record
    ```

### Generating Scenarios

- **Generate default number of scenarios (10):**

    ```bash
    ./generate-scenarios
    ```

- **Generate a specific number of scenarios:**

    ```bash
    ./generate-scenarios 20
    ```

## Directory Structure

```
ball_bounce/
├── .venv/
├── base.py
├── boundary.py
├── display.py
├── generate-scenarios
├── generate_scenarios.py
├── README.md
├── recorder.py
├── run
├── run-random
├── scenarios.json
├── shape.py
└── sound.py
```

## Configuration

### `scenarios.json`

Each scenario in `scenarios.json` defines the boundary and shapes with their respective properties.

#### Example:

```json
{
    "scenarios": [
        {
            "name": "Scenario 1",
            "duration": 10,
            "rect_x": 100,
            "rect_y": 100,
            "rect_width": 400,
            "rect_height": 300,
            "shapes": [
                {
                    "shape": "circle",
                    "color_change": true,
                    "size_change": 2.5,
                    "speed_increase_factor": 1.03,
                    "growth_rate": 0.05,
                    "carrying_capacity": 250,
                    "sides_change": 0,
                    "initial_size": 30.0,
                    "initial_speed_x": 2.0,
                    "initial_speed_y": 3.0
                },
                {
                    "shape": "rectangle",
                    "color_change": false,
                    "size_change": 1.5,
                    "speed_increase_factor": 1.02,
                    "growth_rate": 0.04,
                    "carrying_capacity": 200,
                    "sides_change": 0,
                    "initial_size": 25.0,
                    "initial_speed_x": 3.0,
                    "initial_speed_y": 2.5
                }
            ]
        }
    ]
}
```

### Shape Properties

- `shape`: Type of shape (`circle`, `rectangle`, `polygon`).
- `color_change`: Whether the shape changes color upon collision.
- `size_change`: Amount by which the shape's size changes.
- `speed_increase_factor`: Factor by which the shape's speed increases upon collision.
- `growth_rate`: Rate at which the shape grows.
- `carrying_capacity`: Maximum size the shape can grow to.
- `sides_change`: Number of sides to change for polygons.
- `initial_size`: Initial size of the shape.
- `initial_speed_x`: Initial speed in the x-direction.
- `initial_speed_y`: Initial speed in the y-direction.

## Scripts

- `generate-scenarios`: Generates random scenarios.
- `run`: Runs the main script.
- `run-random`: Generates random scenarios and runs the main script.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.