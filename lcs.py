def longest_common_subsequence(s1, s2):
    if not s1:
        return 0, []
    if not s2:
        return 0, []

    if s1 == s2:
        return len(s1), list(s1)

    if s1[0] == s2[0]:
        length, seq = longest_common_subsequence(s1[1:], s2[1:])
        return length + 1, [s1[0]] + seq
    else:
        length1, seq1 = longest_common_subsequence(s1[1:], s2)
        length2, seq2 = longest_common_subsequence(s1, s2[1:])
        if length1 > length2:
            return length1, seq1
        else:
            return length2, seq2

if __name__ == '__main__':
    s1 = "abcdaf"
    s2 = "bcdaf"
    print(longest_common_subsequence(s1, s2))