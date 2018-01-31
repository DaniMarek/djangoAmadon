from django.shortcuts import render, redirect

def index(request):
	request.session['products'] = [
		{'id':'0', 'item':'Dojo T-shirt', 'price': '19.99'},
		{'id':'1', 'item':'Dojo Sweater', 'price':'29.99'},
		{'id':'2', 'item': 'Dojo Cup', 'price':'4.99'},
		{'id':'3', 'item':'Algoritm Book', 'price':'49.99'},
	]
	request.session['pricelist'] = [19.99, 29.99, 4.99, 49.99]
	if request.session.get('total') == None:
		request.session['total'] = 0
	if request.session.get('sumtotal') == None:
		request.session['sumtotal'] = 0
	if request.session.get('item') == None:
		request.session['item'] = 0
  	return render(request, 'amapp/index.html')

def buyitem(request):
	pricelist = request.session.get('pricelist')
	i = int(request.POST['price'])
	price = float(pricelist[i])
	request.session['total'] = price* float(request.POST['quantity'])
	request.session['item'] = int(request.session.get('item')) + int(request.POST['quantity'])
# insert if statement to add totals and create sumtotal for thanks page
	request.session['sumtotal'] = int(request.POST['quantity'])
	

	return render(request,'amapp/thanks.html')

# def thanks(request):
# 	return render('amapp/thanks.html')

# def back(request):
# 	return redirect('/')