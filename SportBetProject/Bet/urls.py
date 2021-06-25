from django.urls import path
from .views import *

urlpatterns=[
    path('bet/<int:match_id>/',BetPostView.as_view(),name='bet'),
    path('trans/', TransactionView.as_view()),
]