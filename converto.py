##
##Convert your favourite youtube videos to mp3.
##Or just use it to download songs that you like.
##.................................................
##usage:
##    python converto.py
##    Then the rest is all On screen. :)
##.................................................
## BY: MAYANK AGARWAL, NIT Durgapur
##

import requests
import time,re,os,sys

#Check for lxml
try:
    from lxml import etree as ET
except ImportError:
    try:
        import xml.etree.ElementTree as ET
    except:
        print "Failed to import ElementTree. Install lxml and try gain."
        time.sleep(2)
        sys.exit(0)

#check for notification library.
try:
    from gi.repository import Notify
except:
    print "No 'libnotify' module found. You wont be getting Desktop Notifications.\n"


#Func for desktop notifications. Not available on Windows.
def notif(msg):
    try:
        Notify.init("Converto")
        notifc=Notify.Notification.new(msg)
        notifc.show()
        Notify.uninit()
    except:
        pass


#Searches youtube for the given string and returns the video url for the searched string.
#But the returned url might not be very appropriate in some cases.
#So it is recommended to be specific while entering the song/video name, though not necessary.

def getVidURL(songName):
    print "\nSearching for %s..." %songName
    dicData={"search_query":songName}
    try:
        yTube=requests.get("http://www.youtube.com/results",params=dicData).text
    except:
        print "No internet connection. Check and try again."
        notif("No internet connection. Check and try again.")
        time.sleep(1)
        sys.exit(0)
    vidID=re.findall(r'href=\"\/watch\?v=(.{11})',yTube)[1]   #r'href=\"\/watch\?v=(.{11})'       r'data-context-item-id="(.*?)"'
    print "vidID: ",vidID
    vidURL="http://www.youtube.com/watch?v="+vidID
    return vidURL



#Func makes a connection to listentoyoutube.com which basically does the conversion.
#Then the func finds the url to the xml document of the converted file which gives the details after parsing with lxml.

def getSongDetails(vidURL):
    convURL="http://www.listentoyoutube.com/cc/conversioncloud.php"
    dicData={'mediaurl':vidURL}
    print "\nConnecting to server..."
    try:
        page=requests.post(convURL,data=dicData).text
    except:
        print "Server error.. !!! Program is exiting.."
        notif("Server error.. !!! Program is exiting..")
        time.sleep(1)
        sys.exit(0)
    statusURL=page.split(',')[1].split('"')[3].replace('\/','/')
    xmlPage=requests.get(statusURL).content
    print "Connected... :) "
    time.sleep(1)
    tree=ET.fromstring(xmlPage)
    try:
        songURL=tree.find('downloadurl').text
        fileSize=tree.find('filesize').text
        songName=tree.find('file').text
    except:
        print ("\nError.. BAD FILE !!! Either file too large for conversion or BAD CONNECTION to server.")
        print ("Program is exiting. Try again with a more specific search string.")
        notif("BAD FILE ERROR !!!")
        time.sleep(5)
        sys.exit(0)
    return songURL,fileSize,songName



#It basically makes connection to the song url (ending in .mp3) and
#then write bytes to a file. Hence Downloads the song.

def downloadSong(songName,songURL):
    locn="Songs"
    if not os.path.exists(locn):
        print "\nCreating Songs directory for you..:) This will be done only for the first time."
        os.makedirs(locn)
    os.chdir(locn)    #(os.path.join(locn,songName))
    if not os.path.exists(songName):
        print "Downloading %s.. Please wait.." %songName
        fileName=songName
        startTime=time.time()
        getsong=requests.get(songURL,stream=True)
        with open(fileName,'wb') as fs:
            for chunk in getsong.iter_content(chunk_size=1024):
                if chunk:
                    fs.write(chunk)
        endTime=time.time()
        os.chdir("..")
        print "\nDownlaod Complete.. :) You can check Songs folder.\n Download time: %ss" %str(round(endTime-startTime))
        notif("\nDownlaod Complete.. :) You can check Songs folder.\n Download time: %ss" %str(round(endTime-startTime)))
    else:
        print "\nSong already exists in your Songs directory.. !!!!!!!!!!!!!!!!!"
        notif("\nSong already exists in your Songs directory.. !!!!!!!!!!!!!!!!!")



# MAIN program. Execution starts here.

def main():
    while True:
        songName=raw_input("\nEnter the song/video name (a-z or enter to exit): ")
        if(len(songName)<=1):
            print "\nQuiting this wonderful program in 3s.. :D\n"
            time.sleep(2)
            sys.exit(0)
        else:
            vidURL=getVidURL(songName)
            songURL,fileSize,songName=getSongDetails(vidURL)
            print"\n::::: %s :::::" %songName
            choice=raw_input("\n %s will be downloaded.\n Enter y/Y to continue or any key to cancel: " %fileSize)
            if(choice=='y' or choice=='Y'):
                print "\nDownload will start in 1s. You will be notified once completed. :) "
                time.sleep(1)
                downloadSong(songName,songURL)
            else:
                print "\nThat was not that big a file to cancel.. :p "
                ch=raw_input("Want to downlaod some other mp3s that you wish not to cancel..? :D (y/n): ")
                if(ch=='y' or ch=='Y'):
                    continue
                else:
                    print "(-.-) Ok.. Quiting in 30s :)\n"
                    time.sleep(2)
                    print ":D :D "
                    sys.exit(0)
        

if __name__=='__main__':
    main()
