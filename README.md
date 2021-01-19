# photoFrameV2
This is a new type of digital photo frame, which auto rotates the display based on the photo orientation. We can enjoy all photos with their original layout. 
This python script reads the images from a folder ( or can be set up to read from a USB) and then calibrates the image orientation and sends an instruction to the servo controller to rotate the screen accordingly. 

# Hardware components
1.	Any raspberry pi (Used raspberry pi 3)
2.	Pololu servo controller (Any other servo controller also is fine or Arduino also is fine)
3.	Hitec RCD 31422S HS-422 Deluxe Servo
4.	GeeekPi 7 inches 1024 x 600 HDMI Screen LCD (Any HDMI display is fine. Portable display is a perfect option due to built-in display controller)
5.	Any USB if you want to read the images from USB.

We can build the Auto-Rotating photo frame hardware with any box or wooden bricks. I have used old wooden bricks set for this setup, or We can use old photo frames. 


# Setup
I have used Pololu's Maestro servo controller to control the servo position and its speed. Please refer to this tutorial at https://github.com/FRC4564/Maestro/ to set up the servo. 
Once the servo controller setup is complete, you can use the servo.py python program to find the horizontal and vertical positions. I have kept the speed and acceleration to a low value for smooth rotation.
Changes required
1.	We should then replace these calculated servo positions in the photoframe.py python script.
2.	Add some images to the folder wallpaper.
3.	We need to update the screen resolution to 1024, 768 or update the code "pygame.display.set_mode((1024, 768))" to match the screen resolution.
4.	We need to update the variables 'picPath' and 'path' in the photoframe.py python script to the desired photo location and the current script location.
5.	We need to add this line to "@reboot python3 /home/pi/photoFrameV2/photoframe.py &" in the crontab -e to start the script during raspberry pi boot.

Execute the photoframe.py python script and enjoy the Auto-Rotating Photo Frame. The attribute 'mode' setup with a non-empty value will exclude the servo controller logic and debug in the laptop.
Please update the 'picPath' path in the script to the USB mounted location for reading the photos from the USB.
