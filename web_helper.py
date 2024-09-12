import qrcode
import urllib.parse

def converter_dicionário_em_query_string(params: dict):
    query_string = urllib.parse.urlencode(params)
    return query_string


def make_qrcode(data, input_type='text'):
    if input_type == 'text':
        qrcodefile = "static/img/qrcode.png"
        img = qrcode.make(data)
        img.save(qrcodefile)
    
    elif input_type == 'file':
        with open(data) as f:
            qrcodefile = "qrcode.png"
            img = qrcode.make(f.read())
            img.save(qrcodefile)