from django.shortcuts import render
from transactions.models import Transaction, CreditCard
from bankaccounts.models import Account,KYC
from django.contrib import messages
from django.shortcuts import redirect

def credit_card(request,number):
    account=Account.objects.get(user=request.user)
    kyc=KYC.objects.get(user=request.user)
    credit_card=CreditCard.objects.get(number=number)

    context={
        "credit_card":credit_card,
        "kyc":kyc,
        "account":account     

    }
    return render(request,'account\credit_card_detail.html',context)

def credit_card_bill(request,card_id):
    account=Account.objects.get(user=request.user)
    credit_card=CreditCard.objects.get(card_id=card_id)

    context={
        "account":account,
        "credit_card":credit_card
    }
    if request.method=="POST":
        if account.account_balance>credit_card.amount:
            credit_card.amount +=account.account_balance
            credit_card.save()
            account.account_balance -=credit_card.amount
            account.save()
            return redirect("transactions:send_card_bill",credit_card.number)
        else:
            messages.warning(request,"Insufficient Funds, fund your account and try again")
    return render(request,"account/credit_card_bill.html",context)
