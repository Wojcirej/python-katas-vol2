import unittest
from parameterized import parameterized

from katas.not_very_secure.not_very_secure import not_very_secure

class NotVerySecure(unittest.TestCase):

    @parameterized.expand(
        [
            ("Mazinkaiser", True),
            ("helloworld_", False),
            ("PassW0rd", True),
            ("", False),
            ("\n\t\n", False),
            ("ciao\n$$_", False),
            ("__*__", False),
            ("&)))(((", False),
            ("43534h56jmTHHF3k", True),
            ("V_c2k", False),
            ("v3BmBt6uFJJZzCPS7N_FPSmeKVHq7", False),
            ("j7yXHfMZuFYfiLIazP9Qes5CX", True),
            ("53TOjjfz15JpX_0eUXB", False),
            ("2a72Rs7u", True),
            ("JO8 k01", False),
            ("49e28a", True),
            ("dybxRD7jtc49mZ1", True),
            ("y2xGD", True),
            ("8jrSaWRQ8", True),
            ("e7tOevpd!49V", False),
            ("q", True),
            ("GvJzYcerD!j8yJcz", False),
            ("w34QPQNTq1s8SWpvqT7rc", True),
            ("_S3S0OKKjojtaDtRpcvacYyGb7uBY", False),
            ("rPF7uVGZ", True),
            ("Qb_WZjkvG5KpcGPDFr", False),
            ("SeCnT6Y 5HQC7urcPYvXFC531tYS4", False),
            ("exfnm5JO53u!h3qX5nHysenfunD", False),
            ("XgKfq8XSKQleZCggIr", True),
            ("_5pgbNOA3", False),
            ("w8!s", False),
            ("yTDdnzHxRvyNidugkYIhDW", True),
            ("2PFzgV d7d3iF8eM8Whc", False),
            ("xUxCmQZj", True),
            ("TQ", True),
            ("BLhy1CIf8c", True),
            ("APiIHRa0", True),
            ("SX", True),
            ("3FRzNN_sK7UCXljB", False),
            ("yU!sSxHYVJwlBfrfU6RPXFrymLdZy", False),
            ("JS jth6I4v4AiqbXyXWo tMl4kUP", False),
            ("f8kzX", True),
            ("PbVV1Hrv", True),
            ("KhcOP0UKFqG6C_IQTIhxOkiW9WBR", False),
            ("3VOFW", True),
            ("nPNvvUozr", True),
            ("aCG0k!", False),
            ("xDQG8zvmh_kvhxrJ0S0HiwaHZys", False),
            ("vzgryXuLtvsO9_2SaCjH7HzXb8D", False)
        ]
    )
    def test_not_very_secure(self, string, result):
        ""
        assert(not_very_secure(string)) == result