# VergeComputer

Steps to setup:
1. Copy Verge folder to the desired folder/destination
2. Open existingBalance.txt and set value to 0
3. Open poolPayouts.txt and delete everything after the first line. Put your cursor to the end of the line and hit return once. Save and close. (This sets the stage for the first entry to go into the file)
4. Open VergeComputer.py
  a. Everywhere where it says "yourPath/blah", replace this with the full directory path to get to the Verge folder.
  b. Change your address on line 8.
  c. **if youre not mining Verge** You will need to change the following lines.
    i. Line 8: this is the block explorer used for your coin. You will need to find a similar API endpoint that points to your        coin
    ii. Line 11: Depending on the json response received from Line 8, this may need to be changed to find the correct balance         parameter
    iii. Line 25: this is just a simple coinmarketcap endpoint and can probably just have the name changed from /Verge/ to             /Bitcoin/, for example
5. **MAC ONLY, WINDOWS WILL NEED TO FIND A DIFFERENT TASK SCHEDULER**
  a. Open Terminal and paste the following: env EDITOR=nano crontab -e
  b. Once the crontab opens, paste the following without quotes: "30 */4 * * * python yourPath/blah/Verge/VergeComputer.py"
    i. Obviously replace yourPath/blah with the path you created in 4-a above.
    ii. 30 */4 * * *  - this means the task will run at 30 minutes past the hour, every 4th hour. you can go to                       https://crontab.guru/ to customize your scheduling
    
Good Luck!! 
