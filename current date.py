import datetime
def main():
   now = datetime.datetime.now()
   print ("Current date and time : ")
   print (now.strftime("%Y-%m-%d %H:%M:%S"))
main()
