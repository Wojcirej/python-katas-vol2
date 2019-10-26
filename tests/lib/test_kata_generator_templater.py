import pytest

from lib.kata_generator_templater import KataGeneratorTemplater

@pytest.mark.parametrize(
    "input,result",
    [
        ("underscored_kata_name", "Underscored kata name"),
        ("kata", "Kata"),
        ("kata_name", "Kata name")
    ]
)
def test_humanize_kata_name_result(input, result):
    templater = KataGeneratorTemplater(input)  
    assert(templater.humanize_kata_name()) == result