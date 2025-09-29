from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import UploadTextForm
from .utils import scramble_text


class UploadView(FormView):
    template_name = "textprocessor/upload.html"
    form_class = UploadTextForm

    @staticmethod
    def _decode_file(f) -> str:
        raw = f.read()
        for enc in ("utf-8", "cp1250"):
            try:
                return raw.decode(enc)
            except UnicodeDecodeError:
                continue
        return raw.decode("utf-8", errors="ignore")

    def form_valid(self, form):
        text = self._decode_file(form.cleaned_data["file"])
        self.request.session["processed_text"] = scramble_text(text)
        return redirect("textprocessor:result")


class ResultView(TemplateView):
    template_name = "textprocessor/result.html"

    def get(self, request, *args, **kwargs):
        if "processed_text" not in request.session:
            return redirect("textprocessor:upload")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["processed"] = self.request.session.get("processed_text")
        return ctx
