# 📸🔥Thermal Camera Diagnosis App Prototype


This repository contains all the source code, scripts, and notebooks used in my bachelor thesis project, "Enhancing Battery Recycling with Thermal Imaging Anomaly Detection." The project explores the integration of thermal imaging and anomaly detection methods to optimize battery discharging processes in recycling facilities.

## Repository Structure 📂

The repository is organized into the following directories:

### 1. **application** 🖥️
- **Description**: Contains all the implementation scripts and deployment files for the Thermal Camera Diagnosis App.
- **Highlights**:
  - `build-arm64.sh`: Script for building and deploying the application on ARM64 architecture platforms.
  - Integration with Bosch Rexroth's CtrlX CORE system for real-time anomaly detection.

### 2. **model-training-and-evaluation** 📊📈
- **Description**: Includes Jupyter notebooks and scripts for training, evaluating, and validating machine learning models for anomaly detection.
- **Contents**:
  - Datasets used for laboratory and industrial experiments.
  - Scripts for preprocessing thermal images and generating synthetic anomalies.
  - Implementation of anomaly detection algorithms (e.g., PaDiM, PatchCore, iForest).

### 3. **referenced** 📖
- **Description**: Stores references, related documents, and any other supporting materials for the project.
- **Contents**:
  - Academic papers and reports cited during the research.
  - Additional notes or documentation relevant to the development process.

## Features 🌟

- **Anomaly Detection Models**: Integration of state-of-the-art methods like PaDiM, PatchCore, and Isolation Forest.
- **Data Preprocessing Tools**: Automated scripts to process thermal images for model training.
- **Industrial Application**: Real-world data from battery recycling facilities provided by Bosch Rexroth.

## Setup & Usage 🚀

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PetrovEvgeniy/thermal-camera-diagnosis-app.git
