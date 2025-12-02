for _ in range(int(input())):
    name, start, born, courses = input().split()
    start = int(start.split("/")[0])
    born = int(born.split("/")[0])
    courses = int(courses)

    if start >= 2010:
        print(f"{name} eligible")
    elif born >= 1991:
        print(f"{name} eligible")
    elif courses > 40:
        print(f"{name} ineligible")
    else:
        print(f"{name} coach petitions")
