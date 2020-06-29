# Group4Project
_Code for Eden, Eric, Simon, Tony's Group 4 Project_

## Introduction
- In this project, we use Arduino to collect analog value of the voltage output by a solar panel.

- The Arduino control a servo to rotate from 0 deg to 180 deg, and collect the votage output in each degree.

- We send the data (degree and votage) from Arduino to a PC through USB.

- The PC logs the data, graphs the data, and saves the data in csv format.

## Files description

- Code run on Arduino is in folder `Arduino`.
- Code run on PC is in folder `PC`.

## How to use this program
1. Connect the Arduino with the PC through USB.
2. Modify the variable `PORT` in ./PC/main.py to the port Arduino connected to.
3. Run ./PC/main.py
4. The graph will be display. Click `Save` button to save the data to disk, click `Freeze` or `Unfreeze` button to freeze or unfreeze the graph and data.

