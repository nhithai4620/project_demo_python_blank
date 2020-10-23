# -*- coding: utf-8 -*-
import blank


def test_blank_package():
    my_str = "minhng.info"
    rev_str = blank.reverse(my_str)
    assert rev_str == "ofni.gnhnim"