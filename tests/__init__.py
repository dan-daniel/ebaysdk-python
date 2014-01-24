# -*- coding: utf-8 -*-

'''
© 2012-2013 eBay Software Foundation
Authored by: Tim Keefer
Licensed under CDDL 1.0
'''

import unittest
import doctest
import ebaysdk.utils
import ebaysdk.config
import ebaysdk.connection
import ebaysdk.finding
import ebaysdk.shopping
import ebaysdk.trading
import ebaysdk.merchandising
import ebaysdk.soa.finditem

def getTestSuite():
    suite = unittest.TestSuite()

    suite.addTest(doctest.DocTestSuite(ebaysdk.connection))
    suite.addTest(doctest.DocTestSuite(ebaysdk.config))
    suite.addTest(doctest.DocTestSuite(ebaysdk.utils))
    suite.addTest(doctest.DocTestSuite(ebaysdk.finding))
    suite.addTest(doctest.DocTestSuite(ebaysdk.shopping))
    suite.addTest(doctest.DocTestSuite(ebaysdk.trading))
    suite.addTest(doctest.DocTestSuite(ebaysdk.merchandising))
    suite.addTest(doctest.DocTestSuite(ebaysdk.soa.finditem))
    return suite

runner = unittest.TextTestRunner()
runner.run(getTestSuite())
