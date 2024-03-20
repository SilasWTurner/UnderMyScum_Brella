 ###########################################################################
  #   Author: Silas Turner 
  #   Contributors: Oliver Fitzgerald, Luke Clarke, Ellie Andrews
  #
  #   The author has written all code in this file unless stated otherwise.
  ###########################################################################


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from users.models import UserDetail
from items.models import UserItem

# Global for how much happiness increases upon task completion
gameHappiness = 0.05

GAME_COST = 10

def home(request):
    if request.user.is_superuser: #Check if user is superuser
        return redirect('/admin/')
    user = request.user
    if user.is_authenticated: #If user is logged in add user details to context
        user_details = get_object_or_404(UserDetail, pk=user.id)
        worn_user_items = UserItem.objects.filter(user=user, is_worn=True)
        index_array = [user_item.item.item_index for user_item in worn_user_items]
        context = {
            'user_details': user_details,
            'index_array':index_array,
            }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
    
def my_pet(request):
    if not request.user.is_authenticated: #Check if user is logged in
        messages.success(request, "Please login first")
        return redirect('login')
    if request.user.is_superuser: #Check if user is superuser
        return redirect('/admin/')
    user = request.user
    if user.is_authenticated: #If user is logged in add user details to context
        user_details = get_object_or_404(UserDetail, pk=user.id)
        # Oliver Fitzgerald
        worn_user_items = UserItem.objects.filter(user=user, is_worn=True)
        index_array = [user_item.item.item_index for user_item in worn_user_items]
        # gives all of the worn items to the mypet
        context = {
            'user_details': user_details,
            'index_array':index_array,
            }
        return render(request, 'mypet.html', context)
    else:
        return render(request, 'mypet.html')

def games(request):
    if not request.user.is_authenticated: #Check if user is logged in
        messages.success(request, "Please login first")
        return redirect('login')
    if request.user.is_superuser: #Check if user is superuser
        return redirect('/admin/')
    user = request.user
    if user.is_authenticated: #If user is logged in add user details to context
        user_details = get_object_or_404(UserDetail, pk=user.id)
        # Oliver Fitzgerald-
        worn_user_items = UserItem.objects.filter(user=user, is_worn=True)
        index_array = [user_item.item.item_index for user_item in worn_user_items]
        # gives buddies worn items
        context = {
            'user_details': user_details,
            'index_array':index_array,
            'game_cost': GAME_COST,
            }
        return render(request, 'games.html', context)
    else:
        return render(request, 'games.html')

def noughtsCrosses(request):
    if not request.user.is_authenticated: #Check if user is logged in
        messages.success(request, "Please login first")
        return redirect('login')
    if request.user.is_superuser: #Check if user is superuser
        return redirect('/admin/')
 
    user = request.user
    user_details = get_object_or_404(UserDetail, pk=user.id)

    worn_user_items = UserItem.objects.filter(user=user, is_worn=True)
    index_array = [user_item.item.item_index for user_item in worn_user_items]
    
    if user_details.total_coins - GAME_COST < 0:
        messages.success(request, "Insufficient Funds")
        return redirect('games')
    updateCoins(user, -GAME_COST)
    user_details_updated = get_object_or_404(UserDetail, pk=user.id)
    context = {'user_details': user_details_updated,
               'index_array':index_array,
               }
    completeGame(user)
    return render(request, 'Games/noughtsAndCrosses.html', context)

#Luke - used to add/subtract coins
def updateCoins(user, coinsToAdd):
    if user.is_authenticated:
        user_details = get_object_or_404(UserDetail, pk=user.id)
        user_details.total_coins = user_details.total_coins + coinsToAdd
        user_details.save()

def privacy(request):
    return render(request, 'privacy.html')

#Ellie Andrews - adds buddy happiness for playing games with buddy
def completeGame(user_id):
    user = UserDetail.objects.get(user=user_id)
    newHappiness = max(0, min(1, user.buddy_happiness + gameHappiness))
    user.buddy_happiness = newHappiness
    user.save()