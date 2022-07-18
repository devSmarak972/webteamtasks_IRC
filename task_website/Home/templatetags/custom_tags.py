from django import template

register = template.Library()


@register.inclusion_tag('college-card.html', takes_context=True)
def college_card(context, college):
    bookmarks = context["bookmarks"]
    applications = context["applications"]

    # college, bookmarks = args.split(',')
    if college.Name in bookmarks:
        icon = "fas"
    else:
        icon = "far"
    if college.Name in applications:
        apply_status = "btn-applied"
        applytext = "Applied"
    else:
        apply_status = "apply-btn"
        applytext = "Apply"

    return {
        "Name": college.Name,
        "Country": college.Country,
        "Expense": college.Expense,
        "Deadline": college.Deadline,
        "imglink": college.image.url,
        "icon": icon,
        "apply_status": apply_status,
        "applytext": applytext,
        "Website": college.Website
    }


@register.inclusion_tag('application-card.html')
def application_card(college):

    # college, bookmarks = args.split(',')

 
    return {
        "Name": college.Name,
        "Country": college.Country,
        "Expense": college.Expense,
        "Deadline": college.Deadline,
        "imglink": college.image.url,
        "Website": college.Website,
        "Address": college.Address,
        "Email": college.Email,
        "info": college.Info
    }


@register.inclusion_tag('notification-card.html')
def notification_card(notif):

    # college, bookmarks = args.split(',')

    return {
        "headline": notif.headline,
        "body_text": notif.body_text,
        "datetime": notif.datetime,
    }


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='addValue')
def addValue(value, arg):
    return value.as_widget(attrs={'value': arg})
# home_template = get_template('home.html')
# register.inclusion_tag(home_template)(college_card)
