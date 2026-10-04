
print('Choose the language: eng or rus')
lang = input().lower()
if lang == 'rus':

    print('Вы хотите зашифровать или раcшифровать код?', 'Зашифровать - да, Раcшифровать - нет', sep = '\n')
    choice = input().lower()
    if choice == 'да':
        print('Желатет автоматически зашифровать код или вручную?', 'Автоматически - да, Вручную - нет', sep = '\n')
        autom_choice = input().lower()
        if autom_choice == 'нет':

            def create_ces_code_rus():
                alp_upp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                alp_low = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
                ces=''

                print('Это шифр цезаря, введите предложение', sep='\n')
                sentence = input()

                print('Введи шаг')
                shift = int(input())

                for i in sentence:
                    if i in alp_upp:
                        shift1 = (alp_upp.find(i) + shift) % 32
                        ces += alp_upp[shift1]
                    elif i in alp_low:
                        shift1 = (alp_low.find(i) + shift) % 32
                        ces += alp_low[shift1]
                    else:
                        ces += i

                k = 0
                for j in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower():
                    if j.lower() in ces:
                        k +=1

                if k ==0:
                    return None
                else:
                    return ces
        else:
            def rand_code_rus():
                alp_upp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                alp_low = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
                ces = ''
                word = ''
                list_len = []
                list_words = []
                print('Введите код')
                sentence = input()

                for i in sentence:
                    if i in alp_upp:
                        if i not in '''!?., -"{}'[]():;1234567890''':
                            word += i
                        else:
                            list_len.append(len(word))
                            list_words.append(word + i)

                            word = ''
                    else:
                        if i not in '''!?., -"{}'[]():;1234567890''':
                            word += i
                        else:
                            list_len.append(len(word))
                            list_words.append(word + i)

                            word = ''
                if word:
                    list_len.append(len(word))
                    list_words.append(word)

                for j in range(len(list_words)):

                    for f in list_words[j]:
                        if f in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower():
                            shift1 = (alp_low.find(f) + list_len[j]) % 32
                            ces += alp_low[shift1]
                        elif f in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                            shift1 = (alp_upp.find(f) + list_len[j]) % 32
                            ces += alp_upp[shift1]
                        else:
                            ces += f

                return ces
    else:
        def create_ces_uncode_rus():
            alp_upp = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            alp_low = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
            ces = ''

            print('Это шифр цезаря, введите предложение', sep='\n')
            sentence = input()
            print('Вам известен шаг?', 'да или нет', sep='\n')

            if input().lower() == 'да':
                print('Введите шаг')
                shift = int(input())

                for i in sentence:
                    if i in alp_upp:
                        shift1 = (alp_upp.find(i) - shift) % 32
                        ces += alp_upp[shift1]
                    elif i in alp_low:
                        shift1 = (alp_low.find(i) - shift) % 32
                        ces += alp_low[shift1]
                    else:
                        ces += i

                k = 0
                for j in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower():
                    if j.lower() in ces:
                        k += 1

                if k == 0:
                    return None
                else:
                    return ces

            else:

                for j in range(32):
                    ces=''
                    for i in sentence:
                        if i in alp_upp:
                            shift1 = (alp_upp.find(i) - j) % 32
                            ces += alp_upp[shift1]
                        elif i in alp_low:
                            shift1 = (alp_low.find(i) - j) % 32
                            ces += alp_low[shift1]
                        else:
                            ces += i
                    print(f'Шаг: {j} Расшифровка: {ces}')


else:
    print('Do you want to code or ucode?', 'Write code or ucode', sep = '\n')
    choice = input().lower()
    if choice == 'code':
        print('Do you need auto code or not?', 'Send auto or none‑auto')
        autom_choice = input().lower()
        if autom_choice == 'none-auto':

            def create_ces_code_eng():
                alp_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                alp_low = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
                ces = ''
                print("This is Cesar Code", "You have to input your message", sep = '\n')
                sentence = input()
                print('Write the step')
                shift = int(input())

                for i in sentence:
                    if i in alp_upp:
                        shift1 = (alp_upp.find(i) + shift) % 26
                        ces += alp_upp[shift1]
                    elif i in alp_low:

                            shift1 = (alp_low.find(i) + shift) % 26
                            ces += alp_low[shift1]
                    else:
                        ces += i
                k = 0

                for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
                    if j.lower() in ces:
                        k += 1
                if k == 0:
                    return None
                else:
                    return ces
        else:
            def rand_code_eng():
                alp_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                alp_low = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
                ces = ''
                word = ''
                list_len = []
                list_words = []
                print('Write your code')
                sentence = input()

                for i in sentence:
                    if i in alp_upp:
                        if i not in '''!?., -"{}'[]():;1234567890''':
                            word += i
                        else:
                            list_len.append(len(word))
                            list_words.append(word + i)

                            word = ''
                    else:
                        if i not in '''!?., -"{}'[]():;1234567890''':
                            word += i
                        else:
                            list_len.append(len(word))
                            list_words.append(word + i)

                            word = ''
                if word:
                    list_len.append(len(word))
                    list_words.append(word)

                for j in range(len(list_words)):

                    for f in list_words[j]:
                        if f in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
                            shift1 = (alp_low.find(f) + list_len[j]) % 26
                            ces += alp_low[shift1]
                        elif f in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            shift1 = (alp_upp.find(f) + list_len[j]) % 26
                            ces += alp_upp[shift1]
                        else:
                            ces += f

                return ces
    else:
        def create_ces_uncode_eng():
            alp_upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            alp_low = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
            ces = ''

            print("This is Cesar Code", "You have to input your message", sep='\n')
            sentence = input()
            print('Do you know the step?', 'yes or no', sep = '\n')
            if input().lower() == 'yes':

                print('Write the step')
                shift = int(input())

                for i in sentence:
                    if i in alp_upp:
                        shift1 = (alp_upp.find(i) - shift) % 26
                        ces += alp_upp[shift1]
                    elif i in alp_low:
                        shift1 = (alp_low.find(i) - shift) % 26
                        ces += alp_low[shift1]
                    else:
                        ces += i

                k = 0
                for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
                    if j.lower() in ces:
                        k += 1

                if k == 0:
                    return None
                else:
                    return ces
            else:

                for j in range(26):
                    ces=''
                    for i in sentence:
                        if i in alp_upp:
                            shift1 = (alp_upp.find(i) - j) % 26
                            ces += alp_upp[shift1]
                        elif i in alp_low:
                            shift1 = (alp_low.find(i) - j) % 26
                            ces += alp_low[shift1]
                        else:
                            ces += i
                    print(f'The step: {j} Uncode: {ces}')

if lang == 'rus':
    if choice == 'да':
        if autom_choice == 'нет':
            result = create_ces_code_rus()
        else:
            result = rand_code_rus()
    else:
        result = create_ces_uncode_rus()

else:
    if choice == 'code':
        if autom_choice == 'none-auto':
            result = create_ces_code_eng()
        else:
            result = rand_code_eng()
    else:
        result = create_ces_uncode_eng()


if result is not None:
    print(result)





