#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

import nose
from nose.tools.trivial import eq_

from futen.main import get_netlocs


class Test_Main(object):

    def test(self):
        testfile = path.join(path.dirname(__file__), 'data/ssh.config')
        expect = ['web:2200', 'app:2201', 'db:2202']
        with open(testfile) as fd:
            eq_(expect, get_netlocs(fd.readlines()))


if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
