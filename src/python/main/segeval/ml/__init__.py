'''
Computes a variety of traditional machine learning metrics.

.. moduleauthor:: Chris Fournier <chris.m.fournier@gmail.com>
'''
#===============================================================================
# Copyright (c) 2011-2012, Chris Fournier
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
#       
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#===============================================================================
from decimal import Decimal


def load_tests(loader, tests, pattern):
    '''
    A ``load_tests()`` function utilizing the default loader
    :func:`segeval.Utils.default_load_tests`.
    
    .. seealso:: The `load_tests protocol <http://docs.python.org/library/\
    unittest.html#load-tests-protocol>`_.
    '''
    #pylint: disable=W0613
    from ..Utils import default_load_tests
    return default_load_tests(__file__, loader, tests)


def precision(tp, fp):
    '''
    Calculate precision.
    
    :param tp: Number of true positives
    :param fp: Number of false positives
    
    Returns:
    Precision as a Decimal.
    '''
    # pylint: disable=C0103
    if tp == 0 and fp == 0:
        return Decimal(0)
    else:
        return Decimal(tp) / Decimal(tp + fp)
    
    
def recall(tp, fn):
    '''
    Calculate recall.
    
    Arguments:
    :param tp: Number of true positives
    :param fn: Number of false negatives
    
    Returns:
    Recall as a Decimal.
    '''
    # pylint: disable=C0103
    if tp == 0 and fn == 0:
        return Decimal(0)
    else:
        return Decimal(tp) / Decimal(tp + fn)


def fmeasure(tp, fp, fn, beta=1.0):
    '''
    Calculate F-measure, also known as F-score.
    
    .. math::
        \\text{F}_{\\beta}\\text{-measure} = \\frac{(1 + \\beta^2) \\cdot TP}{(1 + \\beta^2) \\cdot TP + \\beta^2 \\cdot FN + FP}
    
    :param tp: Number of true positives.
    :type tp: int
    :param fp: Number of false positives.
    :type fp: int
    :param fn: Number of false negatives.
    :type fn: int
    :param beta: Scales how precision and recall are averaged.
    :type beta: double
    
    :returns: F-measure.
    :rtype: :class:`decimal.Decimal`
    '''
    # pylint: disable=C0103
    if tp == 0 and fp == 0 and fn == 0:
        return Decimal('0')
    else:
        # Convert to Decimal
        tp   = Decimal(tp)
        fp   = Decimal(fp)
        fn   = Decimal(fn)
        beta = Decimal(str(beta))
        # Calculate terms
        beta2   = beta ** 2
        beta2_1 = Decimal('1.0') + beta2
        numerator   = beta2_1 * tp
        denomenator = (beta2_1 * tp) + (beta2 * fn) + fp
        # Perform division
        return numerator / denomenator


def confusionmatrix(tp, fp, fn, tn=None):
    '''
    Creates 2D tuples representing a confusion matrix.
    
    Arguments:
    tp   -- Number of true positives
    fp   -- Number of false positives
    fn   -- Number of false negatives
    tn   -- Number of true negatives
    
    Returns:
    2D tuples containing a confusion matrix.
    '''
    # pylint: disable=C0103
    tp = Decimal(tp)
    fp = Decimal(fp)
    fn = Decimal(fn)
    return ( (tp, fp), (fn, tn) )


def cf_tostring(tp, fp, fn, tn=None):
    '''
    Creates a string representation of a confusion matrix.
    
    Arguments:
    tp   -- Number of true positives
    fp   -- Number of false positives
    fn   -- Number of false negatives
    tn   -- Number of true negatives
    
    Returns:
    String representation of a confusion matrix.
    '''
    # pylint: disable=C0103
    return '[%(tp)i \t %(fp)i\n %(fn)i \t %(tn)i]' % \
        {'tp': tp, 'fp' : fp, 'fn' : fn, 'tn' : tn}


def prfcf(tp, fp, fn, tn=None, beta=1.0):
    '''
    Calculates precision, recall, F-Score, and creates a confusion matrix.
    
    Arguments:
    tp   -- Number of true positives
    fp   -- Number of false positives
    fn   -- Number of false negatives
    tn   -- Number of true negatives
    beta -- Scales how precision and recall are averaged
    
    Returns:
    Precision, recall, F-Score, and a confusion matrix.
    '''
    # pylint: disable=C0103
    return precision(tp, fp), recall(tp, fn), fmeasure(tp, fp, fn, beta), \
           confusionmatrix(tp, fp, fn, tn)

