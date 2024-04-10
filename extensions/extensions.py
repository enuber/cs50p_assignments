def main():
    file = input('File name: ').strip().lower()
    checkFile(file)

def checkFile(name):
    if name.endswith('.gif'):
        print('image/gif')
    elif name.endswith('.jpg') or name.endswith('.jpeg'):
        print('image/jpeg')
    elif name.endswith('.png'):
        print('image/png')
    elif name.endswith('.pdf'):
        print('application/pdf')
    elif name.endswith('.txt'):
        print('text/plain')
    elif name.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')

main()

# check50 cs50/problems/2022/python/extensions
