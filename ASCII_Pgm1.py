# Function to find ASCII value using ord()
def get_ascii_value(char):
    
     return ord(char)

# Test the function
character = 'a'
print("ASCII value of", character, "is:", get_ascii_value(character))
# Using chr() function to get character from ASCII value
print(chr(65)) # Output: 'A'
print(chr(120)) # Output: 'x'
print((chr(ord('S') + 1)),(chr(ord( 'M')+1))) # Output: 'T'
