def debug(x):
    print(x)
    return x


def debug_convo(x):
    if nausia := x.nausia:
        print(f"YES, nausia is mentioned! Pydantic output == {nausia}")
    if pain := x.pain:
        print(f"YES, pain is mentioned! Pydantic output == {pain}")
    if anxiety := x.anxiety:
        print(f"YES, anxiety is mentioned! Pydantic output == {anxiety}")
    return x
