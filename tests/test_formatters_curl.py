from httpie.cli import parser
from httpie.output.formatters.curl import as_curl
from utils import TestEnvironment


class TestCurlFormatter:

    def test_get_request(self):
        args = ["http://example.com"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == ["curl", "http://example.com"]

    def test_post_request(self):
        args = ["POST", "http://example.com"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == ["curl", "-XPOST", "http://example.com"]

    def test_get_request_with_params(self):
        args = ["http://example.com", "a==42"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == ["curl", "http://example.com?a=42"]

    def test_get_request_with_headers(self):
        args = ["http://example.com", "Connection: keep-alive", "Content-Type: application/json"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == [
            "curl",
            "-H 'Connection: keep-alive'", "-H 'Content-Type: application/json'",
            "http://example.com"
        ]

    def test_post_request_with_json_data(self):
        args = ["POST", "http://example.com", "a=42"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == ["curl", "-XPOST", "-d '{\"a\": \"42\"}'", "http://example.com"]

    def test_verbose_flag(self):
        args = ["http://example.com", "-v"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == ["curl", "-v", "http://example.com"]

    def test_ssl_verify_flag(self):
        args = ["http://example.com", "--verify", "no"]
        parsed_args = parser.parse_args(args=args, env=TestEnvironment())
        cmd = as_curl(parsed_args)

        assert cmd == ["curl", "--insecure", "http://example.com"]
