import random
from typing import List, Tuple

FUNCTIONAL_CHARACTERS: str = (
    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$"
    "%&\'()*+,-./;<=>@[\\]^_`{|}~ "
)

GEN_CHARSET: str = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ2034567890!@#$%^&*("
    ")-=_+{}[];\'\",.<>/| "
)


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

    for letter in message.strip():
        if letter == " ":
            return_message += ":"
        for (code_enc, code_letter) in key_file_contents:
            if code_letter == letter:
                return_message += code_enc.split("?")[random.randint(0, 7)]
        return_message += "?"

    return return_message[:-1]


def decode(key_path: str, message: str) -> str:
    key_file_contents: List[Tuple[str, str]] = read_key(key_path)
    return_message: str = ""
    for code in message.split("?"):
        if code == ":":
            return_message += " "
        for (code_enc, code_letter) in key_file_contents:
            if code in code_enc.split("?"):
                return_message += code_letter
    return return_message


def generate25() -> str:
    return ''.join(
        random.choice(GEN_CHARSET) for _ in range(random.randint(15, 25))
    )


def generate4():
    return ''.join(random.choice(GEN_CHARSET) for _ in range(3))


def make_key() -> str:
    generation_base: int = random.randint(1000, 9999)

    file_key: List[str] = [
        "xcrypt-key".center(160),
        (
                f"{generation_base}4kezuihg8i4wz"
                + '?'.join(generate25() for _ in range(7))
        )
    ]

    file_key.extend(
        (
                f"{character}{generate4()}{generate25()}?"
                + '?'.join(generate25() for _ in range(7))
        ) for character in FUNCTIONAL_CHARACTERS
    )

    file_key.append("xcrypt-key".center(160))

    with open(f"{generation_base}_xcrypt.key", "w+") as f:
        f.write('\n'.join(file_key))

    return f"{generation_base}_xcrypt.key"
