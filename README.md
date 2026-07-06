# Smart Traffic Junction Simulation – SUMO Queue Model

## Overview

This project presents a smart traffic junction simulation developed using Python and Pygame. Inspired by queue-based traffic management techniques used in SUMO (Simulation of Urban MObility), the system models a four-way road intersection with intelligent traffic signal control, vehicle queue management, emergency vehicle prioritization, and dynamic traffic flow visualization.

Vehicles of different categories including cars, buses, trucks, ambulances, and fire engines are generated randomly and assigned to different lanes. Traffic signals operate on timed cycles while emergency vehicles receive priority through signal preemption. The simulation demonstrates fundamental concepts of intelligent transportation systems (ITS), traffic engineering, and autonomous traffic management.

---

# Features

* Four-way smart traffic junction simulation
* SUMO-inspired queue-based traffic management
* Dynamic traffic signal control
* Multi-lane vehicle movement
* Intelligent queue handling
* Safe inter-vehicle spacing
* Emergency vehicle priority
* Traffic signal countdown timers
* Vehicle waiting time monitoring
* Random traffic generation
* Multiple vehicle categories
* Real-time graphical visualization

---

# Technologies Used

* Python 3
* Pygame

---

# Project Structure

```text
Smart-Traffic-Junction/
│
├── smart_traffic_junction.py
├── README.md
└── requirements.txt
```

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Kaushal1525/Smart-Traffic-Junction.git
```

## Navigate to the project directory

```bash
cd Smart-Traffic-Junction
```

## Install the required dependency

```bash
pip install -r requirements.txt
```

or

```bash
pip install pygame
```

---

# Running the Project

Execute the simulation:

```bash
python smart_traffic_junction.py
```

The application opens a graphical traffic junction where vehicles are continuously generated and managed by the intelligent traffic signal controller.

Close the application window to terminate the simulation.

---

# Working Principle

The simulation performs the following operations:

1. Initialize a four-way road intersection.
2. Randomly generate vehicles in different lanes.
3. Assign vehicle categories.
4. Control traffic lights using timed signal cycles.
5. Maintain safe spacing between vehicles.
6. Monitor vehicle queues and waiting times.
7. Detect emergency vehicles.
8. Temporarily prioritize emergency traffic.
9. Resume normal signal operation after emergency clearance.

---

# System Architecture

```text
Vehicle Generator
        │
        ▼
Lane Assignment
        │
        ▼
Traffic Queue Manager
        │
        ▼
Traffic Signal Controller
        │
        ▼
Vehicle Movement Engine
        │
        ├────────► Safe Gap Controller
        │
        ├────────► Queue Monitoring
        │
        └────────► Emergency Vehicle Detection
                    │
                    ▼
             Signal Preemption
```

---

# Vehicle Categories

The simulation supports multiple vehicle types:

| Vehicle     | Purpose                    |
| ----------- | -------------------------- |
| Car         | Passenger vehicle          |
| Bus         | Public transportation      |
| Truck       | Heavy transport            |
| Ambulance   | Emergency medical response |
| Fire Engine | Fire and rescue operations |

Each vehicle type is represented using different colors and dimensions.

---

# Traffic Signal Operation

The intersection contains four independent traffic directions:

* North
* East
* South
* West

Traffic signals operate in a cyclic sequence with configurable green signal durations.

The simulation displays:

* Active signal
* Remaining green time
* Waiting time for each direction

---

# Emergency Vehicle Priority

The system includes emergency vehicle detection logic.

When an emergency vehicle is detected:

* The corresponding direction immediately receives a green signal.
* Other directions are temporarily halted.
* Once the emergency vehicle clears the junction, normal traffic operation resumes.

This demonstrates the concept of traffic signal preemption commonly used in intelligent transportation systems.

---

# Queue Management

Vehicles maintain a minimum safe distance from one another while waiting at traffic signals.

Queue management includes:

* Lane-wise vehicle organization
* Collision-free spacing
* Stop-line enforcement
* Smooth acceleration after signal change

---

# Applications

* Intelligent Transportation Systems (ITS)
* Smart Traffic Signal Control
* Autonomous Vehicle Research
* Traffic Engineering
* Urban Mobility Simulation
* Smart City Research
* Transportation Planning
* Queue Optimization Studies
* Emergency Traffic Management
* Educational Traffic Simulators

---

# Future Enhancements

* Adaptive AI-based traffic signal control
* Reinforcement learning optimization
* Vehicle-to-Infrastructure (V2I) communication
* Multi-junction coordination
* Traffic density prediction
* Real-time sensor integration
* Pedestrian crossings
* Weather-aware traffic control
* Connected autonomous vehicles
* SUMO simulator integration
* ROS 2 compatibility
* 3D traffic visualization

---

# Requirements

* Python 3.8 or later

---

# Dependencies

* pygame

---

# Author

**Kaushal Reddy**

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
