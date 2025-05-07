import Pyro4

@Pyro4.expose
class StringConcatenator:
    def concatenate(self, s1, s2):
        return s1 + s2

def main():
    daemon = Pyro4.Daemon()                          # Start the Pyro daemon
    ns = Pyro4.locateNS()                            # Locate the name server
    uri = daemon.register(StringConcatenator)        # Register the object
    ns.register("example.concat", uri)               # Register the object with a name
    print("Server is ready.")
    daemon.requestLoop()                             # Start the event loop

if __name__ == "__main__":
    main()

#python -m Pyro4.naming
#python RMIServer.py
#python RMIClient.py
