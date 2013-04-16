from distutils import log
from setuptools.command.sdist import sdist
from zipfile import ZipFile

template = '''
from os.path import dirname, join
import sys

sys.path.insert(0, join(dirname(__file__), {base_dir!r}))

{main}
'''

class zdist(sdist):

    user_options = [
        ('keep-temp', 'k',
         "keep the distribution tree around after creating " +
         "archive file(s)"),
        ('dist-dir=', 'd',
         "directory to put the source distribution archive(s) in "
         "[default: dist]"),
        ]
    
    help_options = []

    def finalize_options(self):
        sdist.finalize_options(self)
        self.formats = ['zip']

    def make_archive(self, base_name, format, root_dir=None, base_dir=None,
                     owner=None, group=None):
        # original dist
        zip_path = sdist.make_archive(self, base_name, format, root_dir, base_dir,
                                      owner, group)

        # get __main__.py content
        with open('__main__.py') as main_file:
            main = main_file.read()
        
        with ZipFile(zip_path, 'a') as zip_file:
            log.info("adding %r to %r", '__main__.py', zip_path)
            zip_file.writestr('__main__.py', template.format(
                    base_dir=base_dir,
                    main=main
                    ))

            

        return zip_path
