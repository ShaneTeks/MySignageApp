from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Define the User model with roles
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Owner', 'Owner'),
        ('Designer', 'Designer'),
        ('Admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Define the Job model
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')

# Define the Task model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks')

# Define the Contract model
class Contract(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name='contract')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)

# Define the Inventory model
class Inventory(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
