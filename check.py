from pathlib import Path

page = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

if "<h1>Hello, CI/CD!</h1>" in page:
    print("Yay!")
else:
    print("There is missing text.")
    raise SystemExit(1)

# Pretend secret for learning only. Never put a real password in this code.
secret_file = Path(__file__).with_name("secret.txt")

if secret_file.exists() and secret_file.read_text(encoding="utf-8").strip() == "plank":
    print("Secret flag: 1 (success)")
else:
    print("Secret flag: 0 (missing or incorrect)")
    raise SystemExit(1)
