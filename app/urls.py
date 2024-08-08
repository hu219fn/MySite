from django.urls import path
from .views import *
from django.contrib.auth import views as viewsAuth

urlpatterns = [
    path('register/', SignupViews.as_view(), name='register'),
    path('register/login/', viewsAuth.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('register/logout/', logoutViews, name='logout'),
    path('register/change_password/', viewsAuth.PasswordChangeView.as_view(template_name='auth/password_change.html', success_url='done/'), name='change-password'),
    path('register/change_password/done/', viewsAuth.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password-change-done'), 
    path('', index, name='index'),
    path('del-subject/<int:pk>/', Del_subject.as_view(), name='del-subject'),
    path('edit-subject/<int:pk>/', Edit_subject.as_view(), name='edit-subject'),
    path('add_subject/', add_subject,name='add_subject'),
    path('search/', search, name='search'),  
    path('lesson/<int:id>/',detail_subject,name='detail_subject'), 
    path('lesson/<int:id>/books/', books_section, name='books_section'),
    path('lesson/<int:id>/add_book/', add_book, name='add_book'),
    path('lesson/<int:id>/search-books/', search_book, name='search_book'),
    path('lesson/<int:id>/books/edit/<int:pk>/', Edit_book.as_view(), name='edit_book'),
    path('books/del/<int:id>/', del_book, name='del_book'), 
    path('lesson/<int:id>/notebooks/', notebook_section, name='notebooks_section'),
    path('lesson/<int:id>/add_notebook/', add_notebook, name='add_notebook'),
    path('lesson/<int:id>/search-notebooks/', search_notebook, name='search_notebook'),
    path('lesson/<int:id>/notebooks/edit/<int:pk>/', Edit_notebook.as_view(), name='edit_notebook'),
    path('notebooks/del/<int:id>/', del_notebook, name='del_notebook'), 
    path('lesson/<int:id>/mlkhasat/', mlkhasat_section, name='mlkhasats_section'),
    path('lesson/<int:id>/add_mlkhasat/', add_mlkhasat, name='add_mlkhasat'),
    path('mlkhasats/edit/<int:pk>/', Edit_mlkhasat.as_view(), name='edit_mlkhasat'),
    path('mlkhasat/<int:id>/', mlkhasat, name='mlkhasat'),
    path('mlkhasats/del/<int:id>/', del_mlkhasat, name='mlkhasat'),
    path('lesson/<int:id>/search-mlkhasats/', search_mlkhasat, name='search_mlkhasat'), 
    path('lesson/<int:id>/questions/', questions_section, name='questions_section'),
    path('lesson/<int:id>/add_question/', add_question, name='add_question'),
    path('question/<int:id>/', question, name='question'),
    path('questions/edit/<int:pk>/', Edit_question.as_view(), name='edit_question'),
    path('questions/del/<int:id>/', del_question, name='question'),
    path('lesson/<int:id>/search-questions/', search_question, name='search_question'), 
    path('lesson/<int:id>/importantQuestions/', importantQuestions_section, name='ImportantQuestions_section'),
    path('lesson/<int:id>/add_ImportantQuestion/', add_ImportantQuestion, name='add_ImportantQuestion'),
    path('ImportantQuestion/<int:id>/', importantQuestion, name='importantQuestion'),
    path('ImportantQuestions/edit/<int:pk>/', Edit_Important.as_view(), name='Edit_Important'),
    path('ImportantQuestions/del/<int:id>/', del_importantQuestion, name='importantQuestion'),
    path('lesson/<int:id>/search-ImportantQuestions/', search_importantQuestion, name='search_importantQuestion'), 
    path('lesson/<int:id>/recordings/', recordings_section, name='recordings_section'),
    path('lesson/<int:id>/add_recordings/', add_recordings, name='add_recordings'),
    path('recording/edit/<int:pk>/', Edit_Recording.as_view(), name='Edit_Recording'),
    path('recordings/<int:id>/', recordings, name='recordings'),
    path('recording/del/<int:id>/', del_recording, name='recording'),
    path('lesson/<int:id>/search-recordings/', search_recording, name='search_recording'),
]
