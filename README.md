# Saarthi

**Smart AI-Assisted Route & Transit Help for Independence**

Saarthi is a student engineering project exploring an affordable, detachable assistive module for a conventional white mobility cane. It aims to complement established mobility techniques with supplementary environmental information and smartphone-based assistance.

The white cane remains the user's primary mobility aid.

## Problem Statement

People with visual impairments may benefit from additional information about nearby obstacles, printed text, and their surroundings. Saarthi explores how accessible, low-cost electronics and camera-based software could provide supplementary audio and tactile feedback.

## Proposed System

The planned system combines hardware-based proximity alerts with smartphone-based assistance.

- **ESP32 development board:** Planned for sensor processing and Bluetooth Low Energy (BLE) communication.
- **Distance sensor:** Intended to detect nearby obstacles within its effective sensing range.
- **Vibration motor and driver:** Planned to communicate selected alerts through tactile feedback.
- **Smartphone:** Intended to support camera-based text recognition, text-to-speech, and future scene-understanding features.
- **Detachable mount:** Designed to attach the module to a conventional white cane without replacing its primary function.

Hardware components and the final system architecture remain subject to testing and budget constraints.

## Current Prototype

The software prototype is under active development.

- **Camera-based text recognition (OCR):** Implemented and tested with text presented to the camera.
- **Spoken text output:** Implemented and tested using text-to-speech.
- **Directional-symbol recognition:** Under development, with initial testing of directional symbols.
- **Hardware integration:** Planned; the sensing and vibration system has not yet been validated as an integrated prototype.
- **Smartphone companion application:** A future development goal.

These features have different levels of maturity. Initial demonstrations do not establish reliable performance in all lighting conditions, environments, or real-world mobility situations.

## Planned Development Roadmap

1. Improve text recognition and directional-symbol interpretation.
2. Test recognition accuracy under different lighting, distances, and viewing angles.
3. Finalize the hardware architecture and select components within the available budget.
4. Develop and test distance-sensor readings.
5. Implement vibration alerts using an appropriate motor driver.
6. Explore BLE communication between the microcontroller and a smartphone.
7. Develop a companion interface for accessible settings and future journey assistance.
8. Integrate the system and conduct controlled safety and usability tests.

## Technology Stack

**Current software exploration**
- Python
- Camera-based image processing and OCR
- Text-to-speech

**Planned technologies**
- C/C++ for microcontroller firmware
- ESP32 and distance-sensing hardware
- Bluetooth Low Energy
- Android companion application

Technologies listed as planned have not necessarily been integrated or validated.

## Safety and Accessibility

Saarthi is intended to supplement, not replace, a white cane, orientation and mobility training, or established mobility aids.

Sensor blind spots, OCR errors, incorrect directional interpretations, latency, battery failure, and hardware faults are important risks. The system must be tested under controlled conditions, and its limitations must be communicated clearly before any real-world use.

## Project Documentation

This repository will contain source code, technical documentation, development notes, test procedures, and evidence of actual prototype progress.

- `docs/APP_PLAN.md` — companion application planning.

Additional documentation will be added as development progresses.

## Team and Project

**Student engineering project — Vishwakarma Awards 2026–27**

## Disclaimer

Saarthi is an experimental assistive-technology project. Features, specifications, and implementation plans may change as development and testing continue. No claim of reliable independent navigation or real-world safety is made at this stage.