

def set_root_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Content-Type", "text/html; charset=iso-8859-1")
    return resp


def set_redirect_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("Content-Type", "text/html; charset=iso-8859-1")
    return resp


def set_login_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("F5-Login-Page", "true")
    resp.headers.set("Pragma", "no-cache")
    resp.headers.set("Cache-Control", "no-cache, must-revalidate")
    resp.headers.set("Content-Type", "text/html;charset=utf-8")
    resp.headers.set("Vary", "Accept-Encoding")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy", "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    return resp


def set_welcome_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("F5-Login-Page", "true")
    resp.headers.set("Pragma", "no-cache")
    resp.headers.set("Cache-Control", "no-cache, must-revalidate")
    resp.headers.set("Content-Type", "text/html;charset=iso-8859-1")
    resp.headers.set("Vary", "Accept-Encoding")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy",
                     "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    return resp


def set_blank_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("ETag", '"195-597db38323600-gzip"')
    resp.headers.set("Accept-Ranges", "bytes")
    resp.headers.set("Content-Type", "text/html;charset=iso-8859-1")
    resp.headers.set("Vary", "Accept-Encoding")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy",
                     "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    return resp


def set_css_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("ETag", '"c5c-597db09680fc0-gzip"')
    resp.headers.set("Accept-Ranges", "bytes")
    resp.headers.set("Cache-Control", "max-age=120, must-revalidate")
    resp.headers.set("Content-Type", "text/css")
    resp.headers.set("Vary", "Accept-Encoding")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy",
                     "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    return resp


def set_js_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("ETag", '"21ef-597db38323600"')
    resp.headers.set("Accept-Ranges", "bytes")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy", "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    resp.headers.set("Cache-Control", "must-revalidate")
    resp.headers.set("Content-Type", "application/javascript")
    return resp


def set_img_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("ETag", '"1fe7-597db09680fc0"')
    resp.headers.set("Accept-Ranges", "bytes")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy",
                     "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    resp.headers.set("Cache-Control", "max-age=18000")
    resp.headers.set("Content-Type", "image/png")
    return resp


def set_favicon_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("ETag", '"5c06-597db38323600"')
    resp.headers.set("Accept-Ranges", "bytes")
    resp.headers.set("X-Content-Type-Options", "nosniff")
    resp.headers.set("X-XSS-Protection", "1; mode=block")
    resp.headers.set("Content-Security-Policy",
                     "default-src 'self'  'unsafe-inline' 'unsafe-eval' data: blob:; img-src 'self' data:  http://127.4.1.1 http://127.4.2.1")
    resp.headers.set("Content-Type", "image/vnd.microsoft.icon")
    return resp


def set_404_headers(resp):
    resp.headers.set("Server", "Apache")
    resp.headers.set("X-Frame-Options", "SAMEORIGIN")
    resp.headers.set("Strict-Transport-Security", "max-age=16070400; includeSubDomains")
    resp.headers.set("Content-Type", "text/html; charset=iso-8859-1")
    return resp
