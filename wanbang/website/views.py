from idlelib.sidebar import LineNumbers

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import Http404


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def exterior(request):
    return render(request, 'exterior.html', {})


def interior(request):
    return render(request, 'interior.html', {})


def expert(request):
    return render(request, 'expert.html', {})


def aboutu(request):
    return render(request, 'aboutu.html', {})


def insight(request):
    return render(request, 'insight.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']

        # send an email
        send_mail(
            '来自：' + message_name + '的留言板信息',  # subject
            message + '\n电话号码：' + message_phone + '\n邮箱：' + message_email,  # message
            None,  # from email
            ['franco_lsc@163.com'],  # to email
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def aboutu(request):
    if request.method == 'POST':
        question_name = request.POST['question-name']
        question_email = request.POST['question-email']
        question_title = request.POST['question-title']
        question_one_cat = request.POST['question-one-cat']
        question_one_detail = request.POST['question-one-detail']
        # problem_two = request.POST['problem-two']
        # problem_three = request.POST['problem-three']
        # question_others = request.POST['question-others']

        # send an email
        # send_mail(
        #     'message from ' + message_name, #subject
        #     message + '\nphone number ' + message_phone, #message
        #     message_email, #from email
        #     ['franco_lsc@163.com'], #to email
        # )

        return render(request, 'aboutu.html',
                      {'question_name': question_name, 'question_one_detail': question_one_detail,
                       'question_one_cat': question_one_cat})

    else:
        return render(request, 'aboutu.html', {})


def blog_template(request):
    return render(request, 'blog/blog_template.html')


def blog_list(request):
    """
    View function for the blog listing page
    """
    # Get all blog posts or implement pagination if needed
    # Example (adjust according to your models):
    # blog_posts = BlogPost.objects.all().order_by('-date_published')
    return render(request, 'website/blog.html', {
        # 'blog_posts': blog_posts,
        'title': 'Blog',
    })


def blog_detail(request, slug):
    """
    View function for individual blog posts
    """
    # Example (adjust according to your models):
    # try:
    #     post = BlogPost.objects.get(slug=slug)
    # except BlogPost.DoesNotExist:
    #     raise Http404("Blog post not found")
    
    return render(request, 'website/blog_detail.html', {
        # 'post': post,
        'title': 'Blog Post',  # You might want to use the actual post title here
        'slug': slug
    })


def blog_detail(request, slug):
    # For static html templates, we can use a direct template approach
    if slug == 'blog_interior_sandy_springs.html':
        return render(request, 'blog/blog_interior_sandy_springs.html')
    
    # For dynamic blog content from database (when implemented)
    try:
        blog = Blog.objects.get(slug=slug)
        recent_blogs = Blog.objects.exclude(id=blog.id).order_by('-published_date')[:3]
        context = {
            'blog': blog,
            'recent_blogs': recent_blogs
        }
        return render(request, 'blog/blog_detail.html', context)
    except:
        # Fall back to static template if available
        template_name = f"blog/{slug}.html"
        try:
            return render(request, template_name)
        except TemplateDoesNotExist:
            raise Http404("Blog post not found")