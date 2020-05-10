import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(BASE_PATH, 'README.rst')) as f:
    README = f.read()


class DjangoTestCommand(TestCommand):
    user_options = TestCommand.user_options + [
        ('settings=', None, "The Python path to a settings module"),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.settings = ''

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import django
        from django.conf import settings
        from django.test.utils import get_runner

        if self.settings:
            os.environ['DJANGO_SETTINGS_MODULE'] = self.settings
        django.setup()
        TestRunner = get_runner(settings, test_runner_class=self.test_runner)
        test_runner = TestRunner()
        test_labels = [self.test_suite]
        failures = test_runner.run_tests(test_labels)
        if failures:
            sys.exit(1)


setup(
    name='django-wcwidth-filter',
    version='0.0.1',
    packages=find_packages(),
    description='Django Template Filters for multi-width characters',
    long_description=README,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ),
    author='Masashi Shibata',
    author_email='contact@c-bata.link',
    url='https://github.com/c-bata/django-wcwidth-filter',
    license='MIT',
    install_requires=[
        'Django',
        'wcwidth',
    ],
    test_suite='wcwidth_filter.tests',
    tests_require=[],
    cmdclass={'test': DjangoTestCommand}
)
