from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, phone, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name,phone, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            phone=phone,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    CUSTOMER = 1
    EMPLOYEE = 2
    

    ROLE_CHOICE = (
        (CUSTOMER, 'CUSTOMER'),
        (EMPLOYEE, 'EMPLOYEE'),
    )

    username=None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=ROLE_CHOICE, blank=True, null=True,default='1')

    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    
    REQUIRED_FIELDS = ['name', 'phone']

    objects = UserManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def set_employee_role(self):
        self.role=CustomUser.EMPLOYEE
        self.save()

from django.db import models

class Employee(models.Model):
    position = models.CharField(max_length=100,editable=False,null=True,default='default')  # Field for the employee's position
    years_of_experience = models.PositiveIntegerField(null=True,default='default')  # Field for years of experience
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField(default='',null=True)  # Field for employee's address
    id_proof_number = models.CharField(max_length=100,default='',null=True)  # Field for employee's ID proof number
    education = models.CharField(max_length=100,default='',null=True)  # Field for employee's education
    qualification = models.CharField(max_length=100,default='',null=True)  # Field for employee's qualification
    emergency_name = models.CharField(max_length=100,default='',null=True)  # Field for emergency contact name
    emergency_contact_number = models.CharField(max_length=12,default='',blank=True, null=True)  # Field for emergency contact number
    image = models.ImageField(upload_to='employee_profile/', blank=True, null=True)
    active = models.BooleanField(default=True)
    
    # name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=100, unique=True)
    # phone = models.CharField(max_length=12, blank=True)
    # password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.user.username} - {self.position}"


class menus(models.Model):
    CATEGORY_CHOICES = (
        ('Kerala', 'Kerala'),
        ('Chineese', 'Chineese'),
        ('North Indian', 'North Indian'),
        ('Arabian', 'Arabian'),
        ('Beverages', 'Beverages'),
    )

    SUBMENU_CHOICES = (
        ('Breads', 'Breads'),
        ('Curries', 'Curries'),
        ('Rice Dishes','Rice Dishes'),
        ('Appetizers','Appetizers'),
        ('Main Course','Main Course'),
        ('Breads & Accompaniments', 'Breads & Accompaniments'),
        ('Rolls & Grills','Rolls & Grills'),
        ('Hot Beverage','Hot Beverage'),
        ('Cold Beverage','Cold Beverage'),
    )

    SUB_SUBMENU_CHOICES = (
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
        ('Water-based','Water-based'),
        ('Milk-based','Milk-based')
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='')
    submenu = models.CharField(max_length=50, choices=SUBMENU_CHOICES, default='', blank=True)
    sub_submenu = models.CharField(max_length=50, choices=SUB_SUBMENU_CHOICES, default='', blank=True)
    desc = models.CharField(max_length=300)
    price = models.FloatField()
    img = models.ImageField(upload_to='menus/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.db import models

class CateringMenu(models.Model):
    CATEGORY_CHOICES = [
        ('Veg Starter', 'Vegetarian Starter'),
        ('Non-Veg Starter', 'Non-Vegetarian Starter'),
        ('Veg-Main Course', 'Vegetarian Main Course'),
        ('Non-Veg Main Course', 'Non-Vegetarian Main Course'),
        ('Desert', 'Desert'),
        ('Drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name

from django.db import models

class Catering(models.Model):
    date = models.DateField()
    number_of_persons = models.IntegerField()
    menu_items = models.ManyToManyField(CateringMenu, related_name='catering')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


# from django.db import models

# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
#     menu = models.ForeignKey(menus, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return f"Cart for {self.user} - {self.menu.name}"


from django.db import models


class AddToCart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    menu = models.ForeignKey(menus, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username} - {self.menu.name} ({str(self.quantity)} items)"


class hmenus(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)
    price=models.FloatField()
    img = models.ImageField(upload_to='menus/', blank=True, null=True)

    def __str__(self):
        return self.name

# class Reservation(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#     reservation_date = models.DateField()
#     num_of_persons = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name
from django.db import models

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20, primary_key=True,default=None)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    num_of_persons = models.PositiveIntegerField()
    time_slot = models.CharField(max_length=20, null=True, blank=True)  # Add the time_slot field
    table_id = models.ForeignKey('home.tables', on_delete=models.CASCADE,null=True)  # Use string reference
    reservation_date = models.DateField()
    is_active = models.BooleanField(default=True)
    STATUS_CHOICES = [
    (None, 'None'),
    ('approved', 'Approved'),
    ('declined', 'Declined'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    menu_name = models.CharField(max_length=100, null=True, blank=True)
    menu_price = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.reservation_id


    
class tables(models.Model):
    tab_id = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.tab_id

from django.db import models

class TimeSlot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot_time = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.slot_time

    class Meta:
        verbose_name = "Time Slot"
        verbose_name_plural = "Time Slots"

# from django.db import models
# from django.contrib.auth.models import CustomUser
# from home import menus  # Import your Menu model

# class Fav(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     items = models.ManyToManyField(menus)  # Assuming Menu is the model for products

from django.db import models

class BillingInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    town = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    payment_status = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    menu = models.ManyToManyField(menus, blank=True)
    status = models.IntegerField(default=1)
    

    def __str__(self):
        if self.user:
            return f"Billing info for {self.user.name}"
        return "Billing info (No associated user)"

class TableBooking(models.Model):

    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings_by_name', null=True)
    phone = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings_by_phone', null=True)
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings_by_email', null=True)
     # Define choices for table_name
    TABLE_NAME_CHOICES = [
        ('Two-Top (1)', 'Two-Top (1)'),
        ('Two-Top (2)', 'Two-Top (2)'),
        ('Two-Top (3)', 'Two-Top (3)'),
        ('Four-Top (1)', 'Four-Top (1)'),
        ('Four-Top (2)', 'Four-Top (2)'),
        ('Four-Top (3)', 'Four-Top (3)'),
        ('Six-Top (1)', 'Six-Top (1)'),
        ('Six-Top (2)', 'Six-Top (2)'),
        ('Six-Top (3)', 'Six-Top (3)'),
        ('Eight-Top (1)', 'Eight-Top (1)'),
        ('Eight-Top (2)', 'Eight-Top (2)'),
        ('Eight-Top (3)', 'Eight-Top (3)'),
        ('Large Party (1)', 'Large Party (1)'),
        ('Large Party (2)', 'Large Party (2)'),
        ('Large Party (3)', 'Large Party (3)'),
    ]
    table_name = models.CharField(max_length=30, null=True, blank=True, choices=TABLE_NAME_CHOICES)
    
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    status = models.BooleanField(default=False)
    del_status = models.BooleanField(default=False)
    selected_items = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def _str_(self):
        return self.name
      
class Payment(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCESSFUL = 'successful', 'Successful'
        FAILED = 'failed', 'Failed'
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link the payment to a user
    razorpay_order_id = models.CharField(max_length=255)  # Razorpay order ID
    payment_id = models.CharField(max_length=255)  # Razorpay payment ID
    amount = models.DecimalField(max_digits=8, decimal_places=2)  # Amount paid
    currency = models.CharField(max_length=3)  # Currency code (e.g., "INR")
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the payment
    payment_status = models.CharField(max_length=20, choices=PaymentStatusChoices.choices, default=PaymentStatusChoices.PENDING)
    billing_info = models.ForeignKey(BillingInformation, on_delete=models.CASCADE, null=True, blank=True)
    table_booking = models.ForeignKey(TableBooking, on_delete=models.CASCADE, related_name='payments', null=True, blank=True)


    def str(self):
        return f"Order for {self.user.name}"

    class Meta:
        ordering = ['-timestamp']

class PaymentCatering(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SUCCESSFUL = 'successful', 'Successful'
        FAILED = 'failed', 'Failed'
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link the payment to a user
    razorpay_order_id = models.CharField(max_length=255)  # Razorpay order ID
    payment_id = models.CharField(max_length=255)  # Razorpay payment ID
    amount = models.DecimalField(max_digits=8, decimal_places=2)  # Amount paid
    currency = models.CharField(max_length=3)  # Currency code (e.g., "INR")
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the payment
    payment_status = models.CharField(max_length=20, choices=PaymentStatusChoices.choices, default=PaymentStatusChoices.PENDING)
    Catering = models.ForeignKey(Catering, on_delete=models.CASCADE, null=True, blank=True)


    def str(self):
        return f"Order for {self.user.name}"

    class Meta:
        ordering = ['-timestamp']
        
#Update Status not implemented
    def update_status(self):
        # Calculate the time difference in minutes
        time_difference = (timezone.now() - self.timestamp).total_seconds() / 60

        if self.payment_status == self.PaymentStatusChoices.PENDING and time_difference > 1:
            # Update the status to "Failed"
            self.payment_status = self.PaymentStatusChoices.FAILED
            self.save()

from django.db import models

class LeaveApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    duration = models.CharField(max_length=20, choices=[('full-day', 'Full Day'), ('half-day-morning', 'Half Day (Morning)'), ('half-day-afternoon', 'Half Day (Afternoon)')])
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"Leave Application for {self.user.username} on {self.date}"

class MedicalLeave(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    leaveFromDate = models.DateField()
    leaveToDate = models.DateField()
    reason = models.TextField(null=True)
    medicalCertificate = models.FileField(upload_to='medical_certificates', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

    def __str__(self):
        return f'{self.user.username} - Leave Application: {self.leaveFromDate} to {self.leaveToDate}'

    
class PredictedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    predicted_class = models.CharField(max_length=100, null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Assuming you have a CustomUser model
    billing_information = models.ForeignKey('BillingInformation', on_delete=models.CASCADE, related_name='reviews', null=True)
    rating = models.FloatField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.name} on {self.timestamp}"
    

class Stock(models.Model):
    menu_item = models.OneToOneField(menus, on_delete=models.CASCADE, related_name='stock')
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.menu_item.name} Stock: {self.stock_quantity}"
    

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('out_of_stock', 'Out of Stock'),
        ('stock_decrease', 'Stock Decrease'),
        
        # Add more notification types as needed
    ]

    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    menu_item = models.ForeignKey(menus, on_delete=models.CASCADE, null=True, blank=True)
    
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)

    def __str__(self):
        return f"{self.get_notification_type_display()}: {self.message}"
