![093d809c-2b79-41a6-b265-3d8f717025d3](https://github.com/user-attachments/assets/9c9b904c-fd6e-4afe-8a02-837a716e416e)
# Piolín Tech - Project Overview

## 1. Introduction to Piolín 
**Piolín** is an autonomous robot developed by the Panamanian 🇵🇦 team **Piolín Tech** for the 2025 World Robot Olympiad (WRO). Our project participates in the **Future Engineers** category. The primary goal of Piolín Tech is to integrate advanced robotics principles, including sensor fusion, real-time data processing, and autonomous decision-making, to navigate and complete challenges efficiently, representing Panama in an international robotics arena.  

The robot is designed to **autonomously navigate a predefined circuit**, detect obstacles, and adapt its path in real time. Its architecture combines a **Raspberry Pi 5** for visual processing, an **EV3 Brick** for motor and sensor control, and an array of ultrasonic and color sensors to support navigation and obstacle management.  

## 2. Main Components
| Component | EV3 Port / Interface | Function |
|-----------|-------------------|---------|
| **Rear Motor** | A | Rear-mounted, drives rear wheels. |
| **Front Motor** | B | Front-mounted, controls front wheels/steering. |
| **Front Ultrasonic Sensor** | S1 | Front-facing object detection. |
| **Right Ultrasonic Sensor** | S2 | Side-facing object detection. |
| **Left Ultrasonic Sensor** | S3 | Side-facing object detection. |
| **Camera (Nexigo)** | 0 (via Raspberry Pi 5) | Visual detection, color recognition, and obstacle identification. |
| **Color Sensor** | (EV3 Port, if used) | Detects track lines for turns or maneuvers. |

> Each component has detailed documentation covering calibration, common errors, and integration with the robot.  

---

## 3. Sensor & System Diagram
       [Nexigo Camera]
             |
             v
      [Raspberry Pi 5]
             |
             |
             v
       [LUS] [SUS]
             |
        EV3 Brick
             |
        Front Motor
             |
          Wheels


> Flow: Camera -> Pi processes vision -> EV3 controls motors -> Sensors feedback for obstacle avoidance.

---

## 4. Main Operational Workflow

### 4.1 Initialization Phase
- **Ready State:** LED signals readiness; operation starts with button press.

### 4.2 Autonomous Navigation Phase
- **Obstacle Detection:** Nexigo camera identifies obstacles.  
  - **Evasion Maneuver:** Robot turns until path is clear.  
  - **Trajectory Re-acquisition:** Side ultrasonics help recenter robot.

### 4.3 Completion Phase
- **End of Laps:** Robot transitions to finish phase.  
- **Parking Maneuver:** Executes parking maneuver to complete challenge.

