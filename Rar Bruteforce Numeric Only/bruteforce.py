import os
import subprocess


def bruteforcer():
    print("Winrar Password Cracker")
    password = 0

    while True:
        filename = input("File Name: ")
        if not filename:
            print("You can't leave this blank.")
            continue

        path = input("Enter Full Path (eg: C:\\Users\\Admin\\Desktop) : ")
        if not path:
            print("You can't leave this blank.")
            continue

        full_path = os.path.join(path, filename)
        if not os.path.exists(full_path):
            print("File couldn't be found. Make sure you include the (.RAR) extension at the end of the file's name.")
            continue

        break

    print("Breaking Password...")

    while True:
        password += 1
        result = subprocess.run(
            [r"C:\Program Files\WinRAR\UnRAR.exe", "t", f"-p{password}", full_path],
            capture_output=True
        )

        if result.returncode == 0:
            print(f"\nFile = {filename}")
            print(f"Password = {password}\n")
            break

    input("Press any key to exit.")


if __name__ == "__main__":
    bruteforcer()
