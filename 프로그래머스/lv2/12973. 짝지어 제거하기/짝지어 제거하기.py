def solution(s):
    st_li = []
    for i, st in enumerate(s):
        st_li.append(st)

        if len(st_li) > 1 and st_li[-1] == st_li[-2]:
            st_li.pop()
            st_li.pop()

    if len(st_li) == 0:
        return 1

    else:
        return 0