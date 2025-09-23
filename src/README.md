# Explanation of the Designed Solution

## Introduction

This repository contains the source code and documentation for our autonomous vehicle developed for the **World Robot Olympiad (WRO) Future Engineers 2025** competition. The challenge requires us to design, build, and program a self-driving robot capable of navigating a predefined arena with obstacles, walls, and curves, while demonstrating robustness, adaptability, and engineering creativity. This part of our Github is the most complete one, it includes everything that Piolin needs in order to move.

We designed a solution that integrates LEGO Mindstorms EV3 hardware with Python programming using the Pybricks MicroPython environment. The system was engineered to balance **simplicity, stability, and effectiveness**, ensuring that the robot can consistently detect obstacles and navigate safely without human intervention.

This side of our repository explains in detail the hardware design, sensor strategy, programming logic, control algorithms, and improvements that shaped our final solution. It also describes the key challenges we faced during development and how we addressed them.

---

## Hardware Architecture

As we´ve stated before, The robot is based on a **LEGO EV3 Brick** combined with LEGO Technic elements to create a compact but stable chassis. The structure was designed to maintain balance while allowing precise control over steering and forward motion.

- **Motors**
  - **Motor A (Large Motor)** is dedicated to propulsion. It provides constant forward movement at a configurable speed (`SPEED_A`).  
  - **Motor B (Medium Motor)** is dedicated to steering. Instead of using differential drive (two wheels with independent speeds), our design uses a *servo-like steering mechanism* where Motor B rotates left or right to change direction, mimicking real car steering.

- **Sensors**
  - **Ultrasonic Sensor (Port S2, right side)**: Detects obstacles and walls on the right side of the robot.  
  - **Ultrasonic Sensor (Port S3, left side)**: Detects obstacles and walls on the left side of the robot.  
  Using two ultrasonic sensors allows the robot to decide in which direction to steer when approaching an obstacle.

- **Power and Connectivity**
  - The EV3 Brick provides power and computing. No external modules are required, ensuring compliance with WRO rules.

This hardware setup strikes a balance between **mechanical simplicity** and **functional effectiveness**, making it robust enough to handle unpredictable paths in the competition arena.

---

## Control Logic

The logic of the robot was designed around three main behaviors:

1. **Forward Motion**  
   - Motor A runs continuously at a constant speed. This ensures that the robot always moves forward unless stopped manually.  
   - Speed can be tuned in the configuration section of the code.

2. **Obstacle Avoidance**  
   - The robot continuously reads the distance from both ultrasonic sensors.  
   - If the **left sensor detects an obstacle within the threshold (`DIST_MIN`)**, Motor B rotates right, steering away from the obstacle.  
   - If the **right sensor detects an obstacle**, Motor B rotates left.  
   - This logic ensures that the robot does not collide with walls or obstacles.

3. **Auto-Centering (Return to Neutral Position)**  
   - A major improvement to our design was ensuring that the steering motor (Motor B) always returns to its **initial neutral position** when no obstacles are detected.  
   - Without this correction, the robot might drift after avoiding an obstacle, eventually leaving the intended path.  
   - We implemented a **proportional control algorithm (P-controller)**:  
     - The algorithm calculates the error between the motor’s current angle and its initial angle.  
     - Based on the error, a corrective speed is applied to steer Motor B back to neutral.  
     - The correction is **faster when the error is large** and **slower when the error is small**, achieving both speed and smoothness.  
     - A maximum speed limit prevents the motor from moving too aggressively.  
   - This approach simulates servo-like behavior, allowing the robot to self-stabilize after each turn.

---

## Software Architecture

The software is written in **Python using the Pybricks MicroPython framework**, which provides direct access to LEGO EV3 motors and sensors with high performance. The structure is divided into the following parts:

- **Initialization**
  - Import required modules from Pybricks.
  - Configure motors, sensors, and parameters (speed, minimum distance threshold, proportional gain, etc.).

- **Main Loop**
  - Runs indefinitely until stopped.
  - Reads ultrasonic sensors.
  - Applies obstacle avoidance logic if needed.
  - If no obstacle is detected, applies proportional correction to return steering to the neutral position.

- **Failsafe**
  - If the program exits (for example, if the user stops the robot), all motors are stopped safely to prevent damage.

This design keeps the program **modular, easy to understand, and flexible for parameter adjustments**. All configurable parameters (`SPEED_A`, `SPEED_B`, `DIST_MIN`, `Kp`, `MAX_SPEED`) are declared at the top of the code, so they can be tuned without modifying the main logic.

---

## Design Challenges and Solutions

1. **Unstable Steering**  
   - Initial versions of the robot relied on fixed steering corrections, which caused the robot to drift permanently after avoiding obstacles.  
   - **Solution**: Added auto-centering with proportional control. Now, the robot always returns smoothly to its starting direction.

2. **Slow Recovery**  
   - The robot sometimes took too long to straighten after a turn, causing collisions later.  
   - **Solution**: Increased proportional gain (`Kp`) and maximum correction speed (`MAX_SPEED`) to allow faster but still smooth realignment.

3. **Sensor Noise**  
   - Ultrasonic sensors occasionally produced unstable readings.  
   - **Solution**: Added a small loop delay (`wait(50)`) and tolerance ranges for steering correction to reduce unnecessary jitter.

4. **Mechanical Alignment**  
   - The steering mechanism required precise calibration so that Motor B’s zero angle corresponded to straight wheels.  
   - **Solution**: Defined the neutral position (`POS_INICIAL_B`) at startup and ensured all corrections referenced this value.

---

## Key Features of the Solution

- **Continuous Forward Motion**: The robot always progresses, which is essential in WRO timed runs.  
- **Reliable Obstacle Avoidance**: Dual ultrasonic sensors provide redundancy and directional awareness.  
- **Self-Stabilizing Steering**: Automatic return to neutral prevents drift and guarantees path recovery.  
- **Parameter Tuning**: All speeds, distances, and correction factors are easily adjustable.  
- **Simplicity and Robustness**: Minimal moving parts and straightforward code reduce failure points.  

---

## Future Improvements

Although the current design is competition-ready, several enhancements are possible:

- **PID Control**: Extending proportional correction to a full PID controller could make steering even smoother.  
- **Sensor Fusion**: Combining ultrasonic sensors with a gyro sensor could help detect arena curves and improve stability.  
- **Dynamic Speed Control**: Slowing down near obstacles and speeding up in open areas would optimize performance.  
- **Modular Code**: Breaking the program into reusable modules would improve readability and allow faster testing.  

---



The design process was interactive, with multiple prototypes tested and improved. Each challenge taught us valuable lessons about robotics, programming, and teamwork. Ultimately, the final robot represents the principles of engineering that WRO promotes: **innovation, problem-solving, and collaboration**.

This repository contains the complete source code (`src`) used to control the robot. All logic described here is implemented in Python and can be directly executed on the LEGO EV3 brick with Pybricks MicroPython. However, it is strictly prohibited by us for **Panamanian** Robotics teams to use them for their personal privilege within other competitions, this can only be used as a reference or as an educational resource.

We believe this solution is not only effective for the competition but also a great foundation for further experiments in autonomous driving with LEGO robotics.
