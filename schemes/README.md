Schematics and Diagrams – LEGO EV3 Robot
---

## Directory Overview

This folder includes schematic diagrams for:

- **EV3 Brick (Control Unit)**  
  Logical port layout, power management, and I/O architecture.
  
- **Motors**  
  Placement diagrams and wiring configuration using EV3 output ports.
  
- **Sensors**  
  Input port mapping, cable routing, and pinout descriptions for touch, ultrasonic, gyro, and other sensors.
  
- **Camera Module (Optional)**  
  If a camera is used (It is, indeed! we are using a PixyCam), its position and connection are documented here.

---

## Drivetrain Configuration

Our robot uses a **four-wheel chassis using lego** designed for balance, traction, and modularity. The drivetrain setup includes:

### Mechanical Design

- **Two powered wheels** for propulsion.
- **Two unpowered (idler) wheels** for support and balance.
- All wheels are fixed in parallel alignment to allow efficient forward/backward movement.

### Motor Placement

- **Rear Motor**: Mounted centrally between the rear wheels. Connected to EV3 output port A.
- **Front Motor**: Mounted between the front wheels. Connected to EV3 output port B.
- This allows differential drive, where turning is achieved by varying the speed and direction of each motor independently.

### Traction Strategy

- The drivetrain follows a **free-wheel traction model**:
  - Powered wheels provide propulsion.
  - Unpowered front wheels add stability without introducing drag.
  - Simplifies mechanical design while retaining maneuverability.

---

## EV3 Brick Integration

- Uses standard **EV3 input ports (1–4)** for sensors and **output ports (A–D)** for motors.
- Each motor includes an internal rotary encoder, which connects through built-in tacho feedback lines.
- Communication and power distribution follow LEGO’s RJ12 standard.
- The EV3’s onboard ARM9 processor runs a Linux-based OS to handle I/O, motor control, and sensor polling.

---

## Electrical & Wiring Notes

| Component | Port | Description |
|----------|------|-------------|
| Rear Motor  | A | Rear-mounted, connected via standard EV3 cable |
| Front Motor | B | Front-mounted, connected via standard EV3 cable |
| Right Ultrasonic Sensor | S2 | Side-facing object detection |
| Left Ultrasonic Sensor | S3 | Side-facing object detection |
| Front Ultrasonic Sensor | S1 | Front-facing object detection |
|  Camera | 0 | interfaced via a second brain, a raspberry pi |
|  Color Sensor | S4 | Used to detect lines on the floor to rotate to the right side |


---


## References

- LEGO Mindstorms EV3 Hardware Documentation  
- EV3 Schematic Community Resources (StackExchange, GitHub)  


