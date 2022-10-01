def two_characters(text):
        list_set = list(set(text))
        len_max = 0
        for i in range(len(list_set)):
            for j in range(i+1,len(list_set)):
                prev = '0'
                success = True
                cur_len = 0
                for e in text:
                    if e == list_set[i] or e == list_set[j]:
                        cur = e
                        if cur == prev:
                                success = False
                                break
                        else:
                            prev = cur
                            cur_len += 1
                if success and cur_len > len_max:
                    len_max = cur_len
        return len_max