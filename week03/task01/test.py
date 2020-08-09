import subprocess
import telnetlib
from threading import Thread
import getopt
import sys

def ishostalive(ip) -> bool:
    print(ip)
    result = subprocess.call(
        f'ping -w 1000 -n 1 {ip}', stdout=subprocess.PIPE, shell=True)
    return result == 0


def isportopen(ip, port) -> bool:
    server = telnetlib.Telnet()
    try:
        server.open(ip, port)
        return True
    except Exception:
        return False
    finally:
        server.close()


def get_opt(argv, optarg):
    try:
        opts, args = getopt.getopt(argv, "hi:m:w:", ["ip=", "ofile="])
    except getopt.GetoptError:
        print('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
            sys.exit()
        elif opt in ("-m"):
            optarg['ismultiprocess'] = True
            optarg['multimode'] = arg
            print(f"multimode: {opt['multimode']}: {opt['ismultiprocess']}")
        elif opt in ("-n"):
            optarg['multinum'] = int(arg)
            print(f"concurent_num: {opt['num']}")
        elif opt in ("-i", "--ip"):
            optarg['ip'] = arg
            print(f"ip: {optarg['ip']}")
    if optarg['ip'] == '':
        print('usage: python test.py [-i|--ip ip] [-m proc|thread] [-v] [-w outputfile]')
        sys.exit()
  

def multiproc():
    pass

def main(argv):
    opt = {
        'ismultiprocess' : False,
        'multimode' : '',
        'multinum' : 0,
        'outfile' : '',
        'ip' : '',
    }
    get_opt(argv, opt)
    ip = opt['ip'].split('-')

    print(ip)    
    print('开始ping测试')
    if ishostalive(ip):
        print(f'{ip} ping通了')
        for port in range(20, 100):
            if isportopen(ip, port):
                print(f'port {port} is open')
            else:
                print(f'port {port} is not open')
    else:
        print(f'{ip} 没有ping通')

if __name__ == "__main__":
   main(sys.argv[1:])
