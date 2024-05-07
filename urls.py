"""
URL configuration for DineEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import userlogin,register,loggout,login_page

from home.views import index,menu,about,menumore,add_reservation,booking_confirm,predict_image,pred_menu,booking_list,orders_lists,cancel_booking,download_pdf,download_bill,cancel_order,review,add_review,catering_booking,catering_details,save_catering
from home.views import billing_payment,table_booking_payment,paymenthandler,cart,add_to_cart,view_cart,remove_from_cart,update_cart_item_quantity,checkout,display_cart_items,order_summary
from home.views import admin_login,admin_index,add_menu,user_list,ad_MenuList,menu_list,menu_edit,delete_menu_item,employee_count,empLeave_list,order_list,payment_counts,ad_booking_lists,stock_view,edit_stock,add_stock
from home.views import emp_index,emp_add,emp_profile,emp_list,emp_edit,products_by_category,filtered_menus,emp_registration,save_employee_details,employee_profile,delete_emp,change_pswrd,orderlist_emp,history_orders
from home.views import apply_leave,leave_list,approve_leave,emp_booking_lists,check_stock_and_create_notification,notification_detail,medical_leave,notify
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('',index,name=''),
    path('menu/',menu,name='menu'),
    path('check_stock_and_create_notification/', check_stock_and_create_notification, name='check_stock_and_create_notification'),
    path('notification/<int:notification_id>/', notification_detail, name='notification_detail'),
    path('about/',about, name='about'),
    # path('book/',book,name='book'),
    path('menumore/',menumore, name='menumore'),
    path('register/',register,name='register'),
    path('login/', login_page, name='login'),
    path('login-submit/', userlogin, name='login-submit'),
    
    path('loggout', loggout, name='loggout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("",include("allauth.urls")),
    path('home/',include('home.urls')),
    # path('add_table/', add_table, name='add_table'),
    path('add_reservation/', add_reservation, name='add_reservation'),
    path('booking_list/', booking_list, name='booking_list'),
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('booking_confirm/<int:booking_id>/',booking_confirm, name='booking_confirm'),
    # path('cancel_reservation/<str:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    # path('edit_reservation/<str:reservation_id>/', edit_reservation, name='edit_reservation'),
    # path('res_list/',res_list,name='res_list'),
    # path('previous_reservations/', previous_reservations, name='previous_reservations'),
    #  path('approve_reservation/<str:reservation_id>/', approve_reservation, name='approve_reservation'),
    # path('book_table/', book_table, name='book_table'),
    path('catering-booking/', catering_booking, name='catering_booking'),
    path('catering/<int:catering_id>/', catering_details, name='catering_details'),
    path('save_catering/', save_catering, name='save_catering'),
    path('cart/',cart, name='cart'),
    path('add_to_cart/<int:menu_id>/',add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart_item_quantity/<int:item_id>/<int:new_quantity>/', update_cart_item_quantity, name='update_cart_item_quantity'),
    path('view_cart/', view_cart, name='view_cart'),
    path('order_summary/<int:user_id>/',order_summary, name='order_summary'),
    path('checkout/',checkout,name='checkout'),
    path('display_cart_items',display_cart_items,name='display_cart_items'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('orders_lists/', orders_lists, name='orders_lists'),
    path('download_pdf/<int:billing_info_id>/', download_pdf, name='download_pdf'),
    path('download_bill/<int:booking_id>/', download_bill, name='download_bill'),
    path('review/<int:order_id>/', review, name='review'),
    path('add_review/', add_review, name='add_review'),

    # Billing Payment URLs
    path('billing/payment/<int:billing_id>/', billing_payment, name='billing_payment'),
    path('paymenthandler/<int:billing_id>/', paymenthandler, name='billing_paymenthandler'),

    # Table Booking Payment URLs
    path('booking/payment/<int:booking_id>/', table_booking_payment, name='table_booking_payment'),
    path('paymenthandler/<int:booking_id>/', paymenthandler, name='table_booking_paymenthandler'),


    path('admin_login/',admin_login,name='admin_login'),
    path('admin_index/',admin_index,name='admin_index'),
    # path('ad_MenuAdd/',ad_MenuAdd,name='ad_MenuAdd'),
    
    path('add_menu/', add_menu, name='add_menu'),
    path('ad_MenuList/',ad_MenuList,name='ad_MenuList'),
    path('stock/', stock_view, name='stock_view'),
    path('edit_stock/<int:menu_id>/', edit_stock, name='edit_stock'),
    path('add_stock/', add_stock, name='add_stock'),
   
    path('menu_list/', menu_list, name='menu_list'),
    path('user_list',user_list,name='user_list'),
    path('menu_edit/<int:menu_id>/', menu_edit, name='menu_edit'),
    path('delete_menu_item/<int:menu_id>/',delete_menu_item,name='delete_menu_item'),
    path('employee_count',employee_count,name='employee_count'),
    path('empLeave_list/', empLeave_list, name='empLeave_list'),
    path('order_list/',order_list,name='order_list'),
    path('payment_counts/',payment_counts,name='payment_counts'),
    path('ad_booking_lists/', ad_booking_lists, name='ad_booking_lists'),


    path('emp_registration',emp_registration,name='emp_registration'),
    path('emp_index/',emp_index, name='emp_index'),
    path('emp_add/',emp_add, name='emp_add'),
    path('emp_edit/<int:emp_id>/',emp_edit, name='emp_edit'),
    path('emp_list/',emp_list, name='emp_list'),
    path('delete_emp/<int:emp_id>/',delete_emp,name='delete_emp'),
    path('emp_profile/',emp_profile, name='emp_profile'),
    path('employee_profile/',employee_profile,name='employee_profile'),
    path('save_employee_details',save_employee_details,name='save_employee_details'),
    path('change_pswrd/',change_pswrd,name='change_pswrd'),
    path('apply_leave/', apply_leave, name='apply_leave'),
    path('leave_list/', leave_list, name='leave_list'),
    path('medical_leave/', medical_leave, name='medical_leave'),
    path('approve_leave/<int:leave_id>/', approve_leave, name='approve_leave'),
    path('orderlist_emp',orderlist_emp, name='orderlist_emp'),
    # path('notify/', notify, name='notify'),
    path('history_orders',history_orders,name='history_orders'),
    path('emp_booking_lists/', emp_booking_lists, name='emp_booking_lists'),

    path('products/<str:category_name>/', products_by_category, name='products_by_category'),
    path('filtered-menus/<str:category>/<str:submenu>/<str:sub_submenu>/', filtered_menus, name='filtered_menus'),

    path('upload/', predict_image, name='upload_image'),
    # path('result/', prediction_result, name='prediction_result'),
    path('pred_menu/',pred_menu,name='pred_menu')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

