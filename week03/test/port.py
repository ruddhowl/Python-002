import socket
 
def get_ip_status(ip,port):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    server.connect((ip,port))
    print('{0} port {1} is open'.format(ip, port))
  except Exception:
    print('{0} port {1} is not open'.format(ip,port))
  finally:
    server.close()
 
if __name__ == '__main__':
  host = '192.168.0.1'
  for port in range(20,100):
    get_ip_status(host,port)