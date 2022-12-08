def main(var :int) -> int:
    if var > 10:
        return var * 10
    elif var == 2:
        return var
    else:
        return var * 2

if __name__ == "__main__":
    print(main(10))