from django.forms import ModelForm
from .models import TransferHistory,User



class CreateUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','email','credits']
		
		

class TransferForm(ModelForm):
	class Meta:
		model = TransferHistory
		fields = ['sender']

		labels = {
               'sender': 'User ',
              
            }

		


class TransactionForm(ModelForm):
	class Meta:
		model = TransferHistory
		fields = '__all__'


		
		



		
