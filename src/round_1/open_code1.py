#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import _thread
import time
import socket

EV3 = EV3Brick()

MOTOR_A = Motor(Port.A)  # Motor para ir recto
MOTOR_B = Motor(Port.B)  # Motor diferencial para girar

# Guardar posición inicial de MOTOR_B
POS_INICIAL_B = MOTOR_B.angle()

US_LEFT = UltrasonicSensor(Port.S3)   # Izquierda
US_RIGHT = UltrasonicSensor(Port.S2)  # Derecha
US_FRONT = UltrasonicSensor(Port.S1)  # Frontal


SPEED_A = -1000         # Velocidad de avance del motor principal
SPEED_B = 150          # Velocidad del motor para girar
DIST_MIN = 350         # Distancia mínima en mm para evitar choque lateral
DIST_MIN_FRONT = 350   # Distancia mínima en mm para evitar choque frontal
Kp = 20                # Ganancia para control proporcional de MOTOR_B
MAX_SPEED = 900        # Velocidad máxima de corrección de MOTOR_B
TOLERANCIA = 3         # Tolerancia para detener corrección de MOTOR_B 
  # Para que Mia y Christian sepan que cambiar cuando no estoy

def main():
    MOTOR_A.run(SPEED_A)

    try:
        while True:
            front_distance = US_FRONT.distance()
            left_distance = US_RIGHT.distance()
            right_distance = US_LEFT.distance()

            # --- DETECCIÓN FRONTAL ---
            if front_distance < DIST_MIN_FRONT:
                # Detener avance
                MOTOR_A.stop(Stop.BRAKE)

                # Retroceder girando a la izquierda mientras haya pared al frente
                while US_FRONT.distance() < DIST_MIN_FRONT:
                    MOTOR_A.run(-SPEED_A)   # retroceso
                    MOTOR_B.run(SPEED_B)    # giro a la izquierda
                    wait(50)

                # Detener después del retroceso
                MOTOR_A.stop(Stop.BRAKE)
                MOTOR_B.stop(Stop.BRAKE)

                # Volver recto antes de continuar
                error = POS_INICIAL_B - MOTOR_B.angle()
                while abs(error) > TOLERANCIA:
                    speed_correction = int(Kp * error)
                    MOTOR_B.run(speed_correction)
                    error = POS_INICIAL_B - MOTOR_B.angle()
                    wait(10)
                MOTOR_B.stop(Stop.BRAKE)

                # Reanudar avance normal
                MOTOR_A.run(SPEED_A)

            # --- EVITAR PAREDES LATERALES ---
            elif left_distance < DIST_MIN:
                MOTOR_B.run(SPEED_B)  # Gira a la derecha
            elif right_distance < DIST_MIN:
                MOTOR_B.run(-SPEED_B)  # Gira a la izquierda
            else:
                # Regresar a posición inicial con control proporcional
                error = POS_INICIAL_B - MOTOR_B.angle()
                speed_correction = int(Kp * error)

                # Limitar velocidad máxima
                if speed_correction > MAX_SPEED:
                    speed_correction = MAX_SPEED
                elif speed_correction < -MAX_SPEED:
                    speed_correction = -MAX_SPEED

                if abs(error) < TOLERANCIA:
                    MOTOR_B.stop(Stop.BRAKE)
                else:
                    MOTOR_B.run(speed_correction)

            wait(50)  # Pequeña pausa para el loop
    finally:
        MOTOR_A.stop(Stop.BRAKE)
        MOTOR_B.stop(Stop.BRAKE)

if __name__ == '__main__':
    main()
