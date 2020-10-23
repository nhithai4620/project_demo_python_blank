# -*- coding: utf-8 -*-
import blank


def test_say_hello():
    try:
        blank.main.say_hello()
        assert True
    except Exception as e:
        print(e)
        assert False