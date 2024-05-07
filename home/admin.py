from django.contrib import admin
from .models import menus,hmenus,CustomUser,Reservation,tables,TimeSlot,Employee,BillingInformation,Payment,AddToCart,LeaveApplication,TableBooking,Review,Stock,Notification,CateringMenu,Catering,PaymentCatering
# Register your models here.
admin.site.register(menus)
admin.site.register(hmenus)
admin.site.register(CustomUser)
admin.site.register(Reservation)
admin.site.register(tables)
admin.site.register(TimeSlot)
admin.site.register(Employee)
admin.site.register(BillingInformation)
admin.site.register(AddToCart)
admin.site.register(Payment)
admin.site.register(LeaveApplication)
admin.site.register(TableBooking)
admin.site.register(Review)
admin.site.register(Stock)
admin.site.register(Notification)
admin.site.register(CateringMenu)
admin.site.register(Catering)
admin.site.register(PaymentCatering)

class menusAdmin(admin.ModelAdmin):
    list_display=('name','desc','price')
    
