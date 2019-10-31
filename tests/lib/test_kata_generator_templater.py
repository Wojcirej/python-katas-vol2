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
        "transforms underscored kata name into sentence"
        templater = KataGeneratorTemplater(input)
        assert(templater.humanize_kata_name()) == result
        
    @parameterized.expand(
        [
            ("underscored_kata_name", "UnderscoredKataName"),
            ("kata", "Kata"),
            ("kata_name", "KataName")
        ]
    )
    def test_camelize_kata_name_for_class_name_result(self, input, result):
        "transforms underscored kata name into Pascal case"
        templater = KataGeneratorTemplater(input)
        assert(templater.camelize_kata_name_for_class_name()) == result
    
    @parameterized.expand(
        [
            (["param1"], "param1"),
            (["kata", "kata2"], "kata, kata2"),
            (["arg1", "arg2", "arg3"], "arg1, arg2, arg3")
        ]
    )
    def test_format_params_for_method_call(self, params, result):
        "transforms array of params into comma separated string"
        templater = KataGeneratorTemplater("random", params)
        assert(templater.format_params_for_method_call()) == result
        
    @parameterized.expand(
        [
            (["param1"], "param1, result"),
            (["kata", "kata2"], "kata, kata2, result"),
            (["arg1", "arg2", "arg3"], "arg1, arg2, arg3, result")
        ]
    )
    def test_format_params_for_tuple_example(self, params, result):
        "concatenates array of params with 'result' for tuple example"
        templater = KataGeneratorTemplater("random", params)
        assert(templater.format_params_for_tuple_example()) == result
    
    @parameterized.expand(
        [
            (["param1"], "self, param1, result"),
            (["kata", "kata2"], "self, kata, kata2, result"),
            (["arg1", "arg2", "arg3"], "self, arg1, arg2, arg3, result")
        ]
    )
    def test_format_params_for_testing_method(self, params, result):
        "concatenates array of params with 'self' and 'result' for testing method call"
        templater = KataGeneratorTemplater("random", params)
        assert(templater.format_params_for_testing_method()) == result