#!/usr/bin/env python

import argparse
import os

from fs.expose.mocks3 import serve_fs

parser = argparse.ArgumentParser(description='A Mock-S3 server.')
parser.add_argument('--hostname', dest='hostname', action='store',
                    default='localhost',
                    help='Hostname to listen on.')
parser.add_argument('--port', dest='port', action='store',
                    default=10001, type=int,
                    help='Port to run server on.')
parser.add_argument('--root', dest='root', action='store',
                    default='%s/s3store' % os.environ['HOME'],
                    help='Defaults to $HOME/s3store.')
parser.add_argument('--pull-from-aws', dest='pull_from_aws', action='store_true',
                    default=False,
                    help='Pull non-existent keys from aws.')
args = parser.parse_args()

from fs.osfs import OSFS
serve_fs(OSFS(args.root),args)
