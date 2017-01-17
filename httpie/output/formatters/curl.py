from __future__ import absolute_import

import json

from httpie.compat import urlencode


def as_curl(args):
    # Base command
    cmd = ['curl']

    # Enable verbose
    if args.verbose:
        cmd.append("-v")

    # Skip SSL cert verification
    if args.verify != 'yes':
        cmd.append("--insecure")

    # Add HTTP method
    if args.method != "GET":
        cmd.append("-X" + args.method)

    # Add headers
    for key in args.headers:
        value = args.headers[key].strip()

        cmd.append("-H '{}: {}'".format(key, value))

    # Add data
    if args.data:
        cmd.append("-d '{}'".format(json.dumps(args.data)))

    # Add URL with params
    url = args.url

    if args.params:
        url += "?{}".format(urlencode(args.params))

    cmd.append(url)

    # Return command
    return cmd
