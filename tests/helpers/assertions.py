from .utils import list_to_set


def assert_lists_equal(list_actual, list_expect):
    set_actual = list_to_set(list_actual)
    set_expect = list_to_set(list_expect)

    diff_1 = set_actual - set_expect
    diff_2 = set_expect - set_actual

    msg = ""
    if len(diff_1) != 0:
        msg = f"{msg}This items {diff_1} from actual data was not be found in expected data\n"
    if len(diff_2) != 0:
        msg = f"{msg}This items {diff_2} from expected data was not be found in actual data\n"

    if len(msg) > 0:
        raise AssertionError(msg)
