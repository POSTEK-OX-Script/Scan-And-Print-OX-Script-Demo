# Scan-And-Print-OX-Script-Demo

This code is designed to take in data from a external scanner through USB and print a label with the scanned data. This specific demo takes in two scans and have a specific label layout already, but you can use whatever design or however many scans as you would like per label. 

## Demo video

A demonstration of what this script can do can be found here
https://www.youtube.com/watch?v=qDKJzS-VcvI

A tutorial video on walking through the development process of this script can be found here
https://www.youtube.com/watch?v=2IPcM7ErJjY&t=44s

## Installation

To run this code, you will need to have Python 3.8+ installed on your printer(which comes standard on all POSTEK Printers that support OX Script after May 2023). You will not be able to execute this code directly on your computer as it is intended to be executed on the printer

## Usage

To execute this demo, simply load the .py file and commands1.txt(file for the label design) into your printer through the POSTEK App. Then to run the program you can initate it from the printer touch screen or the POSTEK App. 

- Initating the program from printer touch screen
    - On your printer's touch screen, go to settings>Ox Script>[your file name].py. Press it and select run from the bottom right of the pop-up window
 
- Initating the program from the POSTEK App
    - Inside the App, select Ox Script from the left hand side. Connect to the printer that you just moved the files to and select the file from the left hand side drop down, click run on the top right hand corner

## License

This code is released under the MIT License. Please see the LICENSE file for more information.

## Disclaimer

This software is provided "as is" and the author of the software is not liable for any damages or losses that may arise from the use of the software. Use at your own risk.
