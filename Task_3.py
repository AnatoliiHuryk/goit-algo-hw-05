import timeit

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == p_hash and text[i:i + m] == pattern:
            return i
    return -1

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    skip = {}
    for k in range(m):
        skip[pattern[k]] = m - k - 1
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j == -1:
            return i
        i += skip.get(text[i + m - 1], m)
    return -1

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." * 1000
pattern = "consectetur"

print("Час виконання алгоритмів для пошуку підрядка:")
print("Рабін-Карп:", timeit.timeit(lambda: rabin_karp(text, pattern), number=100))
print("Кнут-Морріс-Пратт:", timeit.timeit(lambda: kmp_search(text, pattern), number=100))
print("Боєр-Мур:", timeit.timeit(lambda: boyer_moore(text, pattern), number=100))
