# Programación - Sheepthieves Robot

Este documento describe la programación y el software del robot Sheepthieves.

## Estructura del Proyecto

```
Sheepthieves-/
├── src/
│   ├── main.ino          # Programa principal de Arduino
│   └── robot_control.py  # Script de control en Python
├── docs/
│   └── PROGRAMMING.md    # Documentación de programación
└── examples/
    └── test_sensors.ino  # Ejemplos de código
```

## Hardware Requerido

- Arduino UNO o compatible
- Driver de motores L298N o similar
- 2 motores DC
- 3 sensores infrarrojos (para seguimiento de línea)
- Fuente de alimentación

## Configuración de Pines

### Motores
- Motor Izquierdo Adelante: Pin 5
- Motor Izquierdo Atrás: Pin 6
- Motor Derecho Adelante: Pin 9
- Motor Derecho Atrás: Pin 10

### Sensores
- Sensor Izquierdo: A0
- Sensor Central: A1
- Sensor Derecho: A2

## Programación Arduino

El programa principal (`src/main.ino`) implementa un algoritmo básico de seguimiento de línea:

1. Lee los valores de los sensores infrarrojos
2. Determina la posición de la línea
3. Ajusta los motores para seguir la línea

### Compilar y Subir

```bash
# Usando Arduino IDE:
# 1. Abrir src/main.ino
# 2. Seleccionar placa Arduino UNO
# 3. Seleccionar puerto COM
# 4. Hacer clic en "Subir"

# Usando arduino-cli:
arduino-cli compile --fqbn arduino:avr:uno src/main.ino
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno src/main.ino
```

## Control con Python

El script `robot_control.py` permite monitorear y controlar el robot desde una computadora.

### Instalación de Dependencias

```bash
pip install pyserial
```

### Uso

```bash
python src/robot_control.py
```

## Personalización

### Ajustar Velocidad

Modificar las constantes en `main.ino`:
```cpp
const int NORMAL_SPEED = 150;  // Velocidad normal (0-255)
const int TURN_SPEED = 100;    // Velocidad de giro (0-255)
```

### Calibración de Sensores

El umbral de detección de línea está configurado en 500. Ajustar según los sensores:
```cpp
if (centerSensor > 500) {  // Cambiar este valor
    moveForward();
}
```

## Solución de Problemas

### El robot no se mueve
- Verificar conexiones de los motores
- Verificar alimentación
- Comprobar pines en el código

### Los sensores no detectan la línea
- Calibrar el umbral de sensores
- Verificar altura de los sensores sobre la superficie
- Asegurar buena iluminación

### Error de comunicación serial
- Verificar que el puerto sea correcto
- Asegurar que no haya otros programas usando el puerto
- Verificar baudrate (9600)

## Recursos Adicionales

- [Arduino Reference](https://www.arduino.cc/reference/)
- [Tutoriales de Arduino](https://www.arduino.cc/en/Tutorial/HomePage)
- Documentación de PySerial
