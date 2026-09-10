from slugify import slugify


def test_lowercases_and_joins_words():
    assert slugify("Hello World") == "hello-world"


def test_strips_punctuation():
    assert slugify("Hello, World!") == "hello-world"
