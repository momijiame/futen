#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import cStringIO

import paramiko


def parse(lines):
    config = ''.join(lines)
    fd = cStringIO.StringIO(config)
    parser = paramiko.SSHConfig()
    parser.parse(fd)
    return parser


def get_entries(parser):
    return parser._config


def get_netloc(entry, parser):
        hostname = entry.get('host')[0]
        if hostname == '*':
            return
        port = parser.lookup(hostname).get('port')
        netloc = ':'.join([element for element in (hostname, port) if element])
        return netloc


def get_netlocs(lines):
    parser = parse(lines)
    entries = get_entries(parser)
    netlocs = []
    for entry in entries:
        netloc = get_netloc(entry, parser)
        if not netloc:
            continue
        netlocs.append(netloc)
    return netlocs


def execute(lines):
    netlocs = get_netlocs(lines)
    for netloc in netlocs:
        print(netloc)


def main():
    try:
        lines = sys.stdin.readlines()
        execute(lines)
    except BaseException as e:
        print('Error: %s' % e, file=sys.stderr)


if __name__ == '__main__':
    main()
