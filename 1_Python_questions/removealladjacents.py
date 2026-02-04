def remove_ajacent_duplicates(s):
    for char in s:
        indices = []
        for cr in range(0, len(s)):
            if char == s[cr]:
                indices.append(cr)
        # for i in range(len(indices)):
        for _ in indices:
            if len(indices) > 1:
                if indices[-1] - indices[-2] != 1:
                    indices.pop()
        if len(indices) != 1:
            for _ in indices:
                s = s.replace(char, '', 1)
    return s


# print(remove_ajacent_duplicates('aaaabbaazcczmmaddadaeffa'))
# print(remove_ajacent_duplicates('aaaabbaaccmmaddadaeffa'))  # (aaaa)(bb)(aa)(cc)(mm)a(dd)adae(ff)a = aadaea'
print(remove_ajacent_duplicates('aaaabbaaccmmdddaeffa'))
# daef
