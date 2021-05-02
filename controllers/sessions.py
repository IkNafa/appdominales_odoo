from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Session
from odoo.addons.appdominales_odoo.controllers.res_users import UserController

class AppdominalesSession(Session):

     @http.route('/api/session/authenticate', type='json', auth="none")
     def apiAuthenticate(self, db, login, password, token=None,base_location=None):
         user_auth_data = super(AppdominalesSession, self).authenticate(db, login, password, base_location)
         user = request.env['res.users'].search([('is_appdominales_user','=',True),('id','=',user_auth_data.get("uid"))], limit=1)
         if token:
            user.sudo().write({
                'firebase_token': token
            })
         return UserController().getUserData(user)