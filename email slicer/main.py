def main():
    print("Slice your email into username, domain and extension ")
    print("")

    email_input = input("Enter your email address: ")

    (username, domain) = email_input.split("@")
    (domain,extension) = domain.split(".")


    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

main()



