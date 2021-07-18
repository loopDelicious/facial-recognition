
# Face recognition concierge to announce new visitors
This tutorial shows you how to train a facial recognition model to identify visitors and send an email announcing their arrival.

## Tutorial Requirements
- Python version 3
- A USB webcam
- A [free Twilio SendGrid account](https://signup.sendgrid.com/) to send up to 100 free emails per day

## Step 0: Clone repo and install dependencies
Clone this example project, and change into the directory from the command line.

    $ git clone git@github.com:loopDelicious/facial-recognition.git
    $ cd face-recognition

Create a virtual environment called `venv`. Activate the virtual environment, and then install the required Python packages inside the virtual environment. If you’re on Unix or Mac operating systems, enter these commands in a terminal.

    $ python -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

If you’re on a Windows machine, enter these commands in a command prompt window.

    $ python -m venv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt

## Step 1: Add a dataset
Create a new subfolder under `dataset` named after you, like `Charlie`. Find `headshots.py` and update row 3 precisely as you named the subfolder. Then run this command to open a new webcam window. Press the spacebar to take at least 10 pictures of your face from different angles. When you're done, **ESC** to close the window.

    (venv) $ python headshots.py

Repeat this step to add more friends, making sure to create a separate folder for each person.

## Step 2: Train the model

    (venv) $ python train_model.py

Run this command to analyze the photos and create a new file `encodings.pickle` that contains criteria for identifying these faces.

## Step 3: Test the model

    (venv) $ python facial_req.py

Run this command to open a new webcam window. If your face is highlighted with a yellow box alongside your name, the model has been properly trained. Hit **q** to quit the program.

## Step 4: Set up SendGrid email notifications
Create a new file called `.env` (notice the dot in front of the filename), formatted like `.env.example`. Save your API key from [the SendGrid settings](https://app.sendgrid.com/settings/api_keys) and other configuration details in this file.

    (venv) $ python send_test_email.py

Run this commnad to test your email is sending properly.

## Step 5: Add email notifications to facial recognition

    (venv) $ ython facial_req_email.py

Run this command to put it all together. If the webcam recognizes someone, it will snap a photo and send an email notification to announce the new arrival. 

---
# Forked from this Raspberry Pi 4 Facial Recognition tutorial
https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition
