import subprocess
import sys

def main():
    print('1 - Resumo')
    print('0 - Sair')
    option = int(input('? '))
    while option != 0:
        if option == 1:
            subprocess.run([sys.executable, 'scripts/summary.py'], check=True)
        option = int(input('? '))

if __name__ == '__main__':
    main()
