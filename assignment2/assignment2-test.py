import assignment2

def test_everything():
    # Test read_employees and column functions
    employees = assignment2.read_employees()
    assert "fields" in employees
    assert "rows" in employees
    assert assignment2.column_index("first_name") >= 0

    # Test first_name
    first = assignment2.first_name(0)
    assert isinstance(first, str)

    # Test employee_find
    found = assignment2.employee_find(1)
    assert isinstance(found, list)

    # Test employee_find_2
    found2 = assignment2.employee_find_2(1)
    assert isinstance(found2, list)

    # Test sorting (just make sure it runs)
    sorted_rows = assignment2.sort_by_last_name()
    assert isinstance(sorted_rows, list)

    # Test employee_dict
    emp = assignment2.employee_dict(employees["rows"][0])
    assert isinstance(emp, dict)

    # Test all_employees_dict
    all_emps = assignment2.all_employees_dict()
    assert isinstance(all_emps, dict)

    # Test get environment variable
    value = assignment2.get_this_value()
    print("THISVALUE:", value)

    # Test secret
    assignment2.set_that_secret("something")
    assert assignment2.custom_module.secret == "something"

    # Test minutes files
    m1, m2 = assignment2.read_minutes()
    assert "rows" in m1 and "fields" in m1
    assert "rows" in m2 and "fields" in m2

    # Test minutes_set creation
    mset = assignment2.create_minutes_set()
    assert isinstance(mset, set)

    # Test minutes_list
    mlist = assignment2.create_minutes_list()
    assert isinstance(mlist, list)

    # Test writing to file
    sorted_minutes = assignment2.write_sorted_list()
    assert isinstance(sorted_minutes, list)

    print("All tests passed!")

if __name__ == "__main__":
    test_everything()
