# Autonav Final Task

## Clone the Repository
Clone this repository into the correct subdirectory of your ROS2 workspace. Ensure you clone it correctly, or some files might not work.

```bash
git clone https://github.com/yourusername/your-repo.git
```

## Build the Package
After cloning the repository, build only the `autonav` package. Alternatively, you can build all packages and see what happens.

```bash
colcon build --packages-select autonav
```

Or, to build everything:

```bash
colcon build
```

## Launch the Robot
Once the `autonav` package is built, run the following command:

```bash
ros2 launch autonav robot.launch.py
```

## Troubleshooting
You might encounter some errors—it's up to you to debug and resolve them!

