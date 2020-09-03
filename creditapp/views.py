from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import User,TransferHistory
from .forms import TransferForm,CreateUserForm,TransactionForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here

def homeView(request):
	return render(request,'home.html',{})

def userView(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('users')
	else:
		form = CreateUserForm()
	context_data = {'form': form}
	return render(request,'create_user.html', context_data)


	

def userlistView(request):
	data=User.objects.all()
	return render(request,'userlist.html',{'data':data})


def transferView(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
        	return HttpResponseRedirect('transfer/profile/%s/'%request.POST['sender'])
    else:       
        form = TransferForm()
    form.fields['sender'].widget.attrs.update({'class':'sender'})
    context_data = {'form': form}
    return render(request,'transfer.html', context_data)


def profileView(request,pk):

	if request.method=='POST':
		return HttpResponseRedirect('transaction/pk')

	userlist=User.objects.all()
	data=User.objects.get(pk=pk)

	context_data = {
				'userlist':userlist,
				'data': data
				}
	
	return render(request,'profile.html',context_data)


def transactionView(request,pk):

	if request.method == 'POST':
		form=TransactionForm(request.POST)
		if form.is_valid():
			sender=User.objects.get(pk=pk)
			reciever = User.objects.get(pk=request.POST['reciever'])

			if(int(request.POST['amount'])>sender.credits):
				message='Sorry..not enough credits'
				return render(request,'error.html',{'user':pk,'message':message})
			elif(int(request.POST['amount'])==0):
				message='Credits cannot be zero!! Please select valid amount'
				return render(request,'error.html',{'user':pk,'message':message})
			else:
				reciever.credits+=int(request.POST['amount'])
				reciever.save()
				sender.credits-=int(request.POST['amount'])
				sender.save()

			form.save()
			return render(request,'success.html',{'user':pk})

				
	else:
		form=TransactionForm()
		sender=User.objects.get(pk=pk)
		form.fields["sender"].queryset = User.objects.filter(username=sender)
		form.fields["reciever"].queryset = User.objects.exclude(username=sender)


	return render(request,'transaction.html',{'form':form})
	



def credithistoryView(request):
	data =TransferHistory.objects.all().order_by('-date')
	
	return render(request,'credithistory.html',{'data':data})



	







