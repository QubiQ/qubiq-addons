# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date, datetime
from dateutil import relativedelta
import json

from openerp import tools, _
from openerp.osv import fields, osv
from openerp.tools.float_utils import float_repr


class crm_case_section(osv.osv):
    _inherit = "crm.case.section"

    '''
        Gets the values for each year using the read_group function
        from openerp/models.py

        :param obj: the target model (i.e. crm_lead)
        :param domain: the domain applied to the read_group
        :param list read_fields: the list of fields to read in the read_group
        :param str value_field: the field used to compute
                                the value of the bar slice
        :param str groupby_field: the fields used to group

        :return list section_result: a list of dicts:
                                [{
                                    'value': (int) bar_column_value,
                                    'tootip': (str) bar_column_tooltip,
                                }]
    '''
    def _get_annual_bar_values(
            self, cr, uid, obj, domain,
            read_fields, value_field, groupby_field, context=None):

        year_begin = date.today().replace(day=1, month=1)
        section_result = [{
            'value': 0,
            'tooltip': tools.ustr((
                year_begin + relativedelta.relativedelta(
                    years=-i)).strftime('year %Y')),
            } for i in range(self._period_number - 1, -1, -1)]

        group_obj = obj.read_group(
            cr, uid, domain, read_fields, groupby_field, context=context)
        groupby_field_split = groupby_field.split(':')[0]
        pattern = tools.DEFAULT_SERVER_DATE_FORMAT if obj.fields_get(
            cr, uid, groupby_field)[groupby_field_split][
            'type'] == 'date' else tools.DEFAULT_SERVER_DATETIME_FORMAT

        for group in group_obj:
            group_begin_date = datetime.strptime(
                group['__domain'][0][2], pattern)
            year_delta = relativedelta.relativedelta(
                year_begin, group_begin_date)
            section_result[
                self._period_number - (year_delta.years + 1)] = {
                    'value': group.get(value_field, 0),
                    'tooltip': group.get(groupby_field, 0)}

        return section_result

    '''
        Function to get the total invoiced during the last 5 years
        Gets the values using the function above _get_annual_bar_values
    '''
    def _get_invoices_annual_data(
            self, cr, uid, ids, field_name, arg, context=None):

        obj = self.pool['account.invoice.report']
        year_begin = date.today().replace(day=1, month=1)
        date_begin = (year_begin - relativedelta.relativedelta(
            years=self._period_number - 1)).strftime(
            tools.DEFAULT_SERVER_DATE_FORMAT)
        date_end = date(date.today().year, 12, 31).strftime(
            tools.DEFAULT_SERVER_DATE_FORMAT)

        res = {}
        for id in ids:
            created_domain = [
                ('type', 'in', ['out_invoice', 'out_refund']),
                ('section_id', '=', id),
                ('state', 'not in', ['draft', 'cancel']),
                ('date', '>=', date_begin),
                ('date', '<=', date_end)]

            # Groupby field date:year to group over the years
            values = self._get_annual_bar_values(
                cr, uid, obj, created_domain,
                ['price_total', 'date'], 'price_total', 'date:year',
                context=context)

            for value in values:
                value['value'] = float_repr(
                    value.get('value', 0), precision_digits=self.pool[
                        'decimal.precision'].precision_get(cr, uid, 'Account'))

            res[id] = json.dumps(values)
        return res

    _columns = {
        'forecast_period': fields.selection([
                ('monthly', _('Monthly')),
                ('annual', _('Annual')),
            ], string='Forecast period'),
        'annual_invoiced': fields.function(
            _get_invoices_annual_data,
            type='char', readonly=True,
            string='Rate of sent invoices per duration'),
    }

    _default = {
        'forecast_period': 'monthly',
    }
