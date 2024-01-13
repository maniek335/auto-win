import pyuac


def main():
    print("Hello World!")

    input("Press Enter to continue...")


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()
