import blank

def test_say_hello():
    try:
        blank.main.say_hello()
        assert True
    except:
        assert False    