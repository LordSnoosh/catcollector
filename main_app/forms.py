from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
<<<<<<< HEAD
    fields = ['date', 'meal']

=======
    fields = ['date', 'meal']
>>>>>>> 54e1f4756d5ce8586bdf54d95f08f5819d5ea2f2
