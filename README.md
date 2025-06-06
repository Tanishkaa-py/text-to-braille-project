
🔠 Text-to-Braille Translation for Accessibility

 👁️‍🗨️ A project to convert English text into Braille using AI and Arduino, designed to empower visually impaired individuals.



📌 Project Description

This project translates typed English text (A–Z) into Braille characters using:

- 🧠 Python & Flask for the web interface and Braille image display  
- 💡 OpenCV for handling Braille images  
- 📟 Arduino for converting Braille to tactile hardware signals  
- 💻 A `.exe` file that runs the entire app on Windows


🎯 Objective

To make written content more accessible by dynamically converting it into Braille, both visually (on screen) and physically (through Arduino).


## 🗂️ Project Structure


text-to-braille/
│
├── app.py                     # Main Flask app
├── braille_logic.py           # Braille image logic
├── braille_arduino.ino        # Arduino sketch (C++)
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # Web interface
├── Data/
│   └── a.jpg, b.jpg, ..., z.jpg  # Braille image files
├── Images/
│   └── web_interface.png, arduino_setup.png
└── README.md
```

 🚀 How to Run

 🖥️ Option 1: Run via Source Code

1. Install Python (3.x) and `pip`
2. Open terminal in the project folder and run:

```bash
pip install -r requirements.txt
python app.py
```

3. Open browser → `http://127.0.0.1:5000`  
4. Enter text → see Braille images


 🧩 Option 2: Download `.exe` File

If you don’t want to install Python, just download and run the `.exe` file:

📥 [Click to Download app.exe](https://drive.google.com/file/d/1pdBOKl2FFazGxU-XQEKntmUbf6IhFilE/view?usp=sharing)

> ⚠️ Make sure Arduino is connected via USB and loaded with the `.ino` sketch.

---

 🛠️ Arduino Setup

1. Open `braille_arduino.ino` in Arduino IDE
2. Connect your Arduino Uno via USB
3. Select the correct board and port from Tools
4. Click Upload (✓)

Arduino will receive dot-patterns over Serial and activate corresponding Braille pins (LEDs, motors, etc.).

---

 💡 How It Works

- Flask app receives text input
- Braille images are matched and shown on-screen
- Braille dot signals are sent to Arduino through Serial (COM port)
- Arduino lights up physical dots or activates tactile output

---

📦 Dependencies

Install all Python packages using:

```bash
pip install -r requirements.txt
```

Required libraries:
- Flask
- OpenCV (`cv2`)
- Numpy
- PySerial (for Arduino communication)

---


## 🧠 AI Model Training (CNN)

The project uses a **Convolutional Neural Network (CNN)** to learn and classify Braille patterns.

### 🧪 Preprocessing

Each Braille image is:

1. Converted to grayscale  
2. Resized to 64×64 pixels  
3. Normalized (pixel values scaled between 0 and 1)

```python
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, IMAGE_SIZE)
    img_normalized = img_resized / 255.0
    return img_normalized
```

### 🧠 CNN Architecture

The CNN has:

- 3 convolutional layers with ReLU activation
- Max pooling layers
- Fully connected (dense) layers
- Softmax for classification

```python
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])
```

### 📊 Evaluation Metrics

The trained model was evaluated using:

- ✅ **Accuracy Score**
- 📃 **Classification Report**

```python
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred))
```

These metrics helped validate the model's ability to correctly classify Braille character images.

---


## 👨‍💻 Author
Tanishka Jain  
2025 

---
