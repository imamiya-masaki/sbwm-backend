ALLOWED_EXTENSIONS = set(['png', 'jpg'])

def allowed_file(filename):
    return '.' in fliename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONSß