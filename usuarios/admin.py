# from django.contrib import admin
# from .models import OpenAIAccount

# @admin.register(OpenAIAccount)
# class OpenAIAccountAdmin(admin.ModelAdmin):
#     list_display = ('organization', 'monthly_limit', 'remaining_balance', 'api_key_short')
#     readonly_fields = ('remaining_balance',)

#     def api_key_short(self, obj):
#         return f"{obj.api_key[:10]}..." if obj.api_key else ""
#     api_key_short.short_description = "API Key"

#     def remaining_balance(self, obj):
#         balance = obj.get_remaining_balance()
#         if isinstance(balance, float):
#             return f"${balance:.2f} USD"
#         return balance
#     remaining_balance.short_description = "Saldo Disponível"
