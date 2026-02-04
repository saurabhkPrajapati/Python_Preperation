l = [12, 35, 9, 56, 24]
a = []
a.append(l[-1])
a.extend(sorted(l[1:-1]))
a.append(l[0])
a
########
first = l.pop(0)
last = l.pop(-1)
l.insert(0, last)
# l.append(first)
# l.insert(-1, first)  # this and below insert behave differently
l.insert(len(l)-1, first)
l

########
l[0], l[-1] = l[-1], l[0]
l
########
a, *b, c = l
l = [c, *sorted(b), a]

