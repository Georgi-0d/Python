# WinRAR Password Cracker

This Python script is designed to perform a brute-force attack on password-protected `.RAR` files. It uses the WinRAR command-line tool (`UnRAR.exe`) to test passwords and identify the correct one.

## Requirements

- Python 3.x
- WinRAR installed on your system
- `UnRAR.exe` available in the default WinRAR installation path (`C:\Program Files\WinRAR\UnRAR.exe`)

## How It Works

1. The script prompts the user to provide the following:
   - The name of the `.RAR` file.
   - The full path to the file on the system.
2. It then starts a brute-force attempt, incrementing the password from `1` upwards, using `UnRAR.exe` to test each password.
3. If the correct password is found, the script will print the file name and the correct password.
4. The process will continue until the correct password is found or interrupted.

## Usage

1. Clone or download the repository to your local machine.
2. Install Python 3.x if not already installed.
3. Make sure WinRAR is installed and `UnRAR.exe` is located in `C:\Program Files\WinRAR\UnRAR.exe` (or update the script with your custom path to `UnRAR.exe`).
4. Run the script:

```bash
python bruteforcer.py
