from typing import Union, Tuple, Iterable


def handler1(name: str, coefficient: Union[float, str]) -> None:
    print(name)
    print(coefficient)


def handler2(name: str, coefficient: Tuple[Union[float, str], ...]) -> None:
    print(name)
    print(coefficient)


def handler3(name: str, coefficient: Iterable[Union[float, str]]) -> None:
    print(name)
    print(coefficient)


handler1("A_Draft string", 10)
handler1("A_Draft string", "10")
handler1("A_Draft string", 10.2)
# handler1("A_Draft string", [])
# handler("A_Draft string", {})
# handler("A_Draft string", ())


handler2("A_Draft string", (10,))
handler2("A_Draft string", ("10", 12))
handler2("A_Draft string", (10.2, 10))
handler2("A_Draft string", (10.2, 12.0))

handler3("A_Draft string", (10,))
handler3("A_Draft string", ("10", 12))
handler3("A_Draft string", [10.2, 10])
handler3("A_Draft string", {10.2, 12.0})
handler3("A_Draft string", "test")
