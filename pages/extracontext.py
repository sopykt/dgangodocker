from datetime import datetime

def bg_img():
    day = datetime.now().day
    bg_img = 'img/bg/'+ str(day) +'.jpg'
    context = {
        'bg_img': bg_img
    }
    return context

def about_context():
    context = {
        'mission': 'missions',
        'motto': 'mottos'
    }
    return context

def contact_context():
    context ={
        'contacts': 'contacts'
    }
    return context