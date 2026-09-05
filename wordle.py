from random import choice


def choose_word():
    words = ["apple", "caped", "soupy", "dated", "sorts"]
    return choice(words)


def checkchoice(hashmap, result):

    val = input_value()
    input_val = list(val)

    hashmap1 = {}

    for i in range(5):
        if input_val[i] in hashmap1:
            hashmap1[input_val[i]] += 1
        else:
            hashmap1[input_val[i]] = 1

    arr1 = []

    for i in range(5):
        if input_val[i] == result[i]:
            arr1.append("green")
            hashmap[input_val[i]] -= 1
            
        elif hashmap.get(input_val[i], 0) > 0:
            arr1.append("yellow")
            hashmap[input_val[i]] -= 1

        else:
            arr1.append("grey")

    print("input val:", input_val)
    print(arr1)

    if input_val == result:
        print("correct guess")
    else:
        checkchoice(hashmap, result)


def input_value():
    val = input("Enter your 5 letter word: ")
    return val.lower()


def main():

    result = list(choose_word())
    hashmap = {}

    for i in range(5):

        if result[i] in hashmap:
            hashmap[result[i]] += 1
        else:
            hashmap[result[i]] = 1

    checkchoice(hashmap, result)


if __name__ == "__main__":
    main()