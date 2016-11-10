from django.shortcuts import render

templateObject = {
	"HeadTitle":{
		"title": "Timp Transportes",
		"section": "",
	},	
	"isHome": True,
}

def home(request):
	templateObject["HeadTitle"]["section"] = "Inicio"
	templateObject["isHome"] = True
	print(templateObject)
	return render(request, 'home.html', templateObject)

def aboutUs(request):
	templateObject["HeadTitle"]["section"] = "Nosotros"
	templateObject["isHome"] = False
	return render(request, 'about_us.html', templateObject)

def services(request):
	templateObject["HeadTitle"]["section"] = "Servicios"
	templateObject["isHome"] = False
	return render(request, 'services.html', templateObject)
