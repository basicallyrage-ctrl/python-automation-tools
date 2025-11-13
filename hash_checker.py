import hashlib

def hash_file(filename):
    h = hashlib.sha256()
    try:
        with open(filename, "rb") as file:
            chunk = file.read(4096)
            while chunk:
                h.update(chunk)
                chunk = file.read(4096)
        return h.hexdigest()
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    file_name = input("Enter file name to hash: ")
    print("SHA-256:", hash_file(file_name))
