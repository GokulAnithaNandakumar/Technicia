### Gesture Controlled OS

Gesture Controlled Virtual Mouse makes human-computer interaction simple by utilizing Hand Gestures. The computer requires almost no direct contact, and all input/output operations can be virtually controlled using static and dynamic hand gestures. This project leverages state-of-the-art Machine Learning and Computer Vision algorithms to recognize hand gestures and voice commands, providing smooth interaction without any additional hardware requirements. It consists of two modules: one which directly works on hands using MediaPipe Hand detection, and the other which makes use of gloves of any uniform color. Currently, it works on the Windows platform.

### Future Applications
1. **Hospital Surgery Room**: Surgeons can control vital monitors for patients' data history without contaminating gloves, ensuring a sterile environment during surgeries.
2. **Billing Kiosks**: Users can navigate through billing kiosks in public spaces without physically touching the screen, enhancing hygiene and reducing the spread of germs.
3. **Car Infotainment System**: Drivers and passengers can control various functions of the car's infotainment system through hand gestures, allowing for safer and more convenient operation while driving.

### Frameworks, Libraries, and Technologies Used
- **MediaPipe**: Used for hand detection and landmark recognition.
- **OpenCV (cv2)**: Used for capturing video frames, image processing, and drawing landmarks.
- **PyAutoGUI**: Used for controlling mouse movements and clicks.
- **Math**: Used for mathematical calculations related to distances and ratios.
- **PyCaw**: Used for controlling system volume.
- **Screen Brightness Control**: Used for controlling system brightness.
- **Enum**: Used for defining enums for hand gestures and multi-handedness labels.
- **ctypes and comtypes**: Used for controlling system volume and interacting with Windows components.

### Instructions for Running
To run the Gesture Controlled OS, follow these steps:

1. Ensure you have all necessary libraries installed (MediaPipe, OpenCV, PyAutoGUI, etc.).
2. Clone the repository to your local machine.
3. Navigate to the directory containing the code.
4. Run the Python script.
5. Position your hands in front of the camera and perform gestures to control the OS.

### Contributors
This project was developed by Team Spongebob during a hackathon.

- [Developer 1 Name]
- [Developer 2 Name]
- [Developer 3 Name]

For any inquiries or issues, please contact [Project Maintainer Email].
