#start the client side using command - python practical2_concat_client.py
import Pyro4

def main():
    with open("server_uri.txt", "r") as f:
        uri = f.read()
    
    server = Pyro4.Proxy(uri)  # Connect to the remote server
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = server.concatenate_strings(str1, str2)
    print("Concatenated Result:", result)

if __name__ == "__main__":
    main()
