[app]

# (str) Title of your application
title = MyApplication

# (str) Package name
package.name = myapplication

# (str) Package domain (needed for android/ios packaging)
package.domain = org.my.domain

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (list) Features
android.features = onSaveInstanceState

# (list) Services to be included in the apk
services = NAME:MyService:my.module:my.service

# (list) Presplash of the application
presplash.filename = %(source.include_patterns)s/presplash.png
