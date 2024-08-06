# HandVerify: Gesture-Based Number Verification

## Description

**HandVerify** is an innovative application that combines computer vision with hand gesture recognition. The application displays a random number on the screen via the webcam feed, and the user needs to show that number using both hands. The system then verifies if the displayed hand gesture matches the number and prints a "Verified" message in the terminal.

## Features

- **Random Number Display**: The application generates and displays a random number on the webcam feed.
- **Two-Hand Gesture Recognition**: Detects and interprets hand gestures shown with both hands in front of the camera.
- **Real-Time Verification**: Instantly verifies if the hand gesture corresponds to the displayed number.
- **Terminal Feedback**: Prints "Verified" in the terminal if the gesture matches the number.

## Installation

To install the necessary dependencies, clone this repository and run:

```bash
pip install -r requirements.txt
```

## Usage

To start the application, run:

```bash
python3 main.py
```
Once the application is running, a random number will appear on the screen via the webcam feed. Show the number using both hands (e.g., holding up five fingers on one hand and two fingers on the other for the number 7). If the gesture matches the displayed number, the application will print "Verified" in the terminal.

## Configuration
No special configuration is needed. However, ensure your webcam is properly connected and accessible by the application.

## Example
Here’s a basic flow of how the application works:

The application displays the number "7" on the webcam feed.
You show the number "7" using both hands (e.g., five fingers on one hand, two fingers on the other).
The application recognizes the gesture and prints "Verified" in the terminal.

## Acknowledgments
This project utilizes code from the CVZone repository. A big thank you to the authors for making this available to the community.

## Contact
For any questions or suggestions, feel free to contact:

Author: [Praveen]
Email: mvpraveenvijayakumar@gmail.com


