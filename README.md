# VideoStreamerSwitcher
This code was developed to capture video from a USB camera and stream it to a web page. It is designed for use on a Raspberry Pi.

## Code Features:
Multiple video streams are transmitted via USB, but the Raspberry Pi cannot process/display them simultaneously.
Therefore, to ensure proper functionality, the system was designed so that each device turns on and off when switching between streams.
However, on a regular PC, it's possible to display two video streams at the same time without issues.
To use the code, follow these steps:

### Using code.
1. Download code.
2. Install the required libraries:
   
   2.1. sudo apt install python3-flask

   2.2. sudo apt install python3-opencv

After installing the libraries, you can run the code.
If you want to change the IP address and port, modify the default values in the line of code:
if __name__ == "__main__".


Page view:
<img width="571" alt="image" src="https://github.com/user-attachments/assets/e059737f-181d-4638-94cd-bf9bbf8797dd" />
