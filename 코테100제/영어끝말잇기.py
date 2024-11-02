def solution(n, words):
    answer = []
    word_set = set()
    prev = words[0][-1]
    word_set.add(words[0])

    for i in range(1, len(words)):
        if words[i][0] != prev or words[i] in word_set:
            return [i%n + 1, i//n + 1]
        word_set.add(words[i])
        prev = words[i][-1]

    return [0, 0]