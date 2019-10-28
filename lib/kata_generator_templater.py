class KataGeneratorTemplater:

    def __init__(self, kata_name, params = []):
        self.kata_name = kata_name
        self.params = params
        
    def readme_file_template_content(self):
        readme = (
            f"""# {self.humanize_kata_name()}\n\n"""
            f"""### Description\n"""
            f"""<!-- Add description of the kata here -->\n\n"""
            f"""### Examples\n"""
            f"""<!-- Add examples/test cases here -->\n\n"""
            f"""### Link to kata on codewars.com\n"""
            )
        return readme

    def kata_definition_file_content(self):
        params_string = ""
        if self.params:
            params_string = ", ".join(self.params)
        content = (
            f"""def {self.kata_name}({params_string}):\n"""
            f"""    #TODO insert definition of the function here..."""
            )
        return content
    
    def kata_test_definition_file_content(self):
        content = "import unittest\n"
        content += "from parameterized import parameterized\n\n"
        content += "from katas.{}.{} import {}\n\n".format(self.kata_name, self.kata_name, self.kata_name)
        content += "class {}(unittest.TestCase):\n\n".format(self.camelize_kata_name_for_class_name())
        content += "    @parameterized.expand(\n    "
        content += "    [\n        "
        content += "#TODO insert your test arguments here as tuples\n        ]\n"
        content += "    )\n"
        content += "    def test_{}({}):\n    ".format(self.kata_name, self.format_params_for_testing_method())
        content += "    assert({}({})) == result".format(self.kata_name, self.format_params_for_method_call())
        return content
    
    def humanize_kata_name(self):
        return " ".join(self.kata_name.split("_")).capitalize()
    
    def camelize_kata_name_for_class_name(self):
        return ''.join(x for x in self.kata_name.title() if not x == "_")
    
    def format_params_for_testing_method(self):
        params = "self, "
        params += self.format_params_for_method_call()
        params += ", result"
        return params
    
    def format_params_for_method_call(self):
        return ", ".join(self.params)