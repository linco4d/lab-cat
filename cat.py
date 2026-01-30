'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    # Read and write the file in chunks to achieve O(1) memory complexity
    chunk_size = 1024 * 1024  # 1MB chunks
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
