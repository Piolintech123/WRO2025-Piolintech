# Explanation of the Designed Solution

### Overview

 Piolín robot implements a **reactive obstacle avoidance system** for autonomous navigation in the Open Challenge. It relies primarily on:

- **Two motors (A and B):** Motor A for forward motion and Motor B for differential steering.  
- **Three ultrasonic sensors:** Front (S1) for frontal obstacle detection, left (S3) and right (S2) for wall and lateral obstacle detection.  

The design avoids complex control systems like PID loops or gyroscope-based stabilization; instead, it uses **proportional feedback on the steering motor (Motor B)** and simple distance thresholds for reactive navigation.

---

### Hardware Utilization

| Hardware | Role in Solution |
|----------|----------------|
| **Motor A (Port A)** | Provides the primary propulsion of the robot, moving it forward at a constant speed defined by `SPEED_A`. |
| **Motor B (Port B)** | Implements differential steering, allowing the robot to turn left or right in response to obstacle proximity. Its position is monitored for proportional correction to maintain straight-line movement. |
| **Front Ultrasonic (S1)** | Measures distance to obstacles directly in front. When an obstacle is too close (`DIST_MIN_FRONT`), triggers a reverse-and-turn maneuver. |
| **Left Ultrasonic (S3) & Right Ultrasonic (S2)** | Detect lateral obstacles or walls. If either sensor reads a distance below `DIST_MIN`, the robot adjusts its heading to avoid collision. |
| **Proportional Control** | Motor B uses a proportional control (`Kp`) to correct heading when no obstacles are detected, returning to its initial straight position (`POS_INICIAL_B`). |

---

### Operational Logic

#### Forward Motion
- Motor A continuously drives the robot forward at a constant speed (`SPEED_A`).  
- Motor B remains at the initial angle (`POS_INICIAL_B`) unless obstacle avoidance is required.  

#### Frontal Obstacle Avoidance
1. The front ultrasonic sensor continuously measures the distance ahead.  
2. If `front_distance < DIST_MIN_FRONT`:  
   - **Motor A stops** to prevent collision.  
   - The robot **reverses** while **Motor B rotates left** (`SPEED_B`) to navigate around the obstacle.  
   - The loop continues until the obstacle is no longer within the minimum distance threshold.  
3. After the reverse-and-turn:  
   - Motor B returns to its initial straight position using proportional correction (`Kp`).  
   - Motor A resumes forward motion.

**Technical Note:** This ensures the robot avoids frontal collisions while automatically reorienting for straight-line navigation.

#### Lateral Obstacle Avoidance
- **Left Wall Detection:** If `left_distance < DIST_MIN`, Motor B turns right (`SPEED_B`) to move away from the wall.  
- **Right Wall Detection:** If `right_distance < DIST_MIN`, Motor B turns left (`-SPEED_B`) to avoid the wall.  
- If no lateral obstacles are detected:  
  - Motor B returns to its straight position (`POS_INICIAL_B`) using **proportional feedback**, limited by `MAX_SPEED` to prevent abrupt movements.  

**Key Feature:** This reactive approach allows the robot to continuously correct its heading based on sensor input, ensuring smooth navigation without overshoot.

#### Proportional Steering Correction
- The robot continuously computes the **error** as:  
    `error = POS_INICIAL_B - MOTOR_B.angle()`
- The correction speed is proportional to this error:  
    `speed_correction = int(Kp * error)`

- Correction is constrained by `MAX_SPEED` to avoid overly aggressive steering.  
- If the error is below a tolerance (`TOLERANCIA`), Motor B stops, maintaining a straight trajectory.

**Impact:** This proportional feedback acts as a lightweight stabilization system without requiring a gyroscope or full PID control.

---

### Loop Timing and Stability
- The main loop executes with a small delay of 50 ms (`wait(50)`) to prevent sensor flooding and allow motor commands to be applied smoothly.  
- The `try/finally` block ensures that motors are safely stopped if the program ends or an exception occurs, preventing runaway motion.

---

### Summary of Technical Design Principles

1. **Reactive Navigation:** Uses simple distance thresholds to make decisions, allowing quick adaptation to dynamic environments.  
2. **Differential Steering with Feedback:** Motor B corrects the robot's heading based on proportional feedback, enabling straight-line travel and smooth course correction.  
3. **Safety Prioritization:** Frontal obstacles trigger immediate stop and reverse maneuvers to prevent collisions.  
4. **Modularity:** Sensor readings and motor controls are cleanly separated, making the system easy to maintain or expand.  
5. **Computational Efficiency:** The algorithm is lightweight and runs entirely on the EV3 Brick without requiring high-level computation from a secondary processor (used only for camera tasks in other rounds).
