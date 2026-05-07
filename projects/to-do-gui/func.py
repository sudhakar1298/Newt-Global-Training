fp="todo.txt"
def get_todo(fp=fp):
    with open(fp,'r') as f:
        t=f.readlines()
    return t 

def write_todo(a,fp=fp):
    with open(fp,'w') as f:
        f.writelines(a)

if __name__=="__main__":
    print(get_todo)