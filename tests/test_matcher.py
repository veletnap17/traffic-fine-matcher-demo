import unittest
import pandas as pd
from src.matcher import match_fines_to_orders

class MatcherTests(unittest.TestCase):
    def setUp(self):
        self.fines = pd.DataFrame([{'spz':'9AB1234','offense_datetime':pd.Timestamp('2025-09-23 15:44'), 'amount':500,'offense_type':'parking','file':'synthetic.pdf'}])
        self.rentals = pd.DataFrame([
            {'spz':'9AB1234','rentstartdatetime':pd.Timestamp('2025-09-23 10:00'),'enddatetime':pd.Timestamp('2025-09-23 11:00'),'first_name':'Jan','last_name':'Novak','email':'jan@example.com'},
            {'spz':'9AB1234','rentstartdatetime':pd.Timestamp('2025-09-23 12:00'),'enddatetime':pd.Timestamp('2025-09-23 14:30'),'first_name':'Petr','last_name':'Svoboda','email':'petr@example.com'},
        ])
    def test_latest_preceding_rental(self):
        matched, unmatched = match_fines_to_orders(self.fines, self.rentals)
        self.assertEqual(len(matched),1)
        self.assertTrue(unmatched.empty)
        self.assertEqual(matched.iloc[0]['email'], 'petr@example.com')
    def test_no_prior_rental(self):
        fines = self.fines.copy()
        fines.loc[0,'offense_datetime']=pd.Timestamp('2025-09-23 09:00')
        matched,unmatched=match_fines_to_orders(fines,self.rentals)
        self.assertTrue(matched.empty)
        self.assertEqual(len(unmatched),1)
    def test_different_vehicle(self):
        fine=self.fines.copy()
        fine.loc[0,'spz']='OTHER'
        matched,unmatched=match_fines_to_orders(fine,self.rentals)
        self.assertTrue(matched.empty)
        self.assertEqual(len(unmatched),1)

if __name__=='__main__':
    unittest.main()
