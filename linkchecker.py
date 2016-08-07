import os
import urllib
import sys
import threading

def StartServer():
    try:
        print("\n Attempting To Start Server With Process ID " + str(os.getpid()))
        os.system('php -S localhost:80 -t ' + sys.argv[1])
    except(IndexError):
        print ("\n Server Startup Failed")
        print ("\n Error: Please Enter The Full Path of Your Web App Root directory")
def RetrieveIndexPage(URL):


if __name__ == '__main__':
    ServerProcess = threading.Thread(name="Link Testing Server", target=StartServer)
    ServerProcess.start()
    print("\n Server With Process ID " + str(os.getpid()) + " Has Started")
