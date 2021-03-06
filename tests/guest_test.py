import unittest
from classes.guest import Guest
from classes.caraoke import Caraoke

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ned Flanders", 200)
        self.guest2 = Guest("Marge Simpson", 100)
        self.guest3 = Guest("Selma Bouvier", 400)
        self.guest4 = Guest("Comic Book guy", 100)
        self.guest5 = Guest("Snake", 600)
        
    def test_guest_has_name(self):
        self.assertEqual =("Ned Flanders",self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual =(100, self.guest4.wallet)

    def test_guest_can_pay_entry_fee(self):
        self.assertEqual(True, self.guest3.can_guest_pay_entry_fee())
        
    
