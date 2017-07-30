# pythots
Class enrollment bot

Need to download the chrome driver
https://sites.google.com/a/chromium.org/chromedriver/downloads

Then extract the .exe from the download

The get the path of the .exe file and hardcode into the python code
  - use readlink -f chromedrivier when your in the chrome driver directory
  -copy and past this path into the chrome_path variable

Also need to pip install selenium


For testing class enrollment use course number 328 to succesfully enroll
For a failure use class code 12345 to test error check




helpful selenium link: 
https://www.youtube.com/watch?v=bhYulVzYRng


really in depth selenium link:
https://www.youtube.com/watch?v=l15ZJAbxCL8&t=2527s

selenium docs:
http://selenium-python.readthedocs.io/
