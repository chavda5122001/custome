import datetime

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def test_cron_job(self):
        date = datetime.datetime.now()
        today_date = datetime.datetime(int(date.strftime("%G")), int(date.strftime("%m")), int(date.strftime("%d")))
        print("________today_date", today_date)
        search_id = self.env['sale.order'].search([('create_date', '>=', today_date)])
        print("_____", search_id)
        print("____", (today_date))
        if not search_id:
            templete_id = self.env.ref('auto_sent_missing_entery.mail_template_opd_details').id
            templete = self.env['mail.template'].browse(templete_id)
            templete.send_mail(self.id, force_send=True)
            print('sent successful')
        else:
            print("not send email")
