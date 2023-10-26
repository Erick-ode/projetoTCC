from waitress import serve
from main import main

if __name__ == "__main__":
    serve(main, host="127.0.0.1", port=5000)
