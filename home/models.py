from django.db import models

# Create your models here.

class feedback(models.Model):
    name = models.CharField(max_length=50)
    suggestions = models.CharField(max_length=125)
    rating = models.CharField(max_length=50)

class Company_profile(models.Model):
    C_id = models.CharField(max_length=10)
    # C_name = models.CharField(max_length=50)
    C_phone =models.CharField(max_length=15)
    C_add = models.CharField(max_length=122)
    C_email =  models.CharField(max_length=50)
    C_username = models.CharField(max_length = 20)

class tender(models.Model):
    t_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=25)
    Time_dur = models.CharField(max_length=25)
    price = models.CharField(max_length=20)
    Start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    descreption = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.t_id:
            last_id = tender.objects.order_by('-t_id').first()
            if last_id:
                last_id_int = int(last_id.t_id)  # Convert the last_id.t_id to integer
                self.t_id = str(last_id_int + 1).zfill(10)  # Increment and pad with leading zeros
            else:
                self.t_id = '0000000001'  # Initial ID
        super().save(*args, **kwargs)


class create_progress(models.Model):
    t_Id = models.CharField(max_length=10)
    descreption = models.CharField(max_length=200)

class applications(models.Model):
    tid = models.CharField(max_length=10)
    c_email = models.CharField(max_length=50)
    q_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2) 
    q_exp = models.IntegerField(default=0)
    q_duration =  models.IntegerField(default=0)

    
