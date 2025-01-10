def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        sub_str = s[i:i + k]
        rem_dup = ""
        for char in sub_str:
            if char not in rem_dup:  # Check if the character is already in the result string
                rem_dup += char
        print(rem_dup)  # Print the processed substring

if __name__ == '__main__':
    string = "AAABCADDE"
    k = 3
    merge_the_tools(string, k)
