from emzed.r import RInterpreter
from emzed.utils import toTable


def test_native_types():

    ip = RInterpreter()
    assert ip.execute("x <-3").x == 3
    assert ip.execute("x <-1.0").x == 1.0
    assert ip.execute("x <-'abc'").x == 'abc'

    ip.y = 42
    assert ip.execute("x <- y").x == 42

    ip.y = 1.0
    assert ip.execute("x <- y").x == 1.0

    ip.y = "abc"
    assert ip.execute("x <- y").x == "abc"


def test_tables():
    ip = RInterpreter()
    t = toTable("a", [1, 2])

    # transfer Table tor R:
    ip.t = t

    # fetch Table from R
    assert ip.execute("s <- t").s.rows == t.rows

    # fetch pandas.DataFrame from R
    df = ip.get_raw("s")
    assert df.as_matrix().tolist() == [[1], [2]]
