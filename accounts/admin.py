# -*- encoding: utf-8 -*-

""" administrator related transactions """

from django.contrib import admin
from .models import User, referral_program


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'main_balance', 'referral_balance', 'is_active']



@admin.register(referral_program)
class Referral_ProgramAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'date']
    actions = ['mark_successful']

    def mark_successful(self, request, queryset):
        for referral_obj in queryset:
            referral_obj.status = referral_program.SUCCESSFUL
            referral_obj.user.referral_balance += referral_obj.award_bonus
            referral_obj.referrals.investment_balance += referral_obj.award_bonus
            referral_obj.user.save()
            referral_obj.save()

    mark_successful.short_description = "Mark selected referrals as successful"