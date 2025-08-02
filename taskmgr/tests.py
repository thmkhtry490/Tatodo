from django.test import TestCase
from .models import Task
class TaskTest(TestCase):
    def setUp(self):
        Task.objects.create(title="testing",text="the test part",done=False)
    def test_first(self):
       self.task = Task.objects.get(title="testing")
       self.assertEqual(str(self.task),"testing")