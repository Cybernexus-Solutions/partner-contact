import unittest
from odoo.tests import TransactionCase, tagged, Form

from odoo.addons.base.tests.test_form_create import TestFormCreate

@unittest.skip
def test_create_res_users(self):
    pass

def test_create_res_partner(self):
    partner_form = Form(self.env['res.partner'])

    firstname = "Fïrst"
    lastname = "Läst"    
    # Changes firstname, which triggers compute
    partner_form.firstname = firstname

    # Changes lastname, which triggers compute
    partner_form.lastname = lastname

    # YTI: Clean that brol
    if hasattr(self.env['res.partner'], 'property_account_payable_id'):
        property_account_payable_id = self.env['account.account'].create({
            'name': 'Test Account',
            'user_type_id': self.env.ref('account.data_account_type_payable').id,
            'code': 'TestAccountPayable',
            'reconcile': True
        })
        property_account_receivable_id = self.env['account.account'].create({
            'name': 'Test Account',
            'user_type_id': self.env.ref('account.data_account_type_receivable').id,
            'code': 'TestAccountReceivable',
            'reconcile': True
        })
        partner_form.property_account_payable_id = property_account_payable_id
        partner_form.property_account_receivable_id = property_account_receivable_id
    partner_form.save()

TestFormCreate.test_create_res_users = test_create_res_users
TestFormCreate.test_create_res_partner = test_create_res_partner