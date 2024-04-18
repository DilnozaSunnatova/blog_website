from django.shortcuts import render
from .models import Profile,Skill,Service,About,Project,Category,Blog
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def home(request):
    profile = Profile.objects.last() #oxirgi obyektni oladi
    skills = Skill.objects.order_by('order')  #barcha obyektni oladi
    services = Service.objects.order_by('order')
    about = About.objects.last()
    projects = Project.objects.all()
    categories = Category.objects.all()
    blogs = Blog.objects.all()

    return render(request,'index.html',
                  {'profile': profile, 
                   'skills': skills,
                   'services':services,
                   'about': about,
                   'projects':projects,
                   'categories':categories,
                   'blogs': blogs
                   })  #stringni ichidagi htmlda ishlatiladi



def project_detail(request,pk):
    project= get_object_or_404(Project,id=pk)
    return render(request,'portfolio-details.html',{'project':project})




def blog_detail(request,pk):
    blog = get_object_or_404(Blog,id=pk)
    blog.view_count += 1
    blog.save()

    
    return render(request,'single-blog.html',{'blog':blog})


def blog(request):
    blogs=Blog.objects.all()

    popular_posts = Blog.objects.order_by('-view_count')[:4]

    

    if request.method =='POST':
        search = request.POST.get('search')
        blogs = Blog.objects.filter(title__icontains = search)
        print(search)



    p = Paginator(blogs,3)
    page_number = request.GET.get('page')
    try:
        page_objects = p.get_page(page_number)

    except PageNotAnInteger:
        page_objects = p.page(1)

    except EmptyPage:
        page_objects = p.page(p.num_pages)
    print(page_objects)
    return render(request,'blog.html',{'blogs':page_objects, 'popular_posts': popular_posts})

def about(request):
    return render(request,'about-us.html')

def portfolio(request):
    return render(request,'portfolio.html')








