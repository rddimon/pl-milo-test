from django.shortcuts import render, get_object_or_404, redirect
from djqscsv import render_to_csv_response

from apps.account.forms import UserForm, UserCreationForm
from apps.account.models import User


def user_list(request):
    return render(request, 'account/user-list.html', {'users': User.objects.all()})


def user_detail(request, pk):
    instance = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('account_user_detail', form.instance.pk)
    else:
        form = UserForm(instance=instance)
    return render(request, 'account/user-detail.html', {'form': form})


def user_new(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_user_list')
    else:
        form = UserCreationForm()

    return render(request, 'account/user-new.html', {'form': form})


def user_delete(request, pk):
    get_object_or_404(User, pk=pk).delete()
    return redirect('account_user_list')


def user_list_download(request):
    return render_to_csv_response(User.objects.values())
