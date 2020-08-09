import sys, getopt

def main(argv):
    get_opt(argv)

def get_opt(argv):
   ismultiprocess = False
   try:
      opts, args = getopt.getopt(argv,"hi:m:",["ip=","ofile="])
   except getopt.GetoptError:
      print ('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
         sys.exit()
      elif opt in ("-m"):
         ismultiprocess = True
         multimode = arg
         print(f"multimode: {multimode}: {ismultiprocess}")
      elif opt in ("-n"):
         concurrent_num = int(arg)
         print(f"concurent_num: {concurrent_num}")
      elif opt in ("-i", "--ip"):
         ip = arg
         print(f'ip: {ip}')
   print(args)
   print(type(args))
   print(type(opts[0]))
   print(opts)

if __name__ == "__main__":
   main(sys.argv[1:])