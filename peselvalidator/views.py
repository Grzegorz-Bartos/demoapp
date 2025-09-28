from django.views.generic.edit import FormView

from .forms import PeselForm
from .utils import validate_pesel


class PeselFormView(FormView):
    template_name = "peselvalidator/form.html"
    form_class = PeselForm

    def form_valid(self, form):
        info = validate_pesel(form.cleaned_data["pesel"])
        return self.render_to_response({"form": form, "info": info})

    def form_invalid(self, form):
        return self.render_to_response({"form": form, "info": None})
