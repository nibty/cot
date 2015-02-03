# ui_shared.py - Unit test cases for generic UI class
#
# January 2015, Glenn F. Matthews
# Copyright (c) 2015 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

import logging
import unittest

from verboselogs import VerboseLogger

logging.setLoggerClass(VerboseLogger)

from COT.ui_shared import UI


class TestUI(unittest.TestCase):
    """Test cases for abstract UI class"""

    def test_apis_without_force(self):
        ins = UI()

        self.assertTrue(ins.confirm("prompt"))
        ins.confirm_or_die("prompt")

        ins.default_confirm_response = False
        self.assertFalse(ins.confirm("prompt"))
        self.assertRaises(SystemExit, ins.confirm_or_die, "prompt")

        self.assertEqual("hello", ins.get_input("Prompt:", "hello"))
        self.assertEqual("passwd", ins.get_password("user", "host"))

    def test_apis_with_force(self):
        ins = UI(force=True)

        self.assertTrue(ins.confirm("prompt"))
        ins.confirm_or_die("prompt")

        ins.default_confirm_response = False
        # With --force, the default_confirm_response doesn't apply
        self.assertTrue(ins.confirm("prompt"))
        ins.confirm_or_die("prompt")

        self.assertEqual("hello", ins.get_input("Prompt:", "hello"))
        self.assertEqual("passwd", ins.get_password("user", "host"))
