from nltb.tools import text_cleaning

def test_text_cleaning():
  assert text_cleaning('9 am christophe')[0] == 'christophe'
