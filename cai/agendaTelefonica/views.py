from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .form import PersonaForm

def persona_list(request, template_name='persona_list.html'):
    persona = Persona.objects.all()
    data = {}
    data['object_list'] = persona
    return render(request, template_name, data)

def persona_view(request, pk, template_name='persona_detail.html'):
    persona= get_object_or_404(Persona, pk=pk)    
    return render(request, template_name, {'object':persona})

def persona_create(request, template_name='persona_form.html'):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('persona_list')
    return render(request, template_name, {'form':form})

def persona_update(request, pk, template_name='persona_form.html'):
    persona= get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save()
        return redirect('persona_list')
    return render(request, template_name, {'form':form})

def persona_delete(request, pk, template_name='persona_confirm_delete.html'):
    persona= get_object_or_404(Persona, pk=pk)    
    if request.method=='POST':
        persona.delete()
        return redirect('persona_list')
    return render(request, template_name, {'object':persona})