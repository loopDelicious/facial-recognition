
# Face recognition concierge to announce new visitors
This tutorial shows you how to train a facial recognition model to identify visitors and send an email announcing their arrival.

## Tutorial Requirements
- Python version 3
- A webcam (your laptop’s built-in webcam or an external one)
- A [free Twilio SendGrid account](https://signup.sendgrid.com/) to send up to 100 free emails per day

## Step 0: Clone repo and install dependencies
Clone this example project, and change into the directory from the command line.

    $ git clone git@github.com:loopDelicious/facial-recognition.git
    $ cd facial-recognition

Create a virtual environment called `venv`. Activate the virtual environment, and then install the required Python packages inside the virtual environment. If you’re on Unix or Mac operating systems, enter these commands in a terminal.

    $ python -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

If you’re on a Windows machine, enter these commands in a command prompt window.

    $ python -m venv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt

## Step 1: Create a custom face recognition dataset
Create a new subfolder inside `dataset` using your first name, like `Joyce`, to contain your photos.

    (venv) $ python headshots.py Joyce

Then run this command to open a new webcam window, passing in the name of your new subfolder. Use `headshots_picam.py` if using a Pi camera. Press the spacebar to take at least 10 pictures of your face from different angles. When you're done, **ESC** to close the window. Repeat this step to add more friends, creating a separate folder for each person.

## Step 2: Train the model

    (venv) $ python encode_faces.py

Run this command to analyze the photos and output a new file `encodings.pickle` that contains criteria for identifying these faces.

## Step 3: Test the model

    (venv) $ python facial_req.py

Run this command to open a new webcam window. If your face is highlighted with a yellow box alongside your name, the model has been properly trained. Hit **q** to quit the program.

## Step 4: Set up SendGrid email notifications
Create a new file called `.env` (notice the dot in front of the filename), formatted like `.env.example`. Save your API key from [the SendGrid settings](https://app.sendgrid.com/settings/api_keys) and other configuration details in this file.

    (venv) $ python send_test_email.py

Run this command to send a test email.

## Step 5: Add email notifications to facial recognition

    (venv) $ python facial_req_email.py

Run this command to open a new webcam window and try it out. If someone from your dataset is recognized, the webcam will snap a photo and send an email notification to announce the new arrival. 

---
## Attributions

### Forked from this Raspberry Pi 4 Facial Recognition tutorial
https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition

### Included code samples from these Face Recognition tutorials
https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/
https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
