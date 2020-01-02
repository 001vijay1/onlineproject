from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Contact,Comment,Category
from .forms import CommentForm

# Create your views here.
def index(request):
    form = Post.objects.all()
    return render(request,'index.html',{'form':form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog-single.html', {'category': category})

def blogdetails(request,slug):
    relpost  = Post.objects.all().filter(slug = slug)
    categories = Category.objects.all()
    posts = get_object_or_404(Post,slug=slug)
    comments = posts.comments.filter(active=True, parent__isnull=True)
    if(request.method=='POST'):
        comment_form = CommentForm(data=request.POST)
        if(comment_form.is_valid()):
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if(parent_id):
                parent_obj=Comment.objects.get(id = parent_id)
                if(parent_obj):
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent= parent_obj
        new_comment = comment_form.save(commit=False)
        new_comment.post = posts
        new_comment.save()
        return redirect('blogdetails',slug)
    else:
        comment_form = CommentForm()
    context = {
        'post':posts,
        'comments':comments,
        'comment_form':comment_form,
        'category':categories,
        'relpost':relpost,
    }
    return render(request,'blog-single.html',context)


def contact(request):
    thanks = False
    if(request.method=='POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email = email,phone = phone,desc = desc)
        contact.save()
        thanks = True
    return render(request,'contact.html',{'thanks':thanks})

def about(request):
    return render(request,'about.html')