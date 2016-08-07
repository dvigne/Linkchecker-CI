import os
import http.client
import urllib.request
import sys
import threading
import time

def StartServer():
    try:
        print("\n Attempting To Start Server With Process ID " + str(os.getpid()))
        os.system('php -S localhost:80 -t ' + sys.argv[1])
    except(IndexError):
        print ("\n Server Startup Failed")
        print ("\n Error: Please Enter The Full Path of Your Web App Root directory")
    # WIP: Catching Keyboard Interups From Ctrl+C
    except(KeyboardInterrupt):
        print ("\n Server With Process ID " + str(os.getpid()) + " Has Stopped")

class HTTPRequester():
    def TestRetrieveIndexPage(self):
        URL = 'localhost'
        TestURL = http.client.HTTPConnection('localhost')
        TestURL.request('GET', '/')
        Page = urllib.request.urlopen('http://' + URL + '/')
        PageContents = Page.read()
        print ("Test Access To 'localhost' Reponse: ")
        print (response.status, response.reason)

if __name__ == '__main__':
    ServerProcess = threading.Thread(name="Link Testing Server", target=StartServer)
    ServerProcess.start()
    time.sleep(3)
    RequestPage = HTTPRequester()
    RequestPage.TestRetrieveIndexPage()
