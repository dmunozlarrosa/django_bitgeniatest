from django.db import models

class Gene (models.Model):
    symbol = models.CharField(max_length=30, unique=True)
    start = models.IntegerField()
    end = models.IntegerField()
    chromosome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.symbol

# how to make a migration:
# 1 make the changes
# 1 apply change to database:            py manage.py migrate --run-syncdb
#                    or  :               py manage.py migrate

# 2 run check the changes with :         py manage.py check ejercicioConceptual
# 3 create migration for changes madeit: py manage.py makemigrations
# 4 execute migration :                  py manage.py sqlmigrate ejercicioConceptual 0004


# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.