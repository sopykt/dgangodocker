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
        'mission': 'mission',
        'motto': 'motto'
    }
    return context