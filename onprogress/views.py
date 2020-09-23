from django.shortcuts import render
from .models import Contact
import codecs
from django.core.mail import *
from django.template.loader import render_to_string
# Create your views here.

module_dir = 'static/information/'

def home(request):
    return render(request, 'onprogress/home.html')

def about(request):
    file_path = module_dir + 'HAKKIMIZDA.txt'
    data = codecs.open(file_path, 'r', encoding='utf-8').read().split('|')
    context = {
        'title': "Hakkımızda",
        'header': data[0],
        'body': data[1]
    }
    return render(request, 'onprogress/about.html', context)

def politics(request):
    file_path_gizli = module_dir + 'GIZLILIK_POLITIKASI.txt'
    file_path_teslim = module_dir + 'TESLIMAT_POLITIKASI.txt'

    data_gizli = codecs.open(file_path_gizli, 'r', encoding='utf-8').read().split('|')
    data_teslim = codecs.open(file_path_teslim, 'r', encoding='utf-8').read().split('|')
    body_gizli_kvk_split = data_gizli[3].split('-list-')
    list_items = body_gizli_kvk_split[1].split('-item-')

    context = {
        'title': 'Politikalar',
        'title_teslim': data_teslim[0],
        'body_teslim': data_teslim[1],
        'title_gizli': data_gizli[0],
        'body_gizli': data_gizli[1],
        'title_gizli_kvk': data_gizli[2],
        'body_gizli_kvk_top': body_gizli_kvk_split[0],
        'body_gizli_kvk_list': list_items,
        'body_gizli_kvk_bottom': body_gizli_kvk_split[2],
        'title_gizli_telif': data_gizli[4],
        'body_gizli_telif': data_gizli[5],
        'title_gizli_diger': data_gizli[6],
        'body_gizli_diger': data_gizli[7],
    }

    return render(request, 'onprogress/politics.html', context)

def contact_form(request):
    if request.method == 'POST':
        _name = request.POST['name']
        _surname = request.POST['surname']
        _subject = request.POST['subject']
        _phone = request.POST['phone']
        _email = request.POST['email']
        _content = request.POST['content']
        _getinformation = request.POST.get('confirm', False)

        contact = Contact()
        contact.__setattr__('name', _name)
        contact.__setattr__('surname', _surname)
        contact.__setattr__('title', _subject)
        contact.__setattr__('phone', _phone)
        contact.__setattr__('email', _email)
        contact.__setattr__('content', _content)
        contact.__setattr__('getinformation', True)
        contact.save()

        info = {'name': _name, 'surname': _surname, 'subject': _subject, 'phone': _phone, 'email': _email, 'content': _content, 'date': contact.__getattribute__('date_sent')}

        if _getinformation == 'on':
            from_ = 'info@kurye16.com'

            # Send welcome mail to user who has signed in.
            to_user = str(_email)
            subject_user = 'Hoşgeldiniz!'
            message_user = render_to_string('onprogress/email_contact.html', {'name': _name, 'surname': _surname}, request=request)
            send_mail(
                subject_user,
                message_user,
                from_,
                [to_user],
            )

            # Send information mail to info@kurye16.com
            subject_ = "YENİ MESAJ"
            message_ = render_to_string('onprogress/email_info.html', info, request=request)
            send_mail(
                subject_,
                message_,
                from_,
                [from_]
            )

        return render(request, 'onprogress/contact_form.html', {'title': 'İletişim'})
    else:
        return render(request, 'onprogress/contact_form.html', {'title': 'İletişim'})
