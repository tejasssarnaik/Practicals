# Practicals 🚀

A comprehensive collection of machine learning and computer vision assignments showcasing practical implementations using Python, TensorFlow/Keras, OpenCV, and data analysis libraries.

## 📋 Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Assignment Categories](#assignment-categories)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains various practical assignments covering:
- **Computer Vision**: Real-time face detection and emotion recognition
- **Machine Learning**: Deep learning models with TensorFlow/Keras
- **Data Analysis**: Exploratory data analysis and visualization
- **Image Processing**: Fashion-MNIST dataset classification

## 🛠️ Technologies Used

- **Python 3.x**
- **TensorFlow/Keras** - Deep learning framework
- **OpenCV** - Computer vision library
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization

## 📚 Assignment Categories

### 1. Computer Vision & Real-time Processing
- **Face Detection & Emotion Recognition**
  - Real-time webcam face detection using Haar Cascades
  - Emotion classification using pre-trained deep learning models
  - Live video processing with OpenCV

### 2. Machine Learning & Deep Learning
- **Fashion-MNIST Classification**
  - Image classification using neural networks
  - Data preprocessing and visualization
  - Model training and evaluation

### 3. Data Analysis & Visualization
- **Boston Housing Dataset Analysis**
  - Exploratory data analysis (EDA)
  - Statistical analysis and visualization
  - Data preprocessing techniques

## 📋 Prerequisites

Before running the assignments, ensure you have:

```bash
Python 3.7+
Webcam (for computer vision assignments)
```

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Practicals.git
   cd Practicals
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install tensorflow opencv-python numpy pandas matplotlib seaborn scikit-learn
   ```

   Or install from requirements file:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Face Detection & Emotion Recognition
```bash
python face_emotion_detection.py
```
- Press 'q' to quit the camera feed
- Ensure your webcam is properly connected

### Fashion-MNIST Classification
```bash
python fashion_mnist_classification.py
```

### Boston Housing Analysis
```bash
python boston_housing_analysis.py
```

## 📊 Key Features

### Real-time Face Detection
- Uses Haar Cascade classifiers for face detection
- Integrates pre-trained emotion recognition models
- Real-time video processing capabilities

### Deep Learning Implementation
- TensorFlow/Keras model integration
- Image preprocessing and augmentation
- Model evaluation and visualization

### Data Analysis
- Comprehensive EDA techniques
- Statistical visualization
- Data preprocessing pipelines

## 🔧 Model Requirements

Some assignments require pre-trained models:
- `best_model.h5` - Pre-trained emotion recognition model
- Ensure models are placed in the correct directory structure

## 📈 Results & Visualizations

Each assignment generates:
- Training/validation accuracy plots
- Confusion matrices
- Data distribution visualizations
- Real-time prediction results
