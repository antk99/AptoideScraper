import os
import subprocess
import sys

def run_server() -> None:
    print("Running the server...")
    subprocess.run([sys.executable, os.path.join('src', 'app.py')])

def run_tests() -> None:
    print("Running tests...")
    subprocess.run([sys.executable, '-m', 'pytest', 'tests'])

def run_mypy() -> None:
    print("Running mypy on src...")
    subprocess.run([sys.executable, '-m', 'mypy', 'src'])
    print("Running mypy on tests...")
    subprocess.run([sys.executable, '-m', 'mypy', 'tests'])

def main(command) -> None:
    if command == 'server':
        run_server()
    elif command == 'test':
        run_tests()
    elif command == 'mypy':
        run_mypy()
    else:
        print("Usage: python run.py [server|test|mypy|clean]")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run.py [server|test|mypy|clean]")
    else:
        main(sys.argv[1])
