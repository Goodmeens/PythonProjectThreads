import multiprocessing
import threading, time
import random
from RandomWordGenerator import RandomWord
#Для RandomWordGenerator нужно в консоли прописать "pip install Random-Word-Generator"

def worker(wordsCount,num_thread):
    print(f'Старт потока №{num_thread}') 
    file_name =   f"{threading.get_ident()}.txt" 
    my_file = open(file_name, "w+")

    for i in range(wordsCount):
        my_file.write(rw.generate() + " ")

    my_file.close()
    print(f'Завершение генерации файла. поток №{num_thread}')

    maxLength = 0 #максимальная длина слова
    minLength = 10 #минимальная длина слова
    numsVowels = 0 #кол-во гласных
    numsConsons = 0 #кол-во согласных
    allCount = 0 #всего символов
    arrayLength = [0,0,0,0,0,0,0,0,0,0] #массив хранит кол-во слов каждой длины(1-10)

    with open(file_name, 'r') as f:
        wordLength = 0
        for row in f.read():
            allCount += 1

            if row in vowels:
                numsVowels += 1
            elif row != ' ':
                numsConsons += 1

            if row != ' ':
                wordLength += 1
            elif row == '' or row ==' ':
                if wordLength > maxLength:
                    maxLength=wordLength
                                 
                if wordLength < minLength:
                    minLength = wordLength

                arrayLength[wordLength-1] +=1
                wordLength = 0

            
        sredLength = arrayLength[0] + arrayLength[1]*2 + arrayLength[2]*3 + arrayLength[3]*4 + arrayLength[4]*5 + arrayLength[5]*6 + arrayLength[6]*7 + arrayLength[7]*8 + arrayLength[8]*9 + arrayLength[9]*10
        sredLength /= sum(arrayLength)

        return_string = f"""
        *******************************************************************************************\n
            Информация для файла: {file_name}\n
        *******************************************************************************************\n

            1.Всего символов: {allCount}\n
            2.Максимальная длина слова: {maxLength}\n
            3.Минимальная длина слова: {minLength}\n
            4.Средняя длина слова: {sredLength}\n
            5.Кол-во гласных: {numsVowels}\n
            6.Кол-во согласных: {numsConsons}\n
            7.Кол-во повторений слов с одинаковой длиной:\n
                * 1 сим. >> {arrayLength[0]}\n
                * 2 сим. >> {arrayLength[1]}\n
                * 3 сим. >> {arrayLength[2]}\n
                * 4 сим. >> {arrayLength[3]}\n
                * 5 сим. >> {arrayLength[4]}\n
                * 6 сим. >> {arrayLength[5]}\n
                * 7 сим. >> {arrayLength[6]}\n
                * 8 сим. >> {arrayLength[7]}\n
                * 9 сим. >> {arrayLength[8]}\n
                * 10 сим. >> {arrayLength[9]}\n
        """
        
        print(return_string)

vowels = set("aeiouyAEIOUY") #гласные буквы
rw = RandomWord(max_word_size=10,constant_word_size=False)

minWords = 100000 #поменять на 100к
maxWords = 500000 #поменять на 5кк - будет долго генерить файлы!!!!

countCores = multiprocessing.cpu_count()
for i in range(countCores):
    # создаем экземпляры 'Thread' с функцией
    # 'worker()', которая запустится в отдельных 
    # функции 'worker()' передаются в кортеже `args`
    thread = threading.Thread(target=worker, args=(random.randrange(minWords,maxWords),i))
    # запускаем экземпляр `thread`
    thread.start()

    