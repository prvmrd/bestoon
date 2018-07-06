from django.contrib import admin
from .models import Expense, Income, Pardakht, Token

# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Pardakht)
admin.site.register(Token)

