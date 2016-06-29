# converto.py
Converts and downloads YouTube videos as mp3 file :musical_note: . Great for downloading your favorites songs or how about listening to a lecture/seminar/workshop etc on the go. :relieved:

_**NOTE: Written in python 2.7**_

##Salient features:
* _You just need to enter the name of the song or video you wish to download as mp3._ :notes::notes:
* _It will create a Songs direcory as well in your current directory so that all your downloads are in one place._
* _Incase you already have the song downloaded in the Songs folder, then its not gonna download the same song again._
* _Will ask for download conformation. Just incase you not happy with the file size at that moment._
* _What after conformation? Go do whatever till the file is downloaded. Upon completion it shows a desktop notification so that you need not keep looking at your shell from time to time._ (**NOTE:** Not available on windows.)

####Assumption:
 You have python installed. :stuck_out_tongue_winking_eye:
 
#Dependencies:
 It mostly uses the pre-installed modules. Rare that you will miss out any of it. :wink:
 * **requests** - to make http requests to server. (ex POST, GET etc..) 
 * **re** - regex library to search strings.
 * **os, sys** - for creating directories and doing OS independent tasks.
 * **time** - just to make the time count. :clock1: :clock2: :clock3:
 * **lxml** - used for parsing xml and html. Incase you dont have it installed, go here: [lxml] (http://lxml.de/installation.html)
 * **libnotify** - which is basically the notify module imported from gi.repository. Used for desktop notification. And is not available for windows.
 
#Usage:
open terminal-->browse to the directory where you have **converto.py** saved-->Then run:

```$ python converto.py```

Then the rest is all on the screen. :wink:

#Developer
 
 **Name: [Mayank Agarwal] (https://github.com/mayank1495) :sunglasses:**
 
 **Institute: NIT Durgapur**


