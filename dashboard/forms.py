from django import forms



def ModelFormFunc(model, data=None, instance=None, files=None):
	global model_
	model_ = model

	class ModelAddForm(forms.ModelForm):
		# forms.ModelChoiceField(queryset= model_.objects.all(), initial=0)
		def __init__(self, *args, **kwargs):
			# user = kwargs.pop('user','')
			super(ModelAddForm, self).__init__(*args, **kwargs)

		class Meta:
			model = model_
			fields = ('__all__')


	form = ModelAddForm()
	if data or instance or files:
		form = ModelAddForm(data=data, instance=instance, files=files)


	return form

		
