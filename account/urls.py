from django.urls import path

from .import views
from .views import PostUpdateView, UserUpdateView, PasswordsChangeView

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('userlogged', views.userlogged, name="userlogged"),
    path('teamdetails', views.teamdetails, name="teamdetails"),
    path('new', views.new, name='new'),
    path('newtc', views.newtc, name='newtc'),
    path('template', views.template, name='template'),
    path('tctemplate', views.tctemplate, name='tctemplate'),
    path('pptemplate', views.pptemplate, name='pptemplate'),
    path('draft', views.draft, name='draft'),
    path('ppdraft', views.ppdraft, name='ppdraft'),
    path('tcdraft', views.tcdraft, name='tcdraft'),
    path('contact', views.contact, name='contact'),
    path('templated/<slug:slug_text>/', views.templated, name='templated'),
    path('templatedshare/<slug:slug_text>/', views.templatedshare, name='templatedshare'),
    path('delete_template/<slug:slug_text>/', views.delete_template, name='delete_template'),
    path('profile/', views.profile, name='profile'),
    path('faq', views.faq, name='faq'),
    path('templated/<slug:slug>/update/', PostUpdateView.as_view(), name='update'),
    path('password/', PasswordsChangeView.as_view(template_name='password_reset/change-password.html')),
    path('password_change_done', views.password_change_done, name='password_change_done'),






    
    # path('read', views.PostDetailView.as_view(), name="post_detail")
]