
# DE-Final-Pitop-Project
Repo for Digital Electronics final project 

## **General description:**
This project is meant to be a detection system which will send an alert when the outside conditions are too high or too low. At first when it is turned on it will be in an idle state where it is on but it is not actively monitoring the area around it. Then when a button is pressed it will enter an "active" state. The active state is meant as a transitional state for one to enter in their desired control values, being the light control, the sound control and their respective ranges. Once all the values have been inputted the device will then enter a "set" state. In the set state it is actively monitoring the area around it with a light and sound sensor and displaying a reading for both. If the button to switch the device from idle to active is pressed again during the set state the device will go back to being idle. When the sensor detects either the light or the sound value going outside the range it enters an "alert" state. During the alert state the device releases an alarm indicating that one of the values is outside the range. However if both of the sensors detect that the light and sound are both within the desired range again it will re enter the set state from the alert state. Lastly if the button is pressed during the alert state it will automatically reset everything and go back to the idle state

## **Problem to be solved:**
Create a device that monitors conditions in a certain area and sends an alert when conditions are too far from a certain control value. Used to help with the maintenance of things that may need a specific set of conditions within a specific range. I.e a type of plant that may require certain light conditions to be healthy. 

## **The Sensors and attachments:**

First there are LEDs that indicate what state the system is in. No LEDs mean it is either off or idle, the green LED means it is "active", the green and yellow LED together indicates it is "set", and the red, yellow and green LEDs all together means it is "alert".

Secondly there is a button that be used to transition from the idle state to the "active state", furthermore it can also be used during the set and alert state and set the device back to being in the idle state.

Then there is a light sensor which monitors the light reading around it, updating at around 0.1second intervals. The light sensor checks that the light reading is within the specified range and if it isn't the device will enter the alert state. However if the reading re enters the set light value range then thye system may revert to being just "set" if the sound value is also within the range.

Similarly so the light sensor the sound sensor monitors the area around it and checks if the sound value exceeds the specified range, becoming alert if it does so. Then it can revert back to being "set" if the sound reading re enters the acceptable range in conjunction with the light reading.

Lastly there is a buzzer which serves as an additional feature of the alert state to help indicate it being in said state and draw attention to the alert.

## **Functions of the device:**
First of all it has the ability to switch between the 4 different states of idle, active, set and alert. Idle represents the device not being active or monitoring the area around it. Active state serves as more of a transitional state where the user has the ability to set the control values and ranges for the device. The set state means that the control values and the ranges have been set and the deivce is actively monitoring the area around it, displaying the values of both the light and sound reading. Lastly the alert state indicates that either the light or the sound value are currently too high or too low to the point of being outside the range.

Secondly it has the ability to actively monitor the readings of the light and sound values around it through the use of the sound and light sensors.

Next it has a display that not only helps indicate the current state in addition to the indicators from the LEDs, but also displays the readings for both the light and sound values when either set or alert.

Furthermore it has the abiltity to take in user inputs for a light and sound control as well as a respective range for each. This creates a set range where neither reading can exceed the control values plus the range nor can they go below the control value minus the range.

## **Timeline/Outline:**

Make the text display idle when initially turned on

Add the active state that can be initiated by pressing a button

Add active state indicators(green LED + active display)

Add the ability to set the control values and the ranges through prompts on the consol

Add the set state when values have been set

Add set state indicators(yellow LED + set display)

Make set state be able to switch back to idle when button is pressed again

Add the variables for the light and sound sensors

Add displays of the light and sounds readings on the miniscreen

Add alert state and ability to become alert when the readings exit the range

Add alert state indicators(red LED, Buzzer, alert display)

Make alert state go to idle when button is pressed again

Add ability to switch back to set when the readings re enter the set range

## **Code desciption:**
Designations set for sensors

Variables for readings set

Variable for ranges and controls set to -1

Check to make sure the pitop is currently on and hasn’t been turned off

Display as being idle

If button is pressed enter the active state

While active display so and turn on the green LED.

Prompt the user to enter their desired value for the light control, sound control, light range and sound range in that order

When all 4 control and ranges are no longer -1 switch to set state

While set display set and turn on the yellow LED

Display the readings from the sensors on the screen

If button is pressed go back to idle state(controls and ranges set back to -1 both LEDs turn off and display idle)

Check the display values and switch to alert when one goes outside the range

While alert continue to display the sensor readings

Turn on the red LED as well as the buzzer and display alert

If both readings re enter the range switch back to being set(turn off buzzer, red LED and go back to displaying set)

If button is pressed go back to idle state(turn off everything, set controls and ranges to -1 and display idle)

## **Challenges and lessons learned:**

Challenges I initially faced included the optimization because iniitially I had a lot of redundant code for the swtiching of states, espescially for switching from set or alert back to idle. 

Another challenge was that I initially had trouble setting up the states as initially it would be in both states simulataneously and display both messages for the respective states. Furthermore the initial switching between states was inconsistent due to varying reasons such as the sensors not updating or the button not consistently switching states.

Next another challenge was learning how to code in python which although not too difficult espescially considering the relative simplicity of the project, was still somewhat of a challenge to get used to in comnaprison to java.

Lastly I had some issues with Github uploading because of the format of the pitop coder and not being able to access my other tabs in conjunction with the coder.

Some lessons I learned was I familiarized myself with github more through the editing of the Readme and through figuring out how to commit my code to pitop from the pitop coder.

In addition I feel like I got better with decoding anbd optimizing through working on and debugging the code as well as through the optimization of it at the end.

<img width="733" height="594" alt="Screenshot 2026-01-09 143158" src="https://github.com/user-attachments/assets/746a457c-663d-4e05-b592-f5053c120de9" />
<img width="1052" height="668" alt="Screenshot 2026-01-09 143232" src="https://github.com/user-attachments/assets/0c927879-bf85-421c-87a7-8e69882a9a8c" />
<img width="262" height="341" alt="Screenshot 2026-01-09 143704" src="https://github.com/user-attachments/assets/d8fb4881-5a76-4847-8bc6-c8e79e42b10f" />

<img width="250" height="187" alt="Screenshot 2026-01-09 143740" src="https://github.com/user-attachments/assets/d0ec1625-069c-47d8-9982-735a91ab5145" />

Demonstration: watch top to bottom (full video was too big)

https://github.com/user-attachments/assets/4ed70f8e-a83e-4e7c-9fe9-e6b7c05f579b

https://github.com/user-attachments/assets/ab8c25e4-8f3d-4e75-96bf-2fbc396781e8

https://github.com/user-attachments/assets/daac4393-db19-4dfe-923e-e04ba49de47d

https://github.com/user-attachments/assets/bb21aaa4-e932-43ff-b4f0-0c00461a20d3









