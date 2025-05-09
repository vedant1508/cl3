#first run the server side code in the terminal with the command -
#  python practical1_factorial_server.py 
# then run the client side in the terminal with the command -
#  python practical1_factorial_client.py
import xmlrpc.client 

# Create an XML-RPC client 
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy: 
    try: 
        # Replace 5 with the desired integer value 
        input_value = int(input("Enter number: ")) 
        result = proxy.calculate_factorial(input_value) 
        print(f"Factorial of {input_value} is: {result}") 
    except Exception as e: 
        print(f"Error: {e}")
