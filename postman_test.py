import http
import request

class ProductAPI(http.Controller):

    @http.route('/api/product/pricelist', type='json', auth='user', methods=['POST'])
    def get_default_pricelist(self, **kwargs):
        partner_id = kwargs.get('partner_id')
        if not partner_id:
            return {'error': 'partner_id manquant'}

        # Appel interne du modèle
        pricelist_id = request.env['sale.order'].get_default_pricelist(partner_id)
        return {'partner_id': partner_id, 'pricelist_id': pricelist_id}
