from idlelib.sidebar import LineNumbers

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import Http404
from django.template.exceptions import TemplateDoesNotExist
from django.conf import settings

# Add the Blog model if it doesn't exist
class Blog:
    objects = type('', (), {'get': lambda *args, **kwargs: None})()

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
    if request.method == "POST":
        # Form validation
        message_name = request.POST.get('message-name', '').strip()
        message_email = request.POST.get('message-email', '').strip()
        message_phone = request.POST.get('message-phone', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        errors = {}
        if not message_name:
            errors['name'] = 'Name is required'
        if not message_email:
            errors['email'] = 'Email is required'
        if not message:
            errors['message'] = 'Message is required'
            
        if errors:
            return render(request, 'contact.html', {
                'errors': errors,
                'form_data': {
                    'name': message_name,
                    'email': message_email,
                    'phone': message_phone,
                    'message': message
                }
            })
        
        # Send email
        email_subject = f"Contact Form Submission from {message_name}"
        email_body = f"""
        You have received a new message from the contact form:
        
        Name: {message_name}
        Email: {message_email}
        Phone: {message_phone}
        
        Message:
        {message}
        """
        
        try:
            send_mail(
                email_subject, 
                email_body, 
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # Send to the same email address that's sending
                fail_silently=False,
            )
            return render(request, 'contact.html', {'message_name': message_name, 'success': True})
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Email sending failed: {str(e)}")
            return render(request, 'contact.html', {
                'error': 'Failed to send email. Please try again later.',
                'form_data': {
                    'name': message_name,
                    'email': message_email,
                    'phone': message_phone,
                    'message': message
                }
            })
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
    try:
        blog = Blog.objects.get(slug=slug)
        template_name = f'blog/{slug}.html'
        return render(request, template_name)
    except TemplateDoesNotExist:
        # Fallback to a generic template or redirect to home
        return redirect('home')
    except Exception as e:
        # Handle other exceptions
        print(f"Error in blog_detail: {e}")
        return redirect('home')