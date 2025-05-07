import Pyro4

def main():
    string_concat = Pyro4.Proxy("PYRONAME:example.concat")  # Look up the remote object
    
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    
    result = string_concat.concatenate(s1, s2)
    print("Concatenated result:", result)

if __name__ == "__main__":
    main()
