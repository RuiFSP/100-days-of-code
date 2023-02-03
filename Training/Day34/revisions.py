THEME_COLOR = "#375362"


# class revisions
# OOP Class Day 17 - 23

# Python Typing for input or outputs
# - age: int
# - name: str
# - height: float
# - is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print("You may pass") if police_check(12) else print("Pay a fine")


def greeting(name: str) -> str:
    return f"Hello + {name}"
