email = input("Email Address: ").strip()  #strip to remove any whitespace
index = email.index('@')

username = email[:index] #slicing to separate username
domain = email[index+1:] 

print("\nEmail address: ", email)
print("Username: ", username)
print("Domain name: ", domain)
