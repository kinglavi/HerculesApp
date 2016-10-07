from django.contrib.auth.models import *
from HerculesApi.models import *
from datetime import timedelta
import datetime

u = User(username='kinglavi')
u.save()
g = Group(name='kinglavi_group')
g.save()
u.groups = []
u.groups.add(g)
c = Company(name='laviCompany', description='This is lavi company.', managers=g)
c.save()
s = Store(company=c, address='Lavi Street, Kinglavi country', phone_number="0501234352")
s.save()
camp = Campaign(store=s, goal=10, description="The best campaign ever.", gift_discount=100,
                end_date=datetime.datetime.now() + timedelta(days=50))
camp.save()
p = Product(name='lavi_product', description='This is Lavi product.', price=50, campaign=camp)
p.save()

stick = Sticker(token='lavigever', is_used=False, product=p)
stick.save()
cust = Customer(username='kinglavi_customer')
cust.set_password("Password1")
cust.save()
card = Card(campaign=camp, owner=cust)
card.save()
cust = Customer(username='adam')
cust.set_password("adam")
cust.save()
