# text = "@dance.rtee @punedancers @pune_dancers #dancer #dancersofindia #dancersofinstagram #dance #dancer #choreography #hiphop #urban #urbanchoreography #dancelover #dancechallenge #dancevideo #rap #danceofyou"
#
# import re
#
# # x = re.search("naam", text)
# # print(x.end())
# # print(x)
# # if x:
# #     print("true")
# # x = re.findall("\Aayush", text)
# # print(x)
#
# x = re.findall("#\w+\s", text)
# print(x)
# for i in x:
#     print("current hashtag",i)
#     text = re.sub(i, "", text)
#     print("text after deleting current hashtag",text)
# x = re.findall("#\w+", text)
# text = re.sub(x[0], "", text)
# print(text)



list = ["sfg", "sfvv", "svv", "svv", "svdv", "dvssb", "sd"]
result = sorted(list, key=list.count,  reverse=True)
print(result)
