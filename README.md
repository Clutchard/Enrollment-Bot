# Class enrollment bot

A bot that will help you add (mainly closed) courses to your schedule at fsu.

Refreshes page every 2 to 15 seconds to continually try and add your course to your schedule.

Need to have google chrome downloaded

Need to download the chrome driver
https://sites.google.com/a/chromium.org/chromedriver/downloads

Then extract the .exe from the download

The .exe file needs to be in your home directory

Also need to pip install selenium


For testing class enrollment use course number 328 to succesfully enroll

For a failure use class code 12345

For a class with a lab 12515

For testing the loop in shopping cart use 1876

If class has a lab and everything fails. Worse case put class in shopping cart and choose option 3 to try to add.

Can only have one class in shopping cart at a time.

helpful selenium link: 
https://www.youtube.com/watch?v=bhYulVzYRng


really in depth selenium link:
https://www.youtube.com/watch?v=l15ZJAbxCL8&t=2527s

selenium docs:
http://selenium-python.readthedocs.io/


Bug Report:
  
  -Specific class number won't work if a lab is attached to class
  
  -Course Name and number search doesn't account for results being greater than 50 classes
