import subprocess, tempfile


def updateFile(code):
    with open("./logic/code.bas", "w") as f:
        f.write(code)  

def runCode():

    cmd = ['python', './logic/compiler/output.py']
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

    print(result)
    return result.decode('utf-8')


if __name__ == '__main__':
    
    respuesta = runCode()
    print(respuesta)
        
        
