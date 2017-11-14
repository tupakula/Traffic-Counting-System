# Traffic Counting System Project

Using OpenCV to detect and count moving vehicles.

# Pre-preparation steps:

Step 1: Install OpenCV for a Raspberry system

  1. Update installed packages
    
    `sudo apt-get update`

    `sudo apt-get upgrade`
    
    `sudo rpi-update`
  
  2. Install OpenCV
    
    `sudo apt-get install libopencv-dev python-opencv`

    If you want the latest version of OpenCV you should make it from source. (but I'm lazy :)
  
    To test the installation:
    
    `python`
    
    `>>> import cv2`
    
    `>>> cv2.__version__`
    
Main steps of the image processing

Step 1. Read the video frame by frame.
  
Step 2. Apply some fileters to the frame(dilation, etc.).
  
Step 3. Use BackgroundSubtractor to split the foreground from background(white-foreground, black-background).
  
Step 4. Detect the contours of the foreground(moving objects).
  
Step 5. Calculate the centroid of each moving object.
  
Step 6. For each centroid, detect if there's a nearby centroid of the last frame. If so, assign them to the same vehicle.
  
Step 7. For each vehicle, detect whether it crossed the target line.
 
Finally run "main.py" file and see results and checkout "logfile.txt" for total vehicle count

Thank you.
