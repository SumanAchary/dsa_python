def print_prefix(input_str):
    for e in range(len(input_str)):
        for s in range(e + 1):
            print(input_str[s], end="")
        print()


if __name__ == "__main__":
    input_str = "suman_achary"
    print_prefix(input_str)
