import sys
import socket
from pathlib import Path
sys.path.append(Path(__file__).resolve().parents[1].as_posix())
from sample_app.bin.create_app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host=socket.gethostname(), port=8082, debug=True)
