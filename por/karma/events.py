from pyramid_formalchemy import events
from por.models.dashboard import Project
from por.karma import KarmaRenderer


#Project rendering events
@events.subscriber([Project, events.IBeforeRenderEvent])
def before_project_render(context, event):
    fs = event.kwargs['fs']
    if not fs._render_fields.keys():
        fs.configure(readonly=fs.readonly)
    fs.karma_id.set(renderer=KarmaRenderer)
