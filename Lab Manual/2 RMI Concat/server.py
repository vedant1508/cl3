#1. start Pyro nameserver using the command in the terminal - pyro4-ns 
#2. start server side using the command in the terminal - python practical2_concat_server.py
#3. start client side using the command in the terminal - python practical2_concat_client.py
import Pyro4

@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        result = str1 + str2
        return result

def main():
    daemon = Pyro4.Daemon()  # Create a Pyro daemon
    ns = Pyro4.locateNS()  # Locate the Pyro nameserver
    
    # Create an instance of the server class
    server = StringConcatenationServer()
    print("Server ready to accept requests...")
    # Register the server object with the Pyro nameserver
    uri = daemon.register(server)
    ns.register("string.concatenation", uri)
    
    print("Server URI:", uri)
    
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))
    
    daemon.requestLoop()

if __name__ == "__main__":
    main()
    
#after running the server code copy the server uri in a file named as server_uri.txt 
#save in same folder as the code
