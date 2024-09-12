def main():
    chat_count = int(input())
    
    gomgom_set = set()  #곰곰이 이모티콘을 사용한 사람 이름
    gomgom_count = 0 #곰곰이 이모티콘 개수
    
    for i in range(chat_count):
        chat = input()
        if chat == "ENTER":
            gomgom_count += len(gomgom_set)
            gomgom_set.clear()
        else:
            gomgom_set.add(chat)
    
    gomgom_count += len(gomgom_set)
    print(gomgom_count)

main()