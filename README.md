# YOLOv5 Custom Object Detection

This project implements object detection using YOLOv5 with a custom dataset. The model is trained on Kitty Dataset, and it is capable of detecting 9 classes: ["Car", "Pedestrian", "Van", "Cyclist", "Truck", "Misc", "Tram", "Person_sitting", "DontCare"].

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sitiisyaroh/custom-yolov5-object-detection.git
   cd yolov5-object-detection
   
2. Download The Dataset from [Kitty Dataset]([https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_image_2.zip])
3. Set up and run split dataset.ipynb
4. Once the dataset is already clean and ready for training, setup and run training_yolov5.ipynb
5. Download the model from /weights/best.py
6. Load the model at predict.py


### Documentation
Some result from custom model:
![000039](https://github.com/user-attachments/assets/fb355971-c649-498b-a06e-089039166b2a)
