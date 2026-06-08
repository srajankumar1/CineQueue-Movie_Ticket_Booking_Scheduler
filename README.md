# 🎬 CineQueue – Movie Ticket Booking Scheduler

<div align="center">

HTML
CSS
JavaScript
OS Project
GitHub Pages

### 🎟️ A Professional Movie Ticket Booking Simulation Using CPU Scheduling Algorithms

Visualize and compare how different CPU scheduling algorithms can be applied to a real-world movie ticket booking system.

### 🔗 Live Demo

https://srajankumar1.github.io/CineQueue-Movie_Ticket_Booking_Scheduler/

</div>

---

## 📌 Project Overview

CineQueue is a web-based simulation platform that demonstrates how classical CPU Scheduling Algorithms can be applied to an Online Movie Ticket Booking System.

In this project:

- Each booking request is treated as a process.
- Arrival Time (AT) represents when a user submits a booking request.
- Burst Time (BT) represents the time required to process the booking.
- Priority represents customer membership level (VIP, Premium, Regular, Economy).
- The booking server acts as the CPU.

The simulator provides an interactive interface where users can add booking requests, select scheduling algorithms, visualize execution timelines, and analyze performance metrics.

---

## 🎯 Problem Statement

Online movie ticket booking platforms receive multiple booking requests simultaneously. Efficient scheduling of these requests is essential to reduce waiting time, improve customer satisfaction, and ensure fair resource allocation.

The objective of this project is to simulate and compare various CPU scheduling algorithms to determine how booking requests can be processed efficiently under different scenarios.

---

## 🧠 Scheduling Algorithms Implemented

### 1️⃣ First Come First Served (FCFS)

- Non-Preemptive Scheduling
- Requests are processed in order of arrival.
- Simple and fair execution strategy.

Example:

text Alice → Bob → Carol → User4 

---

### 2️⃣ Shortest Job First (SJF)

- Non-Preemptive Scheduling
- Process with the shortest burst time executes first.
- Reduces average waiting time.

Example:

text User4 → Bob → Alice → Carol 

---

### 3️⃣ Shortest Remaining Time First (SRTF)

- Preemptive Scheduling
- A newly arrived process with shorter remaining time interrupts the currently running process.

Example:

text Alice  ↓ Bob Arrives  ↓ Bob Executes  ↓ Alice Resumes 

---

### 4️⃣ Priority Scheduling (Preemptive)

- VIP customers receive immediate preference.
- Higher priority users can interrupt lower priority users.
- Realistic simulation of premium booking services.

#### Priority Levels

| Priority | Category |
|-----------|-----------|
| 1 | VIP |
| 2 | Premium |
| 3 | Regular |
| 4 | Economy |

---

## 🎥 Real-Life Mapping

| Movie Ticket Booking System | CPU Scheduling Concept |
|----------------------------|-----------------------|
| Booking Request | Process |
| Booking Server | CPU |
| User Arrival | Arrival Time |
| Booking Duration | Burst Time |
| VIP Membership | Priority |
| Booking Execution | CPU Execution |

---

## ✨ Features

### 🎟️ Booking Queue Management

- Add Booking Requests
- Delete Booking Requests
- Modify Arrival Time
- Modify Burst Time
- Modify Priority Levels

### 🎬 Scheduling Simulation

- FCFS Simulation
- SJF Simulation
- SRTF Simulation
- Priority Scheduling Simulation

### 📊 Performance Metrics

- Completion Time (CT)
- Turnaround Time (TAT)
- Waiting Time (WT)
- Response Time (RT)

### 📈 Analytics Dashboard

- Average Waiting Time
- Average Turnaround Time
- Average Response Time
- Total Execution Time
- Number of Users Served

### 🎨 User Interface

- Movie-Themed Design
- Professional Dashboard Layout
- Responsive Design
- Interactive Controls
- Dynamic Visualization

---

## 📊 Performance Metrics Formulas

### Completion Time

text CT = Time when process completes execution 

### Turnaround Time

text TAT = CT − AT 

### Waiting Time

text WT = TAT − BT 

### Response Time

text RT = First Execution Time − Arrival Time 

---


## 🖥️ Technologies Used

| Technology | Purpose |
|------------|----------|
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Scheduling Logic |
| GitHub Pages | Deployment |

---


## 📸 Project Highlights

✅ Interactive Scheduling Simulator

✅ Dynamic Booking Queue

✅ Real-Time Execution Visualization

✅ Performance Metrics Dashboard

✅ Responsive UI Design

✅ GitHub Pages Deployment

✅ Educational Operating Systems Project

---

## 🎓 Academic Relevance

This project demonstrates practical applications of:

- CPU Scheduling Algorithms
- Operating Systems Concepts
- Process Management
- Resource Allocation
- Performance Evaluation
- Algorithm Comparison

It provides a real-world understanding of scheduling techniques through an online movie ticket booking scenario.

---

## 🌍 Sustainable Development Goals (SDGs)

### SDG 9 – Industry, Innovation and Infrastructure

Efficient scheduling improves digital infrastructure and service performance.

### SDG 11 – Sustainable Cities and Communities

Optimized booking systems enhance accessibility and user experience.

### SDG 12 – Responsible Consumption and Production

Efficient resource utilization minimizes computational overhead.

---



## ⭐ Future Enhancements

- Round Robin Scheduling
- Multilevel Queue Scheduling
- Multilevel Feedback Queue Scheduling
- Export Results to PDF
- Advanced Analytics Dashboard
- Dark / Light Theme Support
- Real-Time Simulation Animation

---

<div align="center">

### 🎬 CineQueue – Bringing Operating Systems Concepts to Life

If you found this project useful, consider giving it a ⭐
