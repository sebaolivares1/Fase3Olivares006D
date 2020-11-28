from django.shortcuts import render, redirect,get_object_or_404
from . models import Juego, JuegoInstance
from django.views import generic
from . forms import JuegoForm


# Create your views here.
def index(request):
    num_Juegos = Juego.objects.all().count()
    num_Instances = JuegoInstance.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={'num_juegos': num_Juegos, 'num_instances': num_Instances,},
    )

def tuDestiny(request):
    
    return render(
        request,
        'tuDestiny.html',
    )

def tuSea(request):
    
    return render(
        request,
        'tuSea.html',
    )

def videos(request):
    
    return render(
        request,
        'videos.html',
    )
def agjuegos(request):
    
    return render(
        request,
        'agjuegos.html',
    )

def index_admin(request):
    
    return render(
        request,
        'index_admin.html',
    )

def index_user(request):
    
    return render(
        request,
        'index_user.html',
    )
      


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#views


class JuegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy('index')

class JuegoDetailView(generic.DetailView):
    model = Juego


class JuegoListView(generic.ListView):
    model = Juego
    paginate_by = 6


class JuegoInstanceCreate(CreateView):
    model = JuegoInstance
    fields = '__all__'

class JuegoInstanceUpdate(UpdateView):
    model = JuegoInstance
    fields = '__all__'

class JuegoInstanceDelete(DeleteView):
    model = JuegoInstance
    success_url = reverse_lazy('index')

class JuegoInstanceDetailView(generic.DetailView):
    model = JuegoInstance


class JuegoInstanceListView(generic.ListView):
    model = JuegoInstance
    paginate_by = 6


def juego_new(request):
    if request.method == "POST":
        form = JuegoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm()
        return render(request, 'catalogo/juego_form.html', {'form': form})

def juego_edit(request, pk):
    post = get_object_or_404(Juego, pk=pk)
    if request.method == "POST":
        form = JuegoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('juego-detail', pk=post.pk)
    else:
        form = JuegoForm(instance=post)
    return render(request, 'catalogo/juego_form.html', {'form': form})
