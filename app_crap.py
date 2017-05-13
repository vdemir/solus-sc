#!/usr/bin/env python2.7
import gi.repository
gi.require_version('AppStreamGlib', '1.0')
from gi.repository import AppStreamGlib as AS
import sys

store = AS.Store()

store.load(AS.StoreLoadFlags.APP_INFO_SYSTEM)

def test_markup(desc):
    m = AS.markup_convert_simple(desc)
    return m

app = store.get_app_by_pkgname("gnome-builder")

desc = app.get_description("C")
print test_markup(desc)

screens = app.get_screenshots()
if not screens:
    print("No screens")
    sys.exit(1)

# Get the default screenshot
default = [x for x in screens if x.get_kind() == AS.ScreenshotKind.DEFAULT]
if not default:
    default = screens[0]
else:
    default = default[0]

alt_screens = [x for x in screens if x != default]
print("Got %s alt screens" % len(alt_screens))

thumbnail = None
large = None
normal = None

# TODO: Multiply by 2 for HiDPI screens
images = default.get_images()
for image in images:
    if image.get_width() == AS.IMAGE_LARGE_WIDTH:
        large = image
    elif image.get_width() == AS.IMAGE_NORMAL_WIDTH:
        normal = image
    elif image.get_width() == AS.IMAGE_THUMBNAIL_WIDTH:
        thumbnail = image
    if large and normal and thumbnail:
        break

if thumbnail:
    print("Thumbnail: %s" % thumbnail.get_url())
if normal:
    print("Normal: %s" % normal.get_url())
if large:
    print("Large: %s" % large.get_url())
