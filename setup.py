from setuptools import setup

# to publish use:
# > python setup.py sdist upload
# which depends on ~/.pypirc

setup(name='shap',
      version='0.10.0',
      description='A unified approach to explain the output of any machine learning model.',
      url='http://github.com/slundberg/shap',
      author='Scott Lundberg',
      author_email='slund1@cs.washington.edu',
      license='MIT',
      packages=['shap'],
      install_requires=['numpy', 'scipy', 'iml>=0.3.5', 'scikit-learn', 'matplotlib', 'pandas'],
      test_suite='nose.collector',
      tests_require=['nose', 'xgboost'],
      zip_safe=False)
