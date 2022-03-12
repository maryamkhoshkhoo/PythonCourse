translator_list=[]

def load():
    my_file = open('Translate.txt', 'r')
    word_list = my_file.read().split('\n')
    my_file.close() 
    for i in range(len(word_list)):
        dic={}
        if i%2==0:
            dic['english']=word_list[i]
            dic['persian']=word_list[i+1]
            translator_list.append(dic)
    

def show_menu():
    print("----Menu----")
    print("1.Add new word")
    print("2.Translation english to persian")
    print("3.Translation persian to english")
    print("4.Show list")
    print("5.Exit")

def english_to_persian():
    scan=input('please inter english sentence: ')
    sentence_list=scan.split('.')
    for i in sentence_list:
        words_list=i.split(' ')
        for j in words_list:
            for k in range(len(translator_list)):
                if translator_list[k]['english']==j:
                    print(translator_list[k]['persian'],end=' ')
                    break
                elif k==len(translator_list)-1:
                    print('not found!!',end=' ')
    print()

def persian_to_english():
    scan=input('please inter persian sentence: ')
    sentence_list=scan.split('.')
    for i in sentence_list:
        words_list=i.split(' ')
    for j in words_list:
        for k in range(len(translator_list)):
            if translator_list[k]['persian']==j:
                print(translator_list[k]['english'],end=' ')
                break
            elif k==len(translator_list)-1:
                print('not found!!',end=' ')
    print()

def add_new_word():
        my_file = open('Translate.txt', 'a')
        english = input('english:')
        persian = input('persian:')
        my_file.write('\n%s\n%s' %(english, persian))
        my_file.close()
        translator_list.append({'english':english, 'persian':persian})

def show_list():
    for i in range(len(translator_list)):
        print(translator_list[i])

load()
print('Welcome to translator')
while True:
    show_menu()
    choice=int(input('please select a number:'))
    if choice==1:
        add_new_word()
        print('done')
    elif choice==2:
        english_to_persian()
    elif choice==3:
        persian_to_english()
    elif choice==4:
        show_list() 
    elif choice==5:
        exit()