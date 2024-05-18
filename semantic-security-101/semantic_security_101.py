#!/usr/bin/env python3

import socket
import base64

def main():
    # connect 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '195.134.67.7'
    port = 10090

    s.connect((host,port))
    s = s.makefile(mode="rw")

    # print welcome messages
    welcome1 = s.readline().strip()
    welcome2 = s.readline().strip()
    welcome3 = s.readline().strip()
    print(welcome1,"\n",welcome2,"\n",welcome3,"\n")

    for i in range(10):
        # t0 will be used twice, while the other two just once
        t0 = 'A' * 16
        t1 = 'B' * 16
        t2 = 'C' * 16

        cmd = f"encrypt({t0},{t1})"
        print(cmd,file=s,flush=True)
    
        ct = s.readline().strip()
        
        # get just the ciphertext
        parts = ct.split(': ')
        
        if( i == 0):
            ct0 = parts[1].strip()
        else: # avoid the score part(just print it)
            print(parts[0].strip())
            ct0 = parts[2].strip()
        print("cipher:",ct0)

        # do the same but for message t0 and t2
        cmd = f"encrypt({t0},{t2})"
        print(cmd,file=s,flush=True)

        ct = s.readline().strip()

        parts = ct.split(': ')
        ct1 = parts[1].strip()
        print("cipher:",ct1)
    
        if ct0 == ct1:  # if they are the same it means that the message t0 was encrypted
            solve_cmd = f"solve(0)"
        else:
            solve_cmd = f"solve(1)"

        print("solve_cmd",solve_cmd)
        print(solve_cmd, file=s, flush=True)

    # read the flag           
    flag = s.readline().strip()
    print(flag)
    s.close()

if __name__ == "__main__":
    main()
