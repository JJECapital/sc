from django import template
from django.template.defaultfilters import stringfilter

import string

register = template.Library()

@register.filter
@stringfilter
def splitrole(value, arg):
	a, b = value.split(arg)
	return b

@register.filter
@stringfilter
def splitcustomer(value, arg):
	a, b = value.split(arg)
	return a

@register.filter(name='addclass')
def addclass(value, arg):
	return value.as_widget(attrs={'class': arg})

@register.filter
@stringfilter
def capitalise(line):
    return ' '.join(s[0].upper() + s[1:] for s in line.split(' '))

@register.filter
@stringfilter
def plusone(value):
	a = value.split('-')
	b = [str(a[x]) for x in range(len(a))]
	#b = str(b).strip('[\'\']')
	c = ''.join(b)
	return b


@register.filter
@stringfilter
def stripzeros(value):
	a = value.lstrip('0')
	return a


@register.filter
def increment(value):
	a = value + 1
	return a

@register.simple_tag(name='plusone')
def increment(value, customer):
	value = int(value)
	value = value + 1
	value = str(value)
	if len(value) == 1:
		value = '000' + value
	elif len(value) == 2:
		value = '00' + value
	elif len(value) == 3:
		value = '0' + value
	else:
		value = value
	if customer == 'DimensionData':
		cust = 'DD'
	elif customer == 'Dell':
		cust = 'DL'
	elif customer == 'JJECapital':
		cust = 'JJ'
	elif customer == 'APaaS':
		cust = 'AP'
	else:
		cust = 'GL'
	return cust + '-' + value