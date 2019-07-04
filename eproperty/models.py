from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.

#done-Bj
class Country(models.Model):
    countryID = models.AutoField(primary_key=True)
    countryName = models.TextField(unique=True)

    def __str__(self):
        return self.countryName

#done-Bj
class Province(models.Model):
    provinceID = models.AutoField(primary_key=True)
    countryID = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceName = models.TextField()

    def __str__(self):
        return self.provinceName

#done-Bj
class City(models.Model):
    cityID = models.AutoField(primary_key=True)
    cityName = models.TextField()
    countryName = models.ForeignKey(Country, on_delete=models.DO_NOTHING, )
    provinceID = models.ForeignKey(Province, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return self.cityName

#done-Bj
class PropertyCategory(models.Model):
    propertyCategory = models.AutoField(primary_key=True)
    propertyCategoryName = models.CharField(max_length=200)

    def __str__(self):
        return self.propertyCategoryName

#done-Bj
class Property_Sector(models.Model):
    propertySector = models.AutoField(primary_key=True)
    propertySectorName = models.CharField(max_length=200)

    def __str__(self):
        return self.propertySectorName

#done-Bj
class Property_Facing(models.Model):
    propertyFacing = models.AutoField(primary_key=True)
    propertyFacingName = models.CharField(max_length=200)

    def __str__(self):
        return self.propertyFacingName


class Users(models.Model):
    user_ID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return str(self.user_ID)+"-"+self.firstName+"-"+self.email


#done-Bj
class Property(models.Model):
    propertyID = models.AutoField(primary_key=True)
    propertyTitle = models.CharField(max_length=255)
    propertyCategory = models.ForeignKey(PropertyCategory, on_delete=models.DO_NOTHING)
    propertySector = models.ForeignKey(Property_Sector, on_delete=models.DO_NOTHING)
    propertyFacing = models.ForeignKey(Property_Facing, on_delete=models.DO_NOTHING)
    propertyCountry = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    #propertyImages = models.ForeignKey(PropertyImages, on_delete=models.DO_NOTHING)
    propertyProvince = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    propertyCity = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    propertyStreet = models.CharField(max_length=255, null=False)
    propertyPostalCode = models.CharField(max_length=255, null=False)
    propertyStreetnumber = models.CharField(max_length=255, null=False)
    propertyConstructionDate = models.DateField()
    propertyRegistrationDate = models.DateField()
    propertyNoofHalls = models.IntegerField(null=False)
    propertyNumberofRooms = models.IntegerField(null=False)
    propertyNoofBathrooms = models.FloatField(null=False)
    propertyNoofFloors = models.IntegerField(null=False)
    propertyTotalArea = models.FloatField(null=False)
    propertyAskingPrice = models.FloatField(null=False)
    propertySellingPrice = models.FloatField(null=False)
    user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.propertyID)+"-"+self.propertyTitle+" -> Asking Price: "+str(self.propertyAskingPrice)+"$"

#done-Bj
class PropertyImages(models.Model):
    propertyImageID = models.AutoField(primary_key=True)
    propertyID = models.ForeignKey(Property, on_delete=models.DO_NOTHING, related_name='propImg')
    propertyImage = models.ImageField(blank=True, null=True)
    propertyImageDescription = models.TextField()

    def __str__(self):
        return str(self.propertyImageID)+"-"+self.propertyImageDescription
#done by neel

class RoleCode(models.Model):
    roleCode_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class  UserRole(models.Model):
    userRole_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    roleCode_ID = models.ForeignKey(RoleCode, on_delete=models.CASCADE)
    dateAssigned = models.DateField()

    def __str__(self):
        return str(self.userRole_ID)+"-"+str(self.user_ID)+"-"+str(self.roleCode_ID)

class Password(models.Model):
    password_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    userName = models.CharField(max_length=200, unique=True)
    encryptedPassword = models.CharField(max_length=200)
    salt = models.CharField(max_length=200)
    userAccountExpiryDate = models.DateField()
    passwordMustChanged = models.BooleanField(default=True)
    passwordReset = models.BooleanField(default=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.userName

class PermissionType(models.Model):
    permission_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    rolePermission_ID = models.AutoField(primary_key=True)
    permissionType_ID = models.ForeignKey(PermissionType, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    sysFeature = models.CharField(max_length=200)

    def __str__(self):
        return self.code+"- "+self.sysFeature

class RolePermissionDetail(models.Model):
    rolePermissionDetail_ID = models.AutoField(primary_key=True)
    rolePermission_ID = models.ForeignKey(RolePermission,on_delete=models.CASCADE)
    roleCode_ID = models.ForeignKey(RoleCode,on_delete=models.CASCADE)


    def __str__(self):
        return self.rolePermissionDetail_ID


class Advertisement(models.Model):
    adv_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    propertyID = models.OneToOneField(Property, on_delete=models.DO_NOTHING)
    advStartDate = models.DateField()
    advEndDate = models.DateField()
    advDescription = models.CharField(max_length=200)

    def __str__(self):
        return self.propertyID.propertyTitle