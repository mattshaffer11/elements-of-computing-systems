from hack.parser import _is_valid_symbol


def test_is_valid_symbol():
    valid_symbols = [
        'a',
        'abc',
        'Abc',
        'd.',
        'a1',
        'a:',
        '$_a'
    ]
    invalid_symbols = [
        '1a',
        '!ewqe',
        '',
        '1',
        '?a',
        '<'
    ]

    for symbol in invalid_symbols:
        assert not _is_valid_symbol(symbol)
        
    for symbol in valid_symbols:
        assert _is_valid_symbol(symbol)
