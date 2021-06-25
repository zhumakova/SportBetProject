
def withdraw_money(amount,profile):
    if amount>=200:
        profile.wallet-=amount
        profile.save()

