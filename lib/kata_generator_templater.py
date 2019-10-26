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
        content = "import pytest\n\n"
        content += "from katas.{}.{} import {}\n\n".format(self.kata_name, self.kata_name, self.kata_name)
        content += "@pytest.mark.parametrize(\n    "
        return content
    
    def humanize_kata_name(self):
        return " ".join(self.kata_name.split("_")).capitalize()