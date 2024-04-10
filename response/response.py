import validators

def main():
    email = input("What's your email address? ").strip()
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/response
