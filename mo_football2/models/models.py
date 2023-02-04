from odoo import models, fields

    
class Club(models.Model):
    _name = 'club'
    _description = 'Club'
    
    name = fields.Char('Club name', required=True)
    nam_thanh_lap = fields.Date('Nam thanh lap',required=True)
    image = fields.Binary('Image', attachment=True)
    
    player_ids = fields.One2many('player','club_id',string='PLayer Club')
    

class Player(models.Model):
    _name = 'player'
    _description = 'Player'
    
    club_id = fields.Many2one('club',string='Player Club', ondelete='restrict')

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    date_of_birth = fields.Datetime(string='Date of birth')
    position = fields.Char('Position', groups='mo_football.group_player_manager')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
    
    