
## Step 1: Add a dataset
Create a new subfolder under `dataset` named after you, like `Charlie`. Find `headshots.py` and update row 3 precisely as you named the subfolder, like `Charlie`. Then run this command to open a new webcam window. Press the spacebar to take at least 10 pictures of your face from different angles. When you're done, **Esc** to close the window.

    $ python headshots.py

Repeat this step to add more friends, making sure to create a separate folder for each person.

## Step 2: Train the model
Run this command to analyze the photos, and create a new file `encodings.pickle` containing criteria for identifying these faces.

    $ python train_model.py

## Step 3: Test the model
Run this command to open a new webcam window. If your face is highlighted with a yellow box alongside your name, the model has been properly trained. Hit **q** to quit the program.

    $ python facial_req.py

## Step 4: Set up SendGrid email notifications
Create a new file called `.env` (notice the dot in front of the filename), formatted like `.env.example`. Save your API key from [the SendGrid settings](https://app.sendgrid.com/settings/api_keys) and other configuration details in this file.

Run this commnad to test your email is sending properly.

    $ python send_test_email.py

## Step 5: Add email notifications to facial recognition
Run this command to put it all together. If the webcam recognizes someone, it will snap a photo and send an email notification to announce the new arrival. 

    $ python facial_req_email.py

---
# Forked from this Raspberry Pi 4 Facial Recognition tutorial
https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition

