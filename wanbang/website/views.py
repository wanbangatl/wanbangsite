from idlelib.sidebar import LineNumbers

from django.shortcuts import render
from django.core.mail import send_mail


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


def blog_detail(request, slug):
    # In a real application, you might fetch a blog post based on the slug
    # For now, we'll just render the blog template
    return render(request, 'blog/blog_template.html', {'slug': slug})