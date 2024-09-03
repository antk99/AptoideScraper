import os
import subprocess
import sys

def run_server() -> None:
    print("Running the server...")
    os.chdir('src')
    subprocess.run(['uvicorn', 'app:app', '--reload'])

def run_tests() -> None:
    print("Running tests...")
    subprocess.run([sys.executable, '-m', 'pytest', 'tests'])

def run_mypy() -> None:
    print("Running mypy on src...")
    subprocess.run([sys.executable, '-m', 'mypy', 'src'])
    print("Running mypy on tests...")
    subprocess.run([sys.executable, '-m', 'mypy', 'tests'])

def run_all() -> None:
    run_mypy()
    run_tests()
    run_server()

def main(command) -> None:
    if command == 'server':
        run_server()
    elif command == 'test':
        run_tests()
    elif command == 'mypy':
        run_mypy()
    elif command == 'all':
        run_all()
    else:
        print("Usage: python run.py [server|test|mypy|all]")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run.py [server|test|mypy|all]")
    else:
        main(sys.argv[1])
