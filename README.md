# Sheepthieves-
Robotica

## Descripción

Proyecto de robótica "Sheepthieves" - Robot seguidor de línea con control automatizado.

## Estructura del Proyecto

- **src/** - Código fuente principal
  - `main.ino` - Programa Arduino principal
  - `robot_control.py` - Script de control Python
- **docs/** - Documentación
  - `PROGRAMMING.md` - Guía de programación completa
- **examples/** - Ejemplos de código
  - `test_sensors.ino` - Programa de prueba de sensores

## Inicio Rápido

### Arduino

1. Abrir `src/main.ino` en Arduino IDE
2. Conectar Arduino a la computadora
3. Seleccionar placa y puerto
4. Subir el programa

### Python

```bash
pip install pyserial
python src/robot_control.py
```

## Documentación

Para información detallada sobre programación, consultar [docs/PROGRAMMING.md](docs/PROGRAMMING.md)

## Hardware

- Arduino UNO
- Driver de motores L298N
- 2 motores DC
- 3 sensores infrarrojos
- Fuente de alimentación

## Licencia

MIT
