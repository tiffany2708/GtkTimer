# GtkTimer
A simple, distraction-free timer for Linux users.
## Why this timer?
Do you get distracted by ticking sounds, flashing numbers, or complex interfaces? GtkTimer is designed for you. It is a very simple, calm timer that helps you stay focused without unnecessary sensory overload.

## Who is this for?
This app is built specifically for **Linux** users. If you are using Ubuntu, Fedora, Debian, or any other Linux distribution, this tool will integrate perfectly with your desktop.

## Installation
First, download the code from this page — either by clicking "Download ZIP" or using the standard git clone command. Extract the archive to a convenient location on your computer.
Next, make sure you have Python 3 installed on your system. Most Linux distributions (Ubuntu, Fedora, Debian) come with it pre-installed. You can verify this by opening a terminal and typing python3 --version. If Python is not installed, you can find it in your system's app store.
Inside the program folder, you'll see two files:
visual_timer.py — the main Python program
start-timer — a helper script for easy launching
To allow your system to run the helper script, you need to execute one command in the folder with the code: chmod +x start-timer. This is a standard Linux procedure that makes the file executable. You only need to do this once.

## Usage
Open your terminal and navigate to the program folder using the cd command. Then type ./start-timer followed by the number of minutes you want. For example, ./start-timer 45 will start a 45-minute timer. The dot and slash at the beginning (./) tell the system to look for the file in the current folder.
After launching, a small circle will appear in the top-right corner of your screen. It will gradually change color to show how much time remains. The terminal will be freed immediately — you can close it or use it for other tasks.
Controls:
1. Click the circle — starts or stops the timer.
2. Drag the window — click and drag the top bar to move the timer anywhere on your screen
3. Keep on top — press Alt and Space together while hovering over the timer window. A menu will appear — select "Always on Top". After this, the timer will stay visible above all other programs.
