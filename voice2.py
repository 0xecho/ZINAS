voicedata = {
                # "abra":["of that"],
                # "atfa":[],
                "qey":[],
                "semayawi":[],
                "arenguade":[],
                "and":[],
                "hulet":[],
                "sost":[],
                "arat":[],
                "amist":[],
                "sidist":[],
                "sebat":[],
                "simint":[],
                "zetegn":[],
                "zero":["zero"]
}
from os import listdir
from analyse_wav import analyse_from_file

for i in listdir("./training_data/wavs/"):
    try:
        for j in listdir("./training_data/wavs/"+i):
            # voicedata[i].append(j)
            print(i+" ")
            analyse_from_file("./training_data/wavs/"+i+"/"+j)
    except:
        continue
