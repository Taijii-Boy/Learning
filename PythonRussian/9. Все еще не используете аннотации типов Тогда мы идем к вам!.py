from typing import List, Union, Optional

# из библиотеки typing:
# Union[int, float] - Либо то либо то
# Optional[int, float] - None, либо int, либо float
# Any - любой

def calc(a: Union[int, float], b:int) -> Union[int, float]:
    return a + b

# def to_int(a_list) -> list:
#     return [int(e) for e in a_list]

# 
def to_int(a_list: list[str]) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(to_int(['1', '2']))
    print(to_int(['1', '2'])[0].upper())
    print(calc(1, 2))
