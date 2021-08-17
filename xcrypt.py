import random
from typing import List, Tuple


def read_key(key_path: str) -> List[Tuple[str, str]]:
    with open(key_path) as file:
        key_file = file.readlines()[1:-1]

    key_file_contents: List[Tuple[str, str]] = [
        (line[4:].replace("\n", ""), line[0]) for line in key_file
    ]

    key_file_contents.pop(0)
    return key_file_contents


def encode(key_path: str, message: str) -> str:
    key_file_contents: List[Tuple[str, str]] = read_key(key_path)
    return_message: str = ""

    if message[0] == " ":
        message = message[1:]
    if message[-1] == " ":
        message = message[:-1]

    for letter in message:
        if letter == " ":
            return_message += ":"

        for code in key_file_contents:
            if code[1] == letter:
                enc = code[0].split("?")

                return_message += enc[random.randint(0, 7)]
        return_message += "?"

    if return_message[-1] == "?":
        return_message = return_message[:-1]

    return return_message


def decode(key_path: str, message: str) -> str:
    key_file_contents: List[Tuple[str, str]] = read_key(key_path)

    return_message: str = ""
    message = message.split("?")

    for code in message:

        if code == ":":
            return_message += " "

        for item in key_file_contents:
            enc = item[0].split("?")
            if code in enc:
                return_message += item[1]

    return return_message


def generate25() -> str:
    return ''.join(
        random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ2034567890"
            "!@#$%^&*()-=_+{}[];\'\",.<>/| "
        ) for x in range(random.randint(15, 25))
    )


def generate4():
    return ''.join(
        random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ2034567890"
            "!@#$%^&*()-=_+{}[];\'\",.<>/| "
        ) for x in range(3)
    )


def make_key() -> str:
    generation_base: int = random.randint(1000, 9999)

    inu: int = 70
    file_key: List[str] = []

    functional_characters: str = (
        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$"
        "%&\'()*+,-./;<=>@[\\]^_`{|}~ "
    )

    file_key.append("-" * inu + "xcrypt-key" + "-" * inu)
    file_key.append(
        (
            str(generation_base) + "4kezuihg8i4wz" + generate25() + "?"
            + generate25() + "?" + generate25() + "?" + generate25()
            + generate25() + "?" + generate25() + "?" + generate25()
        )
    )

    for character in functional_characters:
        file_key.append(
            (
                character + generate4() + generate25() + "?" + generate25()
                + "?" + generate25() + "?" + generate25() + "?" + generate25()
                + "?" + generate25() + "?" + generate25() + "?" + generate25()
            )
        )

    file_key.append("-" * inu + "xcrypt-key" + "-" * inu)

    with open(str(generation_base) + "_xcrypt.key", "w+") as f:
        for line in file_key:
            f.write(line + "\n")

    return str(generation_base) + "_xcrypt.key"
