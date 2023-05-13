from seasons import check_bdate

def test_seasons():
  assert check_bdate('1987-01-28') == ('1987', '01', '28')
  assert check_bdate('17777-01-28') == None
  assert check_bdate('January 28, 87') == None


