from django.shortcuts import render, redirect

def index(request):
	context = {
		'shirt': 19.99,
		'sweater': 29.99,
		'cup': 4.99,
		'algobook': 49.99,
	}

  	return render(request, 'amapp/index.html', context)

def buyitem(request):
	# try:
	# 	if request.method == 'POST':
	# 		request.session['item']
	pass