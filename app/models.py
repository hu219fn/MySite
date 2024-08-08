from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Subject(models.Model):
    title = models.CharField(max_length=100, verbose_name='الاسم*')
    description = models.TextField(max_length=500, verbose_name='الوصف')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='اسم الكتاب*')
    description = models.TextField(max_length=500, verbose_name='الوصف', null=True, blank=True)
    file = models.FileField(upload_to='books/', verbose_name='الكتاب',null=True,blank=True)
    url = models.URLField(max_length=5000, null=True, blank=True, verbose_name='او اضافة رابط الكتاب')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class NoteBooks(models.Model):
    title = models.CharField(max_length=100, verbose_name='اسم الملزمة*')
    description = models.TextField(max_length=500, verbose_name='الوصف', null=True, blank=True)
    file = models.FileField(upload_to='notebooks/', verbose_name='الملزمة',null=True,blank=True)
    url = models.URLField(max_length=5000, null=True, blank=True, verbose_name='او اضافة رابط الملزمة')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Mlkhasat(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان الملخص*')
    description = models.TextField(max_length=10000, verbose_name='الوصف', null=True, blank=True)
    image = models.ImageField(upload_to='mlkhasat/img', null=True, blank=True, verbose_name='اضافة صورة الملخص')
    file = models.FileField(upload_to='mlkhasat/pdf', verbose_name='او اضافة pdf المخلص',null=True,blank=True)
    url = models.URLField(max_length=5000, null=True, blank=True, verbose_name='او اضافة رابط الملخص')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان الاسئلة*')
    description = models.TextField(max_length=10000, verbose_name='الوصف', null=True, blank=True)
    image = models.ImageField(upload_to='question/img', null=True, blank=True, verbose_name='اضافة صورة الاسئلة')
    file = models.FileField(upload_to='question/pdf', verbose_name='او اضافة pdf الاسئلة',null=True,blank=True)
    url = models.URLField(max_length=5000, null=True, blank=True, verbose_name='او اضافة رابط الاسئلة')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class ImportantQuestion(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان الاسئلة*')
    description = models.TextField(max_length=10000, verbose_name='الوصف', null=True, blank=True)
    image = models.ImageField(upload_to='question/img', null=True, blank=True, verbose_name='اضافة صورة الاسئلة')
    file = models.FileField(upload_to='question/pdf', verbose_name='او اضافة pdf الاسئلة',null=True,blank=True)
    url = models.URLField(max_length=5000, null=True, blank=True, verbose_name='او اضافة رابط الاسئلة')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Recording(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان الاسئلة*')
    description = models.TextField(max_length=1000, verbose_name='الوصف', null=True, blank=True)
    url = models.URLField(max_length=5000, null=True, blank=True, verbose_name='اضافة رابط التسجيل')
    audio_file1 = models.FileField(upload_to='recordings/',null=True,blank=True)
    audio_file2 = models.FileField(upload_to='recordings/',null=True,blank=True)
    audio_file3 = models.FileField(upload_to='recordings/',null=True,blank=True)
    audio_file4 = models.FileField(upload_to='recordings/',null=True,blank=True)
    audio_file5 = models.FileField(upload_to='recordings/',null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
