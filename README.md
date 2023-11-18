# H.A.Y-bot-
The Python script uses Tkinter for a graphical mood rating interface, prompting users at specific times. Scheduled by a cronjob, it records user moods, date, time, and a daily joke in "logs.csv," with error handling for file operations.


## What modules will it use
- **tkinter**: for the GUI
- **CSV**: to keep track of the time the user logged in
- **datetime**: to find the time and date
-  **random**: to select a random joke from the default jokes
