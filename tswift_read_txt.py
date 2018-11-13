# count = 0
# with open("all_tswift_lyrics.txt") as tswift:
#     for line in tswift:
#         words = line.split()
#         for x in words:
#             if(x == "love"):
#                 count = count+1
#
# print("The word love appeared: ")
# print(count)

from collections import Counter
with open("all_tswift_lyrics.txt") as tswift:
    for line in tswift:
        words = line.split()
        for x in words:
            print(x)
            x = Counter(words)
