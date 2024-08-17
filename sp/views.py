from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.decorators import login_required

#class TaskViewSet(viewsets.ModelViewSet):
#    queryset = Task.objects.all()
    

# 각 모델에 대한 뷰셋 생성
#def generate_viewsets():
#    viewsets_dict = {}
#    for model_name, serializer in serializers.items():
#        model = getattr(models, model_name)
#        viewset_class = type(f'{model_name}ViewSet', (viewsets.ModelViewSet,), {'queryset': model.objects.all(), 'serializer_class': serializer})
#        viewsets_dict[model_name] = viewset_class
#    return viewsets_dict

# viewsets = generate_viewsets()

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error_message = "Invalid credentials"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    # 관리자 페이지 로직
    return render(request, 'admin_dashboard.html')

def signup(request):
    if request.method == 'POST':
        pass
    return render(request, 'signup.html')




@login_required
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
        return redirect('admin_dashboard')
    return render(request, 'create_product.html')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('admin_dashboard')
    return render(request, 'update_product.html', {'product': product})

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('admin_dashboard')


