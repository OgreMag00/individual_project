from unittest import result
from django.db import models


class Tests(models.Model):
    user = models.TextField(default='')
    test = models.IntegerField()
    result = models.CharField(max_length=20,default='')
    
    def add_result(self, user, test_num, test):
        self.user = user
        self.test = test_num
        self.result = test
        
        self.save