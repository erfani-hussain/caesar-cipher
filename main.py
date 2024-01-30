# Modules
from art import logo
from art import alphabet

# Define our caesar() function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # Make our program works for both: encode & decode
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # Do nothing with other characters such as: space, symbols and numbers
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Print the logo on the screen
print(logo)

# Put our function into a while loop
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Handle error if the shift amount was greater than length of English alphabet
  shift %= 26
  # Calling our caesar() function
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  # Restart our program
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if restart == "no":
    should_continue = False
    print("Goodbye")