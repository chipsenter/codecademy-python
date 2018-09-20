"""Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.

You may get a string containing special characters (for example, !, @, or #)."""


def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

print reverse("johan")  