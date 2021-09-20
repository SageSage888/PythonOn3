import subprocess


def start():
    program = 'c:\\Users\\ezstrdm\\Documents\\goit\\useful\\useful\\scan.py'
    arg = input('enter tour path ')
    subprocess.call(['python.exe', program, arg])


if __name__ == '__main__':
    start()
