def main():

    code = input("Enter code: ")

    for num in range(1, 14):

        new_word = ""

        for letter in code:
            value = ord(letter) + num

            if value > 90:
                value -= 26

            new_word += chr(value)

        print(new_word + " (+" + str(num) + ")")

    for num in range(1, 13):

        new_word = ""

        for letter in code:
            value = ord(letter) - num

            if value < 65:
                value += 26

            new_word += chr(value)

        print(new_word + " (-" + str(num) + ")")


if __name__ == "__main__":
    main()