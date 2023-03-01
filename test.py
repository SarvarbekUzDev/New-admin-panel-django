import dotenv
import os 

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

print(os.environ["ADMIN"])  # outputs "value"
os.environ["ADMIN"] = "newvalue"
print(os.environ['ADMIN'])  # outputs 'newvalue'

# Write changes to .env file.
dotenv.set_key(dotenv_file, "ADMIN", os.environ["ADMIN"])


# def fnc(model):
# 	global _model
# 	_model = model

# 	class TestClass:
# 		class Meta:
# 			model = _model
# 			print( model )



# print(dir(fnc(2)))

# import requests

# resp = requests.get("https://buildmedia.readthedocs.org/media/pdf/kivymd/latest/kivymd.pdf")

# with open("kivymd.pdf", "w") as f:
# 	f.write(resp)


# qilinadigan ishlar
# Hamma ma'lumotlarni o'chirish
# qidiruv qismini tayyorlash

# 2) def delete_everything(self):
#     Reporter.objects.all().delete()

# def drop_table(self):
#     cursor = connection.cursor()
#     table_name = self.model._meta.db_table
#     sql = "DROP TABLE %s;" % (table_name, )
#     cursor.execute(sql)

# qgroup = reduce(operator.or_, (Q(**{fieldname: value}) for fieldname in fieldnames))
# asgns = Assignment.objects.filter(qgroup)

# # search


# from django.db.models import CharField
# from django.db.models import  Q

# fields = [f for f in table._meta.fields if isinstance(f, CharField)]
# queries = [Q(**{f.name: SEARCH_TERM}) for f in fields]

# qs = Q()
# for query in queries:
#     qs = qs | query

# table.objects.filter(qs)


# import json

# >>> from django.contrib.postgres.search import SearchVector
# >>> Entry.objects.annotate(
# ...     search=SearchVector('body_text', 'blog__tagline'),
# ... ).filter(search='Cheese')