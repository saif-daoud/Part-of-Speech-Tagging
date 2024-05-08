import os

def preprocess_txt_file(path, mode, save=False):
    file_path = os.path.join(path, "{}.txt".format(mode))
    with open(file_path, encoding="utf-8") as f:
        data = []
        phrase = []
        for line in f:
            line = line.strip()
            if len(line) < 2  or line == "\n":
                if phrase:
                    data.append(" ".join(phrase))
                    phrase = []
            else:
                splits = line.split(" ")
                phrase.append(splits[0])
        if phrase:
            data.append(" ".join(phrase))
    if save:
        text = "\n".join(data)
        output_path = os.path.join(path, "processed_{}.txt".format(mode))
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
    return data

def preprocess_test_file(mode, save=False):
    file_path = "submit.txt"
    with open(file_path, encoding="utf-8") as f:
        data = []
        phrase = []
        i = 0
        for line in f:
            line = line.strip().split(" ")
            if mode!="all":
                if line[1]!=mode:
                    continue
            if line[-1]=="True":
                if phrase:
                    data.append(" ".join(phrase))
                phrase = [line[0]]
            else:
                splits = line
                phrase.append(splits[0])
        if phrase:
            data.append(" ".join(phrase))
    if save:
        text = "\n".join(data)
        output_path = "processed_{}.txt".format(mode)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
    return data

if __name__ == '__main__':
    accent = "ibo"
    path = os.path.join("masakhane-pos-main", "data", accent)
    text = preprocess_txt_file(path, "train")
    print(text[0])