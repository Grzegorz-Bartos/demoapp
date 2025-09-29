from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import UploadTextForm
from .utils import scramble_text


class UploadView(FormView):
    template_name = "textprocessor/upload.html"
    form_class = UploadTextForm

    def form_valid(self, form):
        uploaded = form.cleaned_data["file"]
        raw = uploaded.read()

        for enc in ("utf-8", "cp1250"):
            try:
                text = raw.decode(enc)
                break
            except UnicodeDecodeError:
                continue
        else:
            text = raw.decode("utf-8", errors="ignore")

        processed = scramble_text(text)
        self.request.session["processed_text"] = processed
        return redirect("textprocessor:result")


class ResultView(TemplateView):
    template_name = "textprocessor/result.html"

    def get(self, request, *args, **kwargs):
        processed = request.session.get("processed_text")
        if processed is None:
            return redirect("textprocessor:upload")
        return self.render_to_response({"processed": processed})
