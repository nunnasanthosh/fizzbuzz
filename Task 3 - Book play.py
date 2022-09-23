1. Function name: unique_words 

book1 = r"Book1.txt"

def unique_words(book1):
    uniq_list=[]
    unique_list = []
    book1 = open(book1,'r')
    lines = book1.readlines()
    for ch in lines:
        for i in ch.split(' '):
            i= i.replace('\n','')
            i= i.replace('/','')
            uniq_list.append(i)
    uniq_list = [ele for ele in uniq_list if ele.strip()]
    uniq_list = list(dict.fromkeys(uniq_list))
    book1.close()
    return uniq_list
    return uniq_list

2. Function name: count_the_article 

def count_the_article(book1):
    art_count = []
    book1 = open(book1,'r')
    lines= book1.readlines()
    for ch in lines:
        for i in ch.split(' '):
            art_count.append(i)
    book1.close()
    return len(art_count)


3. Function name: sorted_words

 
def sorted_words(book1):
    words_list = unique_words(book1)
    words_list.sort(key=len,reverse=True)
    return words_list


4. Function name: character_word_count 


def character_word_count(book1):
    words_list = unique_words(book1)
    word_dict  = {}
    for i in words_list:
        x= len(i)
        word_dict[i]=x
    return word_dict


5. Function name: starts_with_vow



def starts_with_vow(book1):
    vow = ('a','e','i','o','u')
    count = 0
    words_list = unique_words(book1)
    for i in words_list:
        print(i)
        if i[0].lower() in vow:
            count +=1
        else:
            continue
    return count
uniqueWords = unique_words(book1)
articleCount = count_the_article(book1)
sortedList = sorted_words(book1)
wordsCount = character_word_count(book1)
vowelsCount = starts_with_vow(book1)

print(unique_words)
print(articleCount)
print(sortedList)
print(wordsCount)
print(vowelsCount)



