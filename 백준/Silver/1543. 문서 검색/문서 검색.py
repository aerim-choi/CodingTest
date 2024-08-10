def main():
    count = 0
    statement = input()
    word = input()
    start = 0
    end = len(word)

    while end <= len(statement) :
        if(statement[start:end] == word):
            count+=1
            start += len(word)
            end += len(word)
        else:
            start +=1
            end +=1
    return count


print(main())