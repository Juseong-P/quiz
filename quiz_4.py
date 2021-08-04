answer = "orange"
print("answer = "+answer)

try_times = 0
awn_list = []
for i in range(0,len(answer)):
    awn_list.append(answer[i])

present = ""

while try_times < 10:
    succeed = True

    letter = input("\n\nInput letter > ")
    for i in range(0, len(answer)):
        if letter == answer[i]:
            present += letter
    for w in answer:
        if w in  present:
            print(w, end = " ")
        else:
            print("_", end = " ")
            succeed = False

    try_times += 1

    if try_times <10 and succeed:
        print("\nsuccess")
        break
    elif try_times >= 10 and not succeed:
        print("\nGame over")