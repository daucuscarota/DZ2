inFile = open('input.txt', 'r', encoding='utf8')
grades = [[] for i in range(12)]
for line in inFile:
    scName, fname, grade, score = line.strip().split()
    grade, score = int(grade), int(score)
    grades[grade].append(score)
for scores in grades:
    if len(scores) != 0:
        print(scores.count(max(scores)), end=' ')