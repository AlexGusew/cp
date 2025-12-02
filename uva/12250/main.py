import sys

for line in sys.stdin:
    print(line, 123)

for i, line in enumerate(sys.stdin.readlines()):
    if line == "#\n":
        continue
    val = {
        "HELLO\n": "ENGLISH",
        "HOLA\n": "SPANISH",
        "HALLO\n": "GERMAN",
        "BONJOUR\n": "FRENCH",
        "CIAO\n": "ITALIAN",
        "ZDRAVSTVUJTE\n": "RUSSIAN",
    }.get(line, "UNKNOWN")
    print(f"Case {i + 1}: {val}")
