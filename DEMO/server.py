# echo-server.py
from pickle import loads, dumps
from login import *
from OpenSSL import SSL
import sys, os, select, socket

# Code for TLS communication
# Directory holding RSA cert
dir = os.path.dirname('\Users\suchm\cs_labs\441_project\DEMO\cert')

# Initializing context 
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.set_options(SSL.OP_NO_SSLv2)
ctx.set_verify(SSL.VERIFY_PEER|SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_cb) # Demand a certificate
ctx.use_privatekey_file (os.path.join(dir, 'server.pkey'))
ctx.use_certificate_file(os.path.join(dir, 'server.cert'))
ctx.load_verify_locations(os.path.join(dir, 'CA.cert'))
# this can be a hostname or IP address, empty string for all connections allowed

def verify_cb(conn, cert, errnum, depth, ok):
    if conn.cert.get_subject():
        return ok

HOST = socket.gethostname()
# number from 1-65536
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# create socket object AF_NET = IPv4 address SOCK_STREAM = TCP
print("Starting server")
with SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    # associate socket with specified network interface and port number
    s.bind((HOST, PORT))
    # listen for connections, this can have a value for num of unaccepted
    # connections allowed before refusing new connections
    print("Awaiting connections...\n")
    s.listen()
    # blocks execution, waits for incoming connection
    # this creates a new socket object representing the client
    conn, addr = s.accept()

    # Check if initialization sequence should be performed
    conn.send("init".encode())
    if str(conn.recv(1024).decode()) == 'done':
        run_setup(conn)
        # Trigger authentication sequence
        start_authentication(conn)
    else:
        # Trigger authentication sequence
        start_authentication(conn)
