# Schematics and Diagrams – LEGO EV3 Robot

## Directory Overview

This folder includes schematic diagrams for:

- **EV3 Brick (Control Unit)**  
  Logical port layout, power management, and I/O architecture.
  
- **Motors**  
  Placement diagrams and wiring configuration using EV3 output ports.
  
- **Sensors**  
  Input port mapping, cable routing, and pinout descriptions for ultrasonic and color sensors.

---

## Drivetrain Configuration

Our robot uses a **four-wheel LEGO chassis** designed for balance, traction, and modularity. The drivetrain setup includes:

### Mechanical Design

- **Two powered wheels** for propulsion.  
- **Two unpowered (idler) wheels** for support and balance.  
- All wheels are fixed in parallel alignment to allow efficient forward and backward movement.

### Motor Placement

- **Rear Motor**: Mounted centrally between the rear wheels and connected to EV3 output port A.  
- **Front Motor**: Mounted between the front wheels and connected to EV3 output port B.  
- This configuration allows precise control over movement and steering by adjusting the motor speeds independently.

### Traction Strategy

- The drivetrain follows a **free-wheel traction model**:
  - Powered wheels provide propulsion.  
  - Unpowered wheels add stability without introducing drag.  
  - This design simplifies the mechanical system while maintaining high maneuverability.

---

## EV3 Brick Integration

- Uses standard **EV3 input ports (1–4)** for sensors and **output ports (A–D)** for motors.  
- Each motor includes an internal rotary encoder for precise movement control.  
- Communication and power distribution follow LEGO’s RJ12 standard.  
- The EV3’s onboard processor manages sensor input, motor control, and decision-making logic.

---

## Electrical & Wiring Notes

| Component | Port | Description |
|------------|------|-------------|
| Rear Motor | A | Rear-mounted, connected via standard EV3 cable |
| Front Motor | B | Front-mounted, connected via standard EV3 cable |
| Right Ultrasonic Sensor | S2 | Side-facing object detection |
| Left Ultrasonic Sensor | S3 | Side-facing object detection |
| Front Ultrasonic Sensor | S1 | Front-facing object detection |
| Color Sensor | S4 | Detects lines, color markers, and assists with navigation |

---

## References

- LEGO Mindstorms EV3 Hardware Documentation  
- EV3 Schematic Community Resources (StackExchange, GitHub)
