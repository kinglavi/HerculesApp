from django.contrib.auth.models import *
from HerculesApi.models import *
from datetime import timedelta
import datetime

# admin user -
u = Customer(username='kinglavi')
u.is_superuser = True
u.set_password("kinglavi")
u.save()

# lavi company mangers group
g = Group(name='lavi_company_managers')
g.save()

# manager of lavi company -
c = Customer(username="lavi_company_manager")
c.set_password("lavi_company_manager")
c.save()

c.groups = []
c.groups.add(g)

# laviCompany -
company = Company(name='laviCompany', description='This is lavi company.', managers=g)
company.save()

# Create laviStore in laviCompany and group of managers of the store(workers).
c = Customer(username="lavi_store_worker")
c.set_password("lavi_store_worker")
c.save()
g = Group(name='lavi_store_workers')
g.save()
c.groups = []
c.groups.add(g)
s = Store(name="laviStore", company=company, address='Lavi Street, Kinglavi country',
          phone_number="0501234352")
s.save()
s.managers.add(g)


camp = Campaign(name="LaviCampaign", store=s, goal=10, description="The best campaign ever.", gift_discount=100,
                end_date=datetime.datetime.now() + timedelta(days=50))
camp.save()

p = Product(name='lavi_product', description='This is Lavi product.', price=50,store=s)
p.save()

camp.products.add(p)

stick = Sticker(token='lavigever', is_used=False, product=p)
stick.save()

cust = Customer(username='kinglavi_customer')
cust.set_password("Password1")
cust.save()
# TODO: remove the add card line.
card = Card(campaign=camp, owner=cust)
card.save()
cust = Customer(username='adam')
cust.set_password("adam")
cust.save()
