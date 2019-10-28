import unittest
from parameterized import parameterized

from lib.kata_generator_templater import KataGeneratorTemplater

class TestKataGeneratorTemplater(unittest.TestCase):

    @parameterized.expand(
        [
            ("underscored_kata_name", "Underscored kata name"),
            ("kata", "Kata"),
            ("kata_name", "Kata name")
        ]
    )
    def test_humanize_kata_name_result(self, input, result):
        templater = KataGeneratorTemplater(input)
        assert(templater.humanize_kata_name()) == result
    
    @parameterized.expand(
        [
            (["param1"], "param1"),
            (["kata", "kata2"], "kata, kata2"),
            (["arg1", "arg2", "arg3"], "arg1, arg2, arg3")
        ]
    )
    def test_format_params_for_method_call(self, params, result):
        templater = KataGeneratorTemplater("random", params)
        assert(templater.format_params_for_method_call()) == result
    
    @parameterized.expand(
        [
            (["param1"], "param1, result"),
            (["kata", "kata2"], "kata, kata2, result"),
            (["arg1", "arg2", "arg3"], "arg1, arg2, arg3, result")
        ]
    )
    def test_format_params_for_testing_method(self, params, result):
        templater = KataGeneratorTemplater("random", params)
        assert(templater.format_params_for_testing_method()) == result
    
    @parameterized.expand(
        [
            (["param1"], "param1,result"),
            (["kata", "kata2"], "kata,kata2,result"),
            (["arg1", "arg2", "arg3"], "arg1,arg2,arg3,result")
        ]
    )
    def test_format_param_names_for_parametrize(self, params, result):
        templater = KataGeneratorTemplater("random", params)
        assert(templater.format_param_names_for_parametrize()) == result