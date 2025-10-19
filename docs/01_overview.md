![093d809c-2b79-41a6-b265-3d8f717025d3](https://github.com/user-attachments/assets/9c9b904c-fd6e-4afe-8a02-837a716e416e)
# Piolín Tech - Project Overview

## 1. Introduction to Piolín  
**Piolín** is an autonomous robot developed by the Panamanian 🇵🇦 team **Piolín Tech** for the 2025 World Robot Olympiad (WRO), in the **Future Engineers** category. The main objective is to design a robot that **navigates a predefined circuit autonomously**, detects obstacles, and adapts its path in real time using EV3 sensors and motors, demonstrating principles of sensor fusion, real-time decision-making, and autonomous navigation.  

---

## 2. Main Components

| Component                  | EV3 Port / Interface | Function                                       |
|----------------------------|-------------------|-----------------------------------------------|
| **Rear Motor**             | A                 | Rear-mounted, drives rear wheels.             |
| **Front Motor**            | B                 | Front-mounted, controls front wheels/steering.|
| **Front Ultrasonic Sensor**| S1                | Front-facing object detection.                |
| **Right Ultrasonic Sensor**| S2                | Side-facing object detection.                 |
| **Left Ultrasonic Sensor** | S3                | Side-facing object detection.                 |
| **Color Sensor**           | S4                | Detects colors for the 3rd and 4th Round.  |

> Each component includes documentation on calibration, common errors, and integration with the robot.  

---

## 3. Sensor & System Diagram (EV3-Only)
```
  [Front Ultrasonic S1] 
           |
           v
   [EV3 Brick Central]
      /         \
[Left Ultrasonic S3] [Right Ultrasonic S2]
           |
           v
[Front Motor B] [Rear Motor A]
       |               |
       v               v 
     Wheels         Wheels       

```
> Flow: EV3 reads sensor data → processes navigation logic → controls motors → sensors provide feedback for obstacle avoidance and track following.  

---
## 4. Open Challenge Operational Workflow

### 4.1 Initialization Phase
#### 4.1.1 Power-Up and Self-Checks
- EV3 verifies:
  - Rear Motor (A) and Front Motor (B) functionality.
  - Ultrasonic sensors: Front (S1), Right (S2), Left (S3).
  - Color sensor functionality (if used for obstacle awareness).

#### 4.1.2 Ready State
- LED indicator signals the robot is ready.
- Operation begins when the start button is pressed.

### 4.2 Autonomous Navigation Phase
#### 4.2.1 Forward Movement
- Robot moves forward along the track autonomously.
- Side ultrasonic sensors (S2 and S3) maintain safe distances from walls or track boundaries.

#### 4.2.2 Obstacle / Wall Detection
- Front ultrasonic sensor (S1) monitors for obstacles directly ahead.
- Pre-programmed maneuvers (Ext if red, Int if green) adjust the trajectory to avoid collisions using sensor readings.

### 4.3 Completion Phase
#### 4.3.1 Lap Counting
- The robot keeps track of completed laps internally (programmed logic).

#### 4.3.2 Stopping
- After completing 3 laps, the robot stops automatically, signaling the completion of the Open Challenge.

[Go back](../README.md)
