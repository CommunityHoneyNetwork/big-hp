import os
import random

import flask
from flask import Flask, render_template, request, make_response

import config
import output
import utils


app = application = Flask(__name__)


config_file = os.environ.get("CONFIG", "default.cfg")
conf = config.parse_config(config_file)
if not conf:
    exit(-1)
output = output.Output(conf)


@app.before_request
def log_request():
    output.write(request)


@app.route('/')
def root():
    resp = make_response(render_template("root.jinja2"))
    resp = utils.set_root_headers(resp)
    return resp


@app.route('/tmui/tmui/system/settings/redirect.jsp')
def redirect():
    resp = make_response(render_template("redirect.jinja2"), 302)
    resp = utils.set_redirect_headers(resp)
    resp.headers.set("Location", "/tmui/login.jsp")
    return resp


@app.route('/tmui/login.jsp')
def login():
    resp = make_response(render_template("login.jinja2",
                                         hostname=conf.get("bighp", "hostname", fallback=""),
                                         ip_address=conf.get("bighp", "ip_address", fallback="")))
    resp = utils.set_login_headers(resp)
    jsession_id = "".join('%02x' % random.randint(0, 255) for _ in range(16)).upper()
    resp.headers.set("Set-Cookie", "JSESSIONID=" + jsession_id + "; Path=/tmui; Secure; HttpOnly")
    return resp


@app.route('/tmui/tmui/login/welcome.jsp')
def welcome():
    resp = make_response(render_template("welcome.jinja2",
                                         hostname=conf.get("bighp", "hostname", fallback="")))
    resp = utils.set_welcome_headers(resp)
    return resp


@app.route('/tmui/logmein.html', methods=['POST'])
def logmein():
    return flask.redirect("/tmui/login.jsp?msgcode=1&")


@app.route('/xui/common/blank.html')
def blank():
    resp = make_response(render_template("blank.jinja2"))
    resp = utils.set_blank_headers(resp)
    return resp


@app.route('/xui/common/scripts/utility.js')
def utility_js():
    with open(os.path.join('static', 'js', 'utility.js'), 'r') as f:
        resp = make_response(f.read())
    resp = utils.set_js_headers(resp)
    return resp


@app.route('/tmui/tmui/login/css/login.css')
def login_css():
    with open(os.path.join('static', 'css', 'login.css'), 'r') as f:
        resp = make_response(f.read())
    resp = utils.set_css_headers(resp)
    return resp


@app.route('/xui/common/css/modals.css')
def modals_css():
    with open(os.path.join('static', 'css', 'modals.css'), 'r') as f:
        resp = make_response(f.read())
    resp = utils.set_css_headers(resp)
    return resp


@app.route('/xui/common/css/base.css')
def base_css():
    with open(os.path.join('static', 'css', 'base.css'), 'r') as f:
        resp = make_response(f.read())
    resp = utils.set_css_headers(resp)
    return resp


@app.route('/xui/common/css/reset.css')
def reset_css():
    with open(os.path.join('static', 'css', 'reset.css'), 'r') as f:
        resp = make_response(f.read())
    resp = utils.set_css_headers(resp)
    return resp


@app.route('/xui/common/css/fonts.css')
def fonts_css():
    with open(os.path.join('static', 'css', 'fonts.css'), 'r') as f:
        resp = make_response(f.read())
    resp = utils.set_css_headers(resp)
    return resp


@app.route('/tmui/tmui/login/images/logo_f5.png')
def logo_f5():
    with open(os.path.join('static', 'img', 'logo_f5.png'), 'rb') as f:
        resp = make_response(f.read())
    resp = utils.set_root_headers(resp)
    return resp


@app.route('/tmui/tmui/login/images/background_banner.png')
def background_banner():
    with open(os.path.join('static', 'img', 'background_banner.png'), 'rb') as f:
        resp = make_response(f.read())
    resp = utils.set_root_headers(resp)
    return resp


if __name__ == '__main__':
    app.run()
