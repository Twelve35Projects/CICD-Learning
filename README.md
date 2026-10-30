# My first CI/CD example

## Step 1: A website and a check

Open `index.html` in your browser to see the website.

Run this in a terminal in this folder:

```powershell
python check.py
```

The check asks one question: does the file contain exactly `<h1>Hello, CI/CD!</h1>`?
It prints "Yay!" if it does. Otherwise it prints "There is missing text." and exits with code 1.
An exit code of 1 tells future automation to stop.

This is one small content check, not a full website or security test.

## What comes later

The checker also reads a local `secret.txt` file and checks for the pretend
value `plank`. It prints a flag of 1 for a match, or 0 for a missing or incorrect
value. A failure exits with code 1; successful scripts exit with code 0.
The printed flag and the process exit code are different things.

`secret.txt` is excluded by `.gitignore`. The checker and the ignore rules
are intended to go to GitHub; the local secret file is not. Ignore rules
do not remove files already tracked by Git or prevent explicit forced adds.
This is a toy comparison: the expected word is visible in the checker.
Never use a real password here or publish secret files with the website.
On GitHub, this ignored file will be absent, so this check will fail until
we deliberately configure a separate demonstration secret there.

With your approval, we will remove the heading, watch the check fail, and
restore it. Then we can put the example on GitHub and have GitHub Actions
run the same check whenever we push a change. Finally, we can add publishing
to GitHub Pages after a passing check.

For now, these are local files. Nothing is published and there are no
external dependencies, accounts, or credentials in this example.
