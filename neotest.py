import sys
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def add_to_path():
    old_path = sys.path[:]
    sys.path.insert(0, str(Path(__file__).parent))
    try:
        yield
    finally:
        sys.path = old_path


with add_to_path():
    from django-neotest import main

if __name__ == "__main__":
    main(sys.argv[1:])
