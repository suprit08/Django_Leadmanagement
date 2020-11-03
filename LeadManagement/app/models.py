from django.db import models

from LeadManagement import settings

medium_choices = (
    ('call', 'call'),
    ('whatsapp', 'whatsapp'),
    ('email', 'email')
)

day_choices = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31')
)

month_choices=(
('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
('11','11'),
    ('12','12')
)

year_choice = (
    ('20','20'),
)

# Create your models here.
class Lead(models.Model):
    lead_id = models.AutoField(primary_key=True)
    contact_person_name = models.CharField(max_length=100, default="Unavailable")
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100, default="Unavailable")
    source = models.CharField(max_length=100, default="Unavailable")
    current_stage = models.CharField(max_length=100, default="Unavailable")
    date_of_followup = models.DateField(auto_now=True)
    response = models.CharField(max_length=100)
    medium_used = models.CharField(max_length=8, choices=medium_choices)
