from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique = True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        
    )
    amount_available = models.IntegerField(blank = True,null = True)
    active = models.BooleanField(default = True)

    #adding a readable name to the model
    def __str__(self):
        return self.code
    
    def check_available(self):
        now = timezone.now()
        if self.amount_available is None:
            return True
        elif self.amount_available > 0:
            return True
        
    # def set_active(self):
    #     if (self.amount_available > 0 or self.amount_available == None) and self.valid_from >= now and self.valid_to <= now:
    #         self.active = True

        

