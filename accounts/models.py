from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager   
from django.dispatch import receiver
from django.db.models.signals import post_save
import random


class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password = None):
        if not username:
            raise ValueError("must have a  username")
        if not email:
            raise ValueError("must have a valid email")
        

        user = self.model(email = self.normalize_email(email)+ str(random.randint(1, 9999)),
            first_name = first_name,
            last_name = last_name,
            username = username )

        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
            
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using = self._db)

        return user
    


class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
    role_choice= (
        (RESTAURANT,'restaurant'),
        (CUSTOMER,"customer")
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=12,blank=True)
    role  =  models.PositiveIntegerField(choices= role_choice ,null=True,blank=True)

    objects = UserManager()


    # required_fields

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name' , 'last_name']

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    # def has_obj_perm(self,:
    #     return self.has_perm(perm)

    def has_module_perms(self,app_label):
        return True
    


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', null=True,blank=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos',null=True,blank = True)
    address_line_1 = models.CharField(max_length=200,null=True,blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    country  = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank = True)
    city = models.CharField(max_length=50,null=True,blank=True)
    pin_code = models.IntegerField(null=True,blank=True)
    latitude = models.CharField(max_length=100,null=True,blank = True)
    longitude = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.email
    


# what are we doing here >> 
# we will send the requests to django signals so whenever the user is created the persons
# userprofile is created 

# problems >> while saving and creating the uer profile, we have to also update the email of the 
# person so that he would have a unique email 

# approach 1>> creating the signals and taking the username of the person and feeding it to the email 

# we see that the username unique identifier works 






# here we have used the django signals     
@receiver(post_save,sender= User )
def post_save_reciever(sender,instance,created,**kwargs):
    print(created)

    if created:
        # now this will be the code to run 
        # print(instance.username)
        user_profile = UserProfile(user=instance)
        user_profile.save()
    else:
         user_profile = UserProfile.objects.get(user=instance)
         user_profile.save()

  
    






    






