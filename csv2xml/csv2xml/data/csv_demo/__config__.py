{ 'xml_files': [
    {'name': 'ir_sequence',
     'depends': ['base'],
     'csv': ['ir_sequence_type.csv','ir_sequence.csv']},
    {'name': 'ir_config',
     'depends': ['base'],
     'csv': ['ir_config_parameter.csv']},
    {'name': 'account_account_type',
     'depends': ['account'],
     'csv': ['account_account_type.csv']},
    {'name': 'account_account',
     'depends': ['account'],
     'csv': ['account_account.csv']},
    {'name': 'account_fiscalyear',
     'depends': ['account'],
     'csv': ['account_fiscalyear.csv', 'account_period.csv']},
    {'name': 'account_journal',
     'depends': ['account'],
     'csv': ['account_journal.csv']},
    {'name': 'account_tax',
     'depends': ['account'],
     'csv': ['account_tax.csv']},
    {'name': 'res_company',
     'depends': ['base'],
     'csv': ['res_company.csv']},
    {'name': 'account_analytic_group',
     'depends': ['analytic_plans_group','account_accountant'],
     'csv': ['account_analytic_group.csv']},
    {'name': 'account_analytic_account',
     'depends': ['account_accountant'],
     'csv': ['account_analytic_account.csv']},
    {'name': 'account_analytic_journal',
     'depends': ['account_accountant'],
     'csv': ['account_analytic_journal.csv',
             'account_journal.csv']},
    {'name': 'account_analytic_plan',
     'depends': ['account_accountant','account_analytic_plans'],
     'csv': ['account_analytic_plan.csv',
             'account_analytic_plan_instance.csv',
             'account_analytic_plan_instance_line.csv']},
    {'name': 'islr_wh_concept',
     'depends': ['l10n_ve_withholding_islr'],
     'csv': ['islr_wh_concept.csv']},
    {'name': 'payment_term',
     'depends': ['account'],
     'csv': ['payment_term.csv', 'account_payment_term_line.csv']},
    {'name': 'product_uom_categ',
     'depends': ['product'],
     'csv': ['product_uom_categ.csv']},
    {'name': 'product_uom',
     'depends': ['product'],
     'csv': ['product_uom.csv']},
    {'name': 'product_category',
     'depends': ['product'],
     'csv': ['product_category.csv']},
    {'name': 'product_product',
     'depends': ['product'],
     'csv': ['product_template.csv', 'product_product.csv']},
    {'name': 'product_pricelist',
     'depends': ['product'],
     'csv': ['product_pricelist.csv', 'product_pricelist_version.csv',
        'product_pricelist_item.csv']},
    {'name': 'res_country_state',
     'depends': ['base'],
     'csv': ['res_country_state.csv']},
    {'name': 'res_bank',
     'depends': ['base'],
     'csv': ['res_bank.csv']},
    {'name': 'res_currency',
     'depends': ['base'],
     'csv': ['res_currency.csv','res_currency_rate.csv']},
    {'name': 'res_partner',
     'depends': ['base'],
     'csv': ['res_partner.csv','res_partner_bank.csv']},
    {'name': 'res_groups',
     'depends': ['base'],
     'csv': ['res_groups.csv']},
    {'name': 'res_users',
     'depends': ['base'],
     'csv': ['res_users.csv']},
    {'name': 'hr',
     'depends': ['hr'],
     'csv': ['hr_employee_category.csv', 'hr_job.csv', 'hr_department.csv',
             'hr_employee.csv', 'hr_department_2.csv', 'hr_job_2.csv']},
    {'name': 'stock_location',
     'depends': ['stock'],
     'csv': ['stock_location.csv']},
    {'name': 'stock_warehouse',
     'depends': ['stock'],
     'csv': ['stock_warehouse.csv']},
    {'name': 'sale_shop',
     'depends': ['sale'],
     'csv': ['sale_shop.csv']},
    {'name': 'stock_warehouse_orderpoint',
     'depends':['stock'],
     'csv': ['stock_warehouse_orderpoint.csv']},
    {'name': 'ir_mail_server',
     'depends': ['base'],
     'csv': ['ir_mail_server.csv']},
    {'name': 'fetchmail_server',
     'depends': ['fetchmail'],
     'csv': ['fetchmail_server.csv']},
]}
