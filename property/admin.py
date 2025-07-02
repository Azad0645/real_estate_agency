from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatOwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']
    extra = 1


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ["created_at"]
    list_display = ['address', 'town', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked']
    inlines = [FlatOwnersInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['complainant', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']