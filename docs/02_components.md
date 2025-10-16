# Hardware Components Overview

## Introduction
Our robot's hardware architecture combines precision actuation, high-quality sensing, and advanced computation to navigate a predefined track, detect obstacles, and execute complex maneuvers. This section provides a detailed overview of all hardware components, including the Raspberry Pi 5, Nexigo camera, LEGO EV3 Brick, motors, ultrasonic sensors, and the color sensor. Each component is described in terms of quantity, voltage requirements, functionality, and key features, ensuring a complete understanding of the robot’s physical architecture.

---

## Raspberry Pi 5
- **Quantity:** 1  
- **Voltage:** 5V (operating), 5–20V via USB-C PD  
- **Description:** The Raspberry Pi 5 serves as a secondary processing unit responsible for high-level computation, particularly image processing from the Nexigo camera. It interprets visual information, such as track colors and obstacles, and communicates navigation commands to the LEGO EV3 Brick for actuation.  
- **Features:** Quad-core ARM Cortex-A76 CPU, 8GB LPDDR5 RAM, USB 3.0 ports, Gigabit Ethernet, Wi-Fi 6, Bluetooth 5.0, multiple camera interfaces via USB or CSI, support for Python and OpenCV libraries.

---

## Nexigo Camera
- **Quantity:** 1  
- **Voltage:** 5V (via USB from Raspberry Pi 5)  
- **Description:** The Nexigo camera captures real-time video, enabling the robot to detect colors and identify obstacles. It connects directly to the Raspberry Pi 5 for processing and provides the visual data necessary for autonomous decision-making.  
- **Features:** Full HD 1080p resolution, wide field of view, USB 2.0/3.0 interface, compatibility with OpenCV and other vision processing libraries, high frame rate support for smooth image capture.

---

## LEGO EV3 Brick
- **Quantity:** 1  
- **Voltage:** 10V 
- **Description:** The EV3 Brick functions as the primary actuator controller of the robot. It executes commands from onboard programs or the Raspberry Pi, controls motors, reads sensor inputs, and coordinates all low-level robot actions.  
- **Features:** ARM9 processor, 64KB RAM, 16MB flash memory, 6 sensor input ports, 4 motor output ports, Bluetooth and USB connectivity, supports programming in MicroPython, EV3-G, and other languages.

---

## DC Motors
### Rear Motor (A)
- **Quantity:** 1  
- **Voltage:** 7.2V nominal (powered by EV3)  
- **Description:** Drives the rear wheels, providing the main propulsion for the robot. Controlled by the EV3 Brick, it allows precise speed and direction adjustments.  
- **Features:** Built-in rotation sensors (encoders) for distance measurement, supports controlled acceleration and braking.

### Front Motor (B)
- **Quantity:** 1  
- **Voltage:** 7.2V nominal (powered by EV3)  
- **Description:** Controls front-wheel steering, enabling accurate turning maneuvers and path adjustments.  
- **Features:** Encoder feedback for precise angular positioning, reversible rotation for left/right turns.

---

## Ultrasonic Sensors
### Front Ultrasonic Sensor (S1)
- **Quantity:** 1  
- **Voltage:** 4.5–7V (EV3 powered)  
- **Description:** Detects obstacles or walls directly ahead of the robot. Provides distance measurements to prevent collisions and enable safe navigation.  
- **Features:** Range 0–250 cm, high sampling rate, adjustable detection thresholds, supports both continuous and triggered measurement modes.

### Right Ultrasonic Sensor (S2) & Left Ultrasonic Sensor (S3)
- **Quantity:** 2  
- **Voltage:** 4.5–7V (EV3 powered)  
- **Description:** Mounted on the sides, these sensors help maintain alignment with walls or track boundaries and assist in path correction during turns or evasive maneuvers.  
- **Features:** Same as front ultrasonic, supports simultaneous readings for improved side-to-side positioning.

---

## Color Sensor
- **Quantity:** 1  
- **Voltage:** 4.5–7V (EV3 powered)  
- **Description:** Detects colored lines or markers on the track to trigger turns or other programmed actions. Essential for lap counting and following designated paths.  
- **Features:** Measures reflected light intensity, detects specific colors, supports ambient light calibration, compatible with EV3 programming functions.

---

## Conclusion
The Piolín Tech robot integrates multiple hardware components in a unified system, allowing autonomous navigation, obstacle avoidance, and accurate path following. The combination of **high-performance computation (Raspberry Pi 5)**, **visual sensing (Nexigo Camera)**, and **robust actuation and sensing (EV3 Brick, motors, and sensors)** ensures reliability and precision in the Open and Obstacle Challenges of the WRO. Each component contributes to the overall efficiency, safety, and adaptability of the robot, forming a versatile platform capable of tackling complex tasks in competitive robotics environments.
