import os, sys, threading
print("[+] DBG ID ON/OFF DATA SVC\n")
def svc(i):
   print("Mematikan data\n")
   os.system('su -c "svc data disable"')
   print("Menghidupkan data\n")
   os.system('su -c "svc data enable"')
if __name__ == '__main__':
 for i in range(1):
  t= threading.Thread(target=svc,args=(i,))
  t.start()
  break