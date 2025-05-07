from xmlrpc.client import ServerProxy

# Create a proxy server
proxy = ServerProxy("http://localhost:4000/")

# Take input
num = int(input("Enter an integer: "))

# Call remote function
result = proxy.factorial(num)

# Show result
print("Factorial of", num, "is", result)
