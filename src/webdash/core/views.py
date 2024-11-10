import os
import random

from django.conf import settings
from django.shortcuts import render, redirect
from django.templatetags.static import static
import orjson
from django.core.cache import cache


async def background_image(request):
    files_cache = await cache.aget("background_image_filenames")
    image_dir = "webdash/backgrounds"
    if files_cache:
        files = orjson.loads(files_cache)
    else:
        image_dir_abs = os.path.join(settings.STATIC_ROOT, image_dir)
        files = os.listdir(image_dir_abs)
        await cache.aset("background_image_filenames", orjson.dumps(files))
    chosen_image = os.path.join(image_dir, random.choice(files))
    return redirect(static(chosen_image), permanent=False)
    
async def index(request):
    return render(request, "core/index.html")