# Piolín Tech - Project Overview

## 1. Introduction to Piolín 
**Piolín** is an autonomous robot developed by the Panamanian 🇵🇦 team **Piolín Tech** for the 2025 World Robot Olympiad (WRO). Our project participates in the **Future Engineers** category. The primary goal of Piolín Tech is to integrate advanced robotics principles, including sensor fusion, real-time data processing, and autonomous decision-making, to navigate and complete challenges efficiently, representing Panama in an international robotics arena.  

The robot is designed to **autonomously navigate a predefined circuit**, detect obstacles, and adapt its path in real time. Its architecture combines a **Raspberry Pi 5** for visual processing, an **EV3 Brick** for motor and sensor control, and an array of ultrasonic and color sensors to support navigation and obstacle management.  

## 2. Main Components

| Component | Function |
|-----------|---------|
| **DC Motors** | Rear-wheel drive (RWD) propulsion. |
| **Wheel Encoders** | Measures wheel rotations for distance and precise movement. |
| **Servo Motor** | Controls front-wheel steering. |
| **Nexigo Camera** | Visual detection, color recognition, obstacle identification (Raspberry Pi 5). |
| **Ultrasonic Sensors (3)** | Two sides + one front, for collision avoidance and wall alignment. |
| **MPU Gyroscope with PID Control** | Maintains stable orientation and straight trajectory. |
| **Color Sensor** | Detects track lines for turns or maneuvers. |

---

## 3. Sensor & System Diagram
       [Nexigo Camera]
             |
             v
      [Raspberry Pi 5]
             |
             v
+--------------+---------------+
| | |
[Front Ultrasonic] [Side Ultrasonics]
| | |
+-------+------+---------------+
|
[EV3 Brick]
|
+----+----+
| |
[DC Motors] [Servo Motor]
|
[Wheels]


> Flow: Camera -> Pi processes vision -> EV3 controls motors & servos -> Sensors feedback for PID & obstacle avoidance.

---

## 4. Main Operational Workflow
## 4. Main Operational Workflow

### 4.1 Initialization Phase
- **Power-Up, Self-Checks, Calibration:** Checks sensors, calibrates MPU gyroscope.  
- **Ready State:** LED signals readiness; operation starts with button press.

### 4.2 Autonomous Navigation Phase
- **Orientation Correction:** MPU-6050 + PID ensures straight path.  
- **Obstacle Detection:** Nexigo camera identifies obstacles.  
  - **Evasion Maneuver:** Robot turns until path is clear.  
  - **Trajectory Re-acquisition:** Side ultrasonics help recenter robot.

### 4.3 Completion Phase
- **End of Laps:** Robot transitions to finish phase.  
- **Parking Maneuver:** Executes parking maneuver to complete challenge.

