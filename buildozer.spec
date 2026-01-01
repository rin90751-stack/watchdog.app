[app]

title = Watchdog App
package.name = watchdog
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# App entry file
entrypoint = main.py

# Use Python3 + Kivy
requirements = python3,kivy
requirements_source = requirements.txt

# Optional icon
icon.filename = icon.png

orientation = portrait
fullscreen = 0

# Permissions (add only if needed)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Minimum + target API
android.minapi = 21
android.api = 33
android.ndk = 25b

# Package format
android.archs = arm64-v8a,armeabi-v7a

# App version (required for build)
version = 1.0.0

# Keep .py files compiled only
android.add_src = .
android.whitelist =

# Enable logcat debugging output
log_level = 2


[buildozer]
log_level = 2
warn_on_root = 1
