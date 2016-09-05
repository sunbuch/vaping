
import pytest
import vaping.plugins.fping

# 10.18.174.22    : xmt/rcv/%loss = 5/5/0%, min/avg/max = 118/120/122
# 10.6.6.2        : xmt/rcv/%loss = 5/0/100%

sumary_line = [
    ]

expect_verbose = {
    '10.130.133.1 : 273.89 298.10 322.58': {
        'host': '10.130.133.1',
        'min': 273.89,
        'max': 322.58,
        'avg': 298.19,
        'cnt': 3,
        'loss': 0.0,
        },
    '10.130.133.2 : 100 - 50': {
        'host': '10.130.133.2',
        'min': 50.0,
        'max': 100.0,
        'avg': 75.0,
        'cnt': 3,
        'loss': 0.333,
        },
    '10.130.133.2 : - - -': {
        'host': '10.130.133.2',
        'cnt': 3,
        'loss': 1,
        },
    'example.com: Temporary failure in name resolution': {
        }
    }


def test_parse_verbose():
    fping = vaping.plugins.fping.FPing({'interval': '5s'}, None)
    for line, expected in expect_verbose.items():
        res = fping.parse_verbose(line)
        for k,v in expected.items():
            if isinstance(v, float):
                assert abs(v - res[k]) < 0.001
            else:
                assert v == res[k]
