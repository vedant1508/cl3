from xmlrpc.server import SimpleXMLRPCServer

# Factorial code 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# Create a server 
server = SimpleXMLRPCServer(("localhost", 4000))

# Register a function 
server.register_function(factorial, "factorial")

print("Server started..........")
server.serve_forever()

# First run server.py

