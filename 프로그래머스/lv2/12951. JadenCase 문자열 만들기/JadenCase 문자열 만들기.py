def solution(s):
    n_s = [i for i in s]
    result = ''

    for i in range(len(n_s)):
        if n_s[i].isdigit():
            result += n_s[i]

        elif n_s[i] == ' ':
            result += n_s[i]

        elif n_s[i].isalpha():
            if len(n_s[0:i]) == 0:
                result += n_s[i].upper()

            elif n_s[i-1] == ' ':
                result += n_s[i].upper()

            else:
                result += n_s[i].lower()

    return result