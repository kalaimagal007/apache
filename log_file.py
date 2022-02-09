import re 
x=0
def parser(f):
    f=open("C:/Users/Kalaimagal_K/.vscode/log_file/txt.log")
    log=f.read()
    
    ID=re.findall("\d{2}.\d{3}.\d{1}.\d{3}",log)
    Date=re.findall("\d{2}/[a-zA-z]{3}/\d{4}",log)
    Time=re.findall("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]",log)
    Method=re.findall("GET...*\sHTTP\/[0-9.]+\"",log)
    url=re.findall("(http?://\S+)",log)
    regex=ID+Date+Time+Method+url
    x=tuple(regex)
    print(x)
    
if __name__ == '__main__':
    parser('log')
    