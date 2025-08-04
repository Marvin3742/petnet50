from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from torchvision import models, transforms
import torch
import torch.nn as nn
from PIL import Image
import io

# Define class names (must match the order of folders in ImageFolder)
class_names = ['Cat', 'Dog']

# Load model architecture
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(512, 2)  # Binary classification
model.load_state_dict(torch.load("model/model.pth", map_location="cpu"))
model.eval()

# Define transforms (must match training transforms)
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Initialize FastAPI app
app = FastAPI()

# Allow local frontend (adjust origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "PetNet-50 API is live!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        img_tensor = transform(image).unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            outputs = model(img_tensor)
            _, predicted = torch.max(outputs, 1)
            prediction = class_names[predicted.item()]

        return JSONResponse(content={"prediction": prediction})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
