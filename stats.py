def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count (text):
    ans = {}
    for letter in text:
        if letter.lower() in ans:
            ans[letter.lower()]  += 1
        else:
             ans[letter.lower()] = 1
    
    return ans

def sort_on(dict):
    return dict["count"]

def sorting_dict(char_dict):
    ans = []

    for char , count in char_dict.items():
        char_info ={'char': char ,'count' : count}
        ans.append(char_info)

    ans.sort(reverse=True, key= sort_on)
    return ans 

