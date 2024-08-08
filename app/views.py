from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *

@login_required
def index(request):
    return render(request, 'index.html',{'subjects':Subject.objects.filter(user=request.user).order_by('title')})

@login_required
def search(request):
    subjects = Subject.objects.filter(title__icontains=request.GET['search'])
    return render(request, 'ced Sujects/search.html',{'subjects': subjects})

class SignupViews(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'auth/signup.html'
    success_url = '/'
    def form_valid(self, form):
        login(self.request, form.save())
        return redirect('/')

@login_required
def logoutViews(request):
    logout(request)
    return render(request, 'auth/logout.html')

@login_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('/')
        else:
            return render(request, 'ced Sujects/create.html', {'form': form})
    else:
        form = SubjectForm()
        return render(request, 'ced Sujects/create.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class Del_subject(DeleteView):
    model = Subject
    template_name = 'ced Sujects/delete.html'
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class Edit_subject(UpdateView):
    model = Subject
    fields = ['title','description']
    template_name = 'ced Sujects/edit.html'
    success_url = '/'

@login_required
def detail_subject(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'ced Sujects/detail.html',{'item':subject})

@login_required
def books_section(request, id):
    subject = Subject.objects.get(id=id)
    books = Book.objects.filter(subject=subject, user=request.user)
    return render(request, 'books/list.html',{'items':books,'subject':subject})

@login_required
def add_book(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        try:
            file = request.FILES['file']
        except:
            url = request.POST['url']
        user = request.user
        subject = Subject.objects.get(id=id)
        try:
            book = Book(title=title, description=description, file=file, user=user, subject=subject)
            book.save()
        except:
            book = Book(title=title, description=description, url=url, user=user, subject=subject)
            book.save()
        return redirect('/lesson/'+ str(id) +'/books/')
    else:
        return render(request, 'books/create.html')

@login_required
def search_book(request, id):
    subject = Subject.objects.get(id=id)
    books = Book.objects.filter(title__icontains=request.GET['search_book'], user=request.user, subject=subject)
    return render(request, 'books/search.html',{'items':books,'subject':subject})

@method_decorator(login_required, name='dispatch')
class Edit_book(UpdateView):
    model = Book
    fields = ['title','description','file','url']
    template_name = 'books/update.html'
    success_url = '/'

@login_required
def del_book(request,id):
    book = Book.objects.get(id=id)
    if request.user == book.user:
        if request.method == 'POST':
            book.delete()
            return redirect('/lesson/'+str(book.subject.id)+'/books/')
        return render(request, 'books/delete.html',{'item':book})
    else:
        return redirect('/')

@login_required
def notebook_section(request, id):
    subject = Subject.objects.get(id=id)
    notebooks = NoteBooks.objects.filter(subject=subject, user=request.user)
    return render(request, 'notebooks/list.html',{'items':notebooks,'subject':subject})

@login_required
def add_notebook(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        try:
            file = request.FILES['file']
        except:
            url = request.POST['url']
        user = request.user
        subject = Subject.objects.get(id=id)
        try:
            notebook = NoteBooks(title=title, description=description, file=file, user=user, subject=subject)
            notebook.save()
        except:
            notebook = NoteBooks(title=title, description=description, url=url, user=user, subject=subject)
            notebook.save()
        return redirect('/lesson/'+ str(id) +'/notebooks/')
    else:
        return render(request, 'notebooks/create.html')

@login_required
def search_notebook(request, id):
    subject = Subject.objects.get(id=id)
    notebooks = NoteBooks.objects.filter(title__icontains=request.GET['search_notebook'], user=request.user, subject=subject)
    return render(request, 'notebooks/search.html',{'items':notebooks,'subject':subject})

@method_decorator(login_required, name='dispatch')
class Edit_notebook(UpdateView):
    model = NoteBooks
    fields = ['title','description','file','url']
    template_name = 'notebooks/update.html'
    success_url = '/'

@login_required
def del_notebook(request,id):
    notebook = NoteBooks.objects.get(id=id)
    if notebook.user == request.user:
        if request.method == 'POST':
            notebook.delete()
            return redirect('/lesson/'+str(notebook.subject.id)+'/notebooks/')
        return render(request, 'notebooks/delete.html',{'item':notebook})
    else:
        return redirect('/')

@login_required
def mlkhasat_section(request, id):
    subject = Subject.objects.get(id=id)
    mlkhasat = Mlkhasat.objects.filter(subject=subject, user=request.user)
    return render(request, 'mlkhasat/list.html',{'items':mlkhasat,'subject':subject})

@login_required
def add_mlkhasat(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        try:
            image = request.FILES['image']
        except:
            file = request.FILES['file']
        url = request.POST['url']
        user = request.user
        subject = Subject.objects.get(id=id)
        try:
            mlkhasat = Mlkhasat(title=title, description=description, image=image, url=url, user=user, subject=subject)
        except:
            mlkhasat = Mlkhasat(title=title, description=description, file=file, url=url, user=user, subject=subject)
        mlkhasat.save()
        return redirect('/lesson/'+ str(id) +'/mlkhasat/')
    else:
        return render(request, 'mlkhasat/create.html')

@method_decorator(login_required, name='dispatch')
class Edit_mlkhasat(UpdateView):
    model = Mlkhasat
    fields = ['title','description','image','file','url']
    template_name = 'mlkhasat/update.html'
    success_url = '/'

@login_required
def mlkhasat(request, id):
    item = Mlkhasat.objects.get(id=id,user=request.user)
    if request.user == item.user:
        return render(request, 'mlkhasat/detail.html', {'item':item})
    else:
        return redirect('/')

@login_required
def del_mlkhasat(request,id):
    mlkhasat = Mlkhasat.objects.get(id=id)
    if mlkhasat.user == request.user:
        if request.method == 'POST':
            mlkhasat.delete()
            return redirect('/lesson/'+str(mlkhasat.subject.id)+'/mlkhasat/')
        return render(request, 'mlkhasat/delete.html',{'item':mlkhasat})
    else:
        return redirect('/')

@login_required
def search_mlkhasat(request, id):
    subject = Subject.objects.get(id=id)
    mlkhasats = Mlkhasat.objects.filter(title__icontains=request.GET['search_mlkhasat'], user=request.user, subject=subject)
    return render(request, 'mlkhasat/search.html',{'items':mlkhasats,'subject':subject})

@login_required
def questions_section(request, id):
    subject = Subject.objects.get(id=id)
    questions = Question.objects.filter(subject=subject, user=request.user)
    return render(request, 'questions/list.html',{'items':questions,'subject':subject})

@login_required
def add_question(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        try:
            image = request.FILES['image']
        except:
            file = request.FILES['file']
        url = request.POST['url']
        user = request.user
        subject = Subject.objects.get(id=id)
        try:
            question = Question(title=title, description=description, image=image, url=url, user=user, subject=subject)
        except:
            question = Question(title=title, description=description, file=file, url=url, user=user, subject=subject)
        finally:
            question.save()
        return redirect('/lesson/'+ str(id) +'/questions/')
    else:
        return render(request, 'questions/create.html')

@login_required
def question(request, id):
    item = Question.objects.get(id=id,user=request.user)
    if request.user == item.user:
        return render(request, 'questions/detail.html', {'item':item})
    else:
        return redirect('/')

@method_decorator(login_required, name='dispatch')
class Edit_question(UpdateView):
    model = Question
    fields = ['title','description','image','file','url']
    template_name = 'questions/update.html'
    success_url = '/'

@login_required
def del_question(request,id):
    question = Question.objects.get(id=id)
    if question.user == request.user:
        if request.method == 'POST':
            question.delete()
            return redirect('/lesson/'+str(question.subject.id)+'/questions/')
        return render(request, 'questions/delete.html',{'item':question})
    else:
        return redirect('/')

@login_required
def search_question(request, id):
    subject = Subject.objects.get(id=id)
    questions = Question.objects.filter(title__icontains=request.GET['search_question'], user=request.user, subject=subject)
    return render(request, 'questions/search.html',{'items':questions,'subject':subject})

@login_required
def importantQuestions_section(request, id):
    subject = Subject.objects.get(id=id)
    importantQuestions = ImportantQuestion.objects.filter(subject=subject, user=request.user)
    return render(request, 'َImportantquestions/list.html',{'items':importantQuestions,'subject':subject})

@login_required
def add_ImportantQuestion(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        try:
            image = request.FILES['image']
        except:
            file = request.FILES['file']
        url = request.POST['url']
        user = request.user
        subject = Subject.objects.get(id=id)
        try:
            question = ImportantQuestion(title=title, description=description, image=image, url=url, user=user, subject=subject)
        except:
            question = ImportantQuestion(title=title, description=description, file=file, url=url, user=user, subject=subject)
        finally:
            question.save()
        return redirect('/lesson/'+ str(id) +'/importantQuestions/')
    else:
        return render(request, 'َImportantquestions/create.html')

def importantQuestion(request, id):
    item = ImportantQuestion.objects.get(id=id,user=request.user)
    if request.user == item.user:
        return render(request, 'َImportantquestions/detail.html', {'item':item})
    else:
        return redirect('/')

@method_decorator(login_required, name='dispatch')
class Edit_Important(UpdateView):
    model = ImportantQuestion
    fields = ['title','description','image','file','url']
    template_name = 'َImportantquestions/update.html'
    success_url = '/'

@login_required
def del_importantQuestion(request,id):
    importantQuestion = ImportantQuestion.objects.get(id=id)
    if importantQuestion.user == request.user:
        if request.method == 'POST':
            importantQuestion.delete()
            return redirect('/lesson/'+str(importantQuestion.subject.id)+'/importantQuestions/')
        return render(request, 'َImportantquestions/delete.html',{'item':importantQuestion})
    else:
        return redirect('/')

@login_required
def search_importantQuestion(request, id):
    subject = Subject.objects.get(id=id)
    importantQuestions = ImportantQuestion.objects.filter(title__icontains=request.GET['search_ImportantQuestion'], user=request.user, subject=subject)
    return render(request, 'َImportantquestions/search.html',{'items':importantQuestions,'subject':subject})

@login_required
def recordings_section(request, id):
    subject = Subject.objects.get(id=id)
    recordings = Recording.objects.filter(subject=subject, user=request.user)
    return render(request, 'recordings/list.html',{'items':recordings,'subject':subject})

@login_required
def add_recordings(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        url = request.POST['url']
        user = request.user
        subject = Subject.objects.get(id=id)
        question = Recording(title=title, description=description, url=url, user=user, subject=subject)
        question.save()
        return redirect('/lesson/'+ str(id) +'/recordings/')
    else:
        return render(request, 'recordings/create.html')

@method_decorator(login_required, name='dispatch')
class Edit_Recording(UpdateView):
    model = Recording
    fields = ['title','description','url','audio_file1','audio_file2','audio_file3','audio_file4','audio_file5']
    template_name = 'recordings/update.html'
    success_url = '/'

@login_required
def del_recording(request,id):
    recording = Recording.objects.get(id=id)
    if recording.user == request.user:
        if request.method == 'POST':
            recording.delete()
            return redirect('/lesson/'+str(recording.subject.id)+'/recordings/')
        return render(request, 'recordings/delete.html',{'item':recording})
    else:
        return redirect('/')

@login_required
def recordings(request, id):
    item = Recording.objects.get(id=id,user=request.user)
    if request.user == item.user:
        if request.method == 'POST':
            item = Recording.objects.get(id=id,user=request.user)
            try:
                item.audio_file1 = request.FILES["record1"]
            except:
                print()
            try:
                item.audio_file2 = request.FILES["record2"]
            except:
                print()
            try:
                item.audio_file3 = request.FILES["record3"]
            except:
                print()
            try:
                item.audio_file4 = request.FILES["record4"]
            except:
                print()
            try:
                item.audio_file5 = request.FILES["record5"]
            except:
                print()
            item.save()
            return redirect('/recordings/'+str(id))
        return render(request, 'recordings/detail.html', {'item':item})
    else:
        return redirect('/')

@login_required
def search_recording(request, id):
    subject = Subject.objects.get(id=id)
    recording = Recording.objects.filter(title__icontains=request.GET['search_recording'], user=request.user, subject=subject)
    return render(request, 'recordings/search.html',{'items':recording,'subject':subject})

