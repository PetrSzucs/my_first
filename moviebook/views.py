﻿from django.shortcuts import render

#hesloheslo
def index(request):
    return render(request, "moviebook/index.html", dict(nazev_filmu="Strážci Galaxie", zanr="Fantasy", hodnoceni="11/10"))