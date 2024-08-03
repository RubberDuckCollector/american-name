def main():
    american_dict = {
        " ": " ",
        "a": "freedom",
        "b": "spray cheese",
        "c": "smith",
        "d": "guns",
        "e": "bill",
        "f": "hudson",
        "g": "cultural appropriation",
        "h": "beer",
        "i": "war",
        "j": "corn",
        "k": "football",
        "l": "burger",
        "m": "ayden",
        "n": "shooting",
        "o": "military",
        "p": "mcdonald's",
        "q": "walmart",
        "r": "johnson",
        "s": "fried chicken",
        "t": "nationalism",
        "u": "racism",
        "v": "leigh",
        "w": "thanksgiving",
        "x": "nascar",
        "y": "ie",
        "z": "capitalism",
    }

    name = input("Enter your name: ")
    new_name = ""
    for i in range(len(name.lower())):
        new_name += american_dict[name[i]]

    print(new_name)


if __name__ == "__main__":
    main()
