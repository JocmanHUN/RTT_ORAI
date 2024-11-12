import sys

from pylint import lint

THRESHOLD = 10

run = lint.Run(["--rcfile=pylintrc", "main.py"], exit=False)

score = run.linter.stats.global_note

print(f"Score: {score}")

if score < THRESHOLD:
    print("Code quality is too low!")
    sys.exit(1)
else:
    sys.exit(0)
