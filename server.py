from bottle import route, run, template, static_file, request
import os.path

dist_path = './dist'
pwa_file_name = 'pwa-upload.png'


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('file')
    name, ext = os.path.splitext(upload.filename)

    save_path = os.path.join(dist_path, pwa_file_name)
    # appends upload.filename automatically
    upload.save(save_path, overwrite=True)
    return 'OK<script>history.go(-1);</script>'


@route('/<icon_name:re:pwa-.+.png>')
def get_pwa_icon(icon_name):
    print("icon_name", icon_name)
    if os.path.exists(os.path.join(dist_path, pwa_file_name)):
        return static_file(pwa_file_name, root=dist_path)
    else:
        return static_file(icon_name, root=dist_path)


@route('/')
def index():
    return static_file('index.html', root=dist_path)


@route('/<filepath:path>')
def index(filepath):
    return static_file(filepath, root=dist_path)


run(host='0.0.0.0', port=6080, reloader=True)
