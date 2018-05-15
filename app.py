import os
from tornado import web, locale, ioloop
from forms import TestForm


class MainHandler(web.RequestHandler):
    def initialize(self):
        self.form = TestForm(meta={'locale': self.locale})

    def get(self):
        return self.render('page.html', form=self.form)

    def post(self):
        # just mock the form processing
        # as it will always raise error
        self.form.process(data={'username': 'hello'})
        self.form.validate()
        return self.render('page.html', form=self.form)



def make_app():
    return web.Application(
            [
                (r'/', MainHandler),
            ],
            template_path=os.path.dirname(__file__),
            debug=True
        )


if __name__ == '__main__':

    locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
    locale_domain = 'test'
    locale.load_gettext_translations(locale_dir, locale_domain)

    app = make_app()
    app.listen(8888)
    print("Listening on post 8888 ...")
    ioloop.IOLoop.current().start()
