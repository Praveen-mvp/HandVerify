import cv2
from cvzone.HandTrackingModule import HandDetector
import random

# Generate random numbers for left and right hands
def generate_hand_numbers(max_sum):
    """Generate two random numbers such that their sum is less than max_sum."""
    num1 = random.randint(0, max_sum - 1)
    num2 = random.randint(0, max_sum - 1)
    return num1, num2

# Initialize the webcam
cap = cv2.VideoCapture('/dev/video0')

# Initialize the HandDetector class
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

max_sum = 5
left_hand_number, right_hand_number = generate_hand_numbers(max_sum)

# Flag to indicate when the condition has been met
condition_met = False

# Continuously getting frames from the webcam
while True:
    # Capture each frame from the webcam
    success, img = cap.read()
    if not success:
        break  # Exit loop if frame capture fails

    # Find hands in the current frame
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Display the random numbers on the webcam feed
    cv2.putText(img, f'Right Hand: {right_hand_number}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img, f'Left Hand: {left_hand_number}', (280, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    if hands:
        right_hand_fingers = None
        left_hand_fingers = None

        # Process each detected hand
        for hand in hands:
            hand_type = hand["type"]
            lm_list = hand["lmList"]
            fingers = detector.fingersUp(hand)
            finger_count = fingers.count(1)

            # Store finger counts based on hand type
            if hand_type == "Right":
                right_hand_fingers = finger_count
                cv2.putText(img, f'Right Hand: {right_hand_fingers}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)


            elif hand_type == "Left":
                left_hand_fingers = finger_count
                cv2.putText(img, f'Left Hand: {left_hand_fingers}', (280, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Example condition based on hand type and finger counts
        if right_hand_fingers is not None and left_hand_fingers is not None:
            if right_hand_fingers == right_hand_number and left_hand_fingers == left_hand_number:
                # Check if the sum of displayed numbers is under 10
                print("Verified")
                condition_met = True  # Set the flag to indicate that the condition has been met
                # Display the success message on the image
                cv2.putText(img, 'Correct!', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the image in a window
    cv2.imshow("Image", img)
    
    # Exit loop if the condition is met
    if condition_met:
        break

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Allow manual exit with 'q'
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
