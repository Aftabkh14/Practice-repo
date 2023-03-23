from odoo import api, fields, models


class ApplePythonReport(models.AbstractModel):
    _name = "report.apple_iphone_company.apple_python_temp_report"

    def _get_report_values(self, docids, data=None):
        apple_ids = self.env['apple.iphone.company'].browse(docids)
        # print(apple_ids.c_name, apple_ids.c_address)


        reclist = []
        # reclist.append(apple_ids.c_name)
        for line in apple_ids.ipad_id:
            reclist.append({
                'ipad_models': line.ipad_models,
                'prices': line.prices,
                'accessories': line.accessories,

            })
            return {
                'apple_ids': reclist,
                # 'c_name': line.c_name,
            }