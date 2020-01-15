import sys

def main():
    try: filename = sys.argv[1]
    except IndexError: raise FileNotFoundError("Please give a markdown filename")
    with open(filename, 'r') as f:
        lines = f.readlines()
    toc = Builder()
    for l in lines:
        if l[0]=="#":
            toc += l
    print(toc)


class Builder:
    mark = ['-','+','*']
    def __init__(self):
        self.str = ""

    def __str__(self):
        return self.str.strip()

    def __add__(self, line):
        for i in range(3,0,-1):
            if line[:i]=="#"*i:
                self.add(line,i)
                break
        return self

    def add(self, line, ind):
        line = line[ind+1:]
        markdown_code = line.lower().strip().replace(" ","-").replace("`","-").replace(":","-")

        self.str += " "*2*(ind-1)
        self.str += Builder.mark[ind-1]
        self.str += " [{}](#{})\n".format(line.strip(), markdown_code)


if __name__=="__main__": main()
