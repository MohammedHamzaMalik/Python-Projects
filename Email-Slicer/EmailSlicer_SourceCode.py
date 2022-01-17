# So this first we are going to do is to ask the user to enter the email to be sliced
email = input("Enter Your Email: ").strip()

# Here we are slicing the user input to obtain the username and domain and ignore the rest.
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

# And now finally, let's print our output.
print(f"Your username is {username} & domain is {domain}")