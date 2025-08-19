# PetNet-50

**PetNet-50** is a web-based image classification demo built using a Convolutional Neural Network (CNN) with Transfer Learning from **ResNet-50**. Upload an image of a cat or dog, and the model will classify it for you!

Built by Marvin Guerrero-Rangel.

## 🎯 Purpose

This project was created to learn web dev. This is my first ever full stack app. 

## 📸 Features

- Upload a cat or dog image directly from your device
- Real-time classification using a trained ResNet-50 model
- Frontend in HTML/CSS/JavaScript
- Backend API using **FastAPI**
- Model trained with PyTorch and deployed locally

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **Model:** ResNet-50 from torchvision
- **ML Framework:** PyTorch
- **Deployment:**

## 🧪 How It Works

1. Upload an image from your device
2. The image is sent to the FastAPI backend
3. The model processes the image and returns a prediction (Cat or Dog)
4. The result is displayed instantly on the page

## 🏗️ Project Structure

PetNet-50/
│
├── backend/
│ ├── main.py # FastAPI server
│ ├── model.pth # Trained model
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── about.html
│ ├── demo.html
│ ├── style.css
│ ├── script.js
│ └── images/
├── .gitignore
├── LICENSE
└── README.md
