sentence = input()
split_sentence = sentence.split(" ")
answer = len(split_sentence)
if split_sentence[0] == "":
    answer-=1
if split_sentence[-1] == "":
    answer-=1
print(answer)