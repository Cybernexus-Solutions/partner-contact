import unittest
from odoo.tests import TransactionCase, tagged, Form

from odoo.addons.base.tests.test_form_create import TestFormCreate
from odoo.addons.base.tests.test_res_users import TestUsers2

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

def test_reified_groups(self):
        """ The groups handler doesn't use the "real" view with pseudo-fields
        during installation, so it always works (because it uses the normal
        groups_id field).
        """
        # use the specific views which has the pseudo-fields
        f = Form(self.env['res.users'], view='base.view_users_form')

        firstname = "Fïrst"
        lastname = "Läst" 

        # Changes firstname, which triggers compute
        f.firstname = firstname

        # Changes lastname, which triggers compute
        f.lastname = lastname

        f.login = "bob"
        user = f.save()

        self.assertIn(self.env.ref('base.group_user'), user.groups_id)

TestFormCreate.test_create_res_users = test_create_res_users
TestFormCreate.test_create_res_partner = test_create_res_partner
TestUsers2.test_reified_groups = test_reified_groups