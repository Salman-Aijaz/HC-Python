def split_and_join(line):
    # write your code here
    wordSplit=line.split(" ")
    wordJoin= "-".join(wordSplit)
    return wordJoin

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)