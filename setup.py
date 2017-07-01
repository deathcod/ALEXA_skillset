from distutils.core import setup

setup(
    name='ALEXA_skill',
    version='',
    packages=['EC2.src', 'EC2.PACKAGES.lxml', 'EC2.PACKAGES.lxml.html', 'EC2.PACKAGES.lxml.includes',
              'EC2.PACKAGES.lxml.isoschematron', 'EC2.PACKAGES.requests', 'EC2.PACKAGES.requests.packages',
              'EC2.PACKAGES.requests.packages.idna', 'EC2.PACKAGES.requests.packages.chardet',
              'EC2.PACKAGES.requests.packages.urllib3', 'EC2.PACKAGES.requests.packages.urllib3.util',
              'EC2.PACKAGES.requests.packages.urllib3.contrib', 'EC2.PACKAGES.requests.packages.urllib3.packages',
              'EC2.PACKAGES.requests.packages.urllib3.packages.backports',
              'EC2.PACKAGES.requests.packages.urllib3.packages.ssl_match_hostname', 'test',
              'myenv.lib.python3.4.distutils', 'myenv.lib.python3.4.encodings', 'myenv.lib.python3.4.importlib',
              'myenv.lib.python3.4.collections', 'myenv.lib.python3.4.site-packages.py',
              'myenv.lib.python3.4.site-packages.py._io', 'myenv.lib.python3.4.site-packages.py._log',
              'myenv.lib.python3.4.site-packages.py._code', 'myenv.lib.python3.4.site-packages.py._path',
              'myenv.lib.python3.4.site-packages.py._process', 'myenv.lib.python3.4.site-packages.PIL',
              'myenv.lib.python3.4.site-packages.pip', 'myenv.lib.python3.4.site-packages.pip.req',
              'myenv.lib.python3.4.site-packages.pip.vcs', 'myenv.lib.python3.4.site-packages.pip.utils',
              'myenv.lib.python3.4.site-packages.pip.compat', 'myenv.lib.python3.4.site-packages.pip.models',
              'myenv.lib.python3.4.site-packages.pip._vendor', 'myenv.lib.python3.4.site-packages.pip._vendor.distlib',
              'myenv.lib.python3.4.site-packages.pip._vendor.distlib._backport',
              'myenv.lib.python3.4.site-packages.pip._vendor.colorama',
              'myenv.lib.python3.4.site-packages.pip._vendor.html5lib',
              'myenv.lib.python3.4.site-packages.pip._vendor.html5lib._trie',
              'myenv.lib.python3.4.site-packages.pip._vendor.html5lib.filters',
              'myenv.lib.python3.4.site-packages.pip._vendor.html5lib.treewalkers',
              'myenv.lib.python3.4.site-packages.pip._vendor.html5lib.treeadapters',
              'myenv.lib.python3.4.site-packages.pip._vendor.html5lib.treebuilders',
              'myenv.lib.python3.4.site-packages.pip._vendor.lockfile',
              'myenv.lib.python3.4.site-packages.pip._vendor.progress',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages.chardet',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages.urllib3',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages.urllib3.util',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'myenv.lib.python3.4.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'myenv.lib.python3.4.site-packages.pip._vendor.packaging',
              'myenv.lib.python3.4.site-packages.pip._vendor.cachecontrol',
              'myenv.lib.python3.4.site-packages.pip._vendor.cachecontrol.caches',
              'myenv.lib.python3.4.site-packages.pip._vendor.webencodings',
              'myenv.lib.python3.4.site-packages.pip._vendor.pkg_resources',
              'myenv.lib.python3.4.site-packages.pip.commands', 'myenv.lib.python3.4.site-packages.pip.operations',
              'myenv.lib.python3.4.site-packages.rsa', 'myenv.lib.python3.4.site-packages.lxml',
              'myenv.lib.python3.4.site-packages.lxml.html', 'myenv.lib.python3.4.site-packages.lxml.includes',
              'myenv.lib.python3.4.site-packages.lxml.isoschematron', 'myenv.lib.python3.4.site-packages.yaml',
              'myenv.lib.python3.4.site-packages.boto3', 'myenv.lib.python3.4.site-packages.boto3.s3',
              'myenv.lib.python3.4.site-packages.boto3.ec2', 'myenv.lib.python3.4.site-packages.boto3.docs',
              'myenv.lib.python3.4.site-packages.boto3.dynamodb', 'myenv.lib.python3.4.site-packages.boto3.resources',
              'myenv.lib.python3.4.site-packages.awscli', 'myenv.lib.python3.4.site-packages.awscli.customizations',
              'myenv.lib.python3.4.site-packages.awscli.customizations.s3',
              'myenv.lib.python3.4.site-packages.awscli.customizations.s3.syncstrategy',
              'myenv.lib.python3.4.site-packages.awscli.customizations.ec2',
              'myenv.lib.python3.4.site-packages.awscli.customizations.emr',
              'myenv.lib.python3.4.site-packages.awscli.customizations.gamelift',
              'myenv.lib.python3.4.site-packages.awscli.customizations.configure',
              'myenv.lib.python3.4.site-packages.awscli.customizations.cloudtrail',
              'myenv.lib.python3.4.site-packages.awscli.customizations.codedeploy',
              'myenv.lib.python3.4.site-packages.awscli.customizations.datapipeline',
              'myenv.lib.python3.4.site-packages.awscli.customizations.configservice',
              'myenv.lib.python3.4.site-packages.awscli.customizations.cloudformation',
              'myenv.lib.python3.4.site-packages.pyasn1', 'myenv.lib.python3.4.site-packages.pyasn1.type',
              'myenv.lib.python3.4.site-packages.pyasn1.codec', 'myenv.lib.python3.4.site-packages.pyasn1.codec.ber',
              'myenv.lib.python3.4.site-packages.pyasn1.codec.cer',
              'myenv.lib.python3.4.site-packages.pyasn1.codec.der',
              'myenv.lib.python3.4.site-packages.pyasn1.codec.native',
              'myenv.lib.python3.4.site-packages.pyasn1.compat', 'myenv.lib.python3.4.site-packages._pytest',
              'myenv.lib.python3.4.site-packages._pytest._code', 'myenv.lib.python3.4.site-packages._pytest.assertion',
              'myenv.lib.python3.4.site-packages._pytest.vendored_packages',
              'myenv.lib.python3.4.site-packages.execnet', 'myenv.lib.python3.4.site-packages.execnet.script',
              'myenv.lib.python3.4.site-packages.olefile', 'myenv.lib.python3.4.site-packages.botocore',
              'myenv.lib.python3.4.site-packages.botocore.docs',
              'myenv.lib.python3.4.site-packages.botocore.docs.bcdoc',
              'myenv.lib.python3.4.site-packages.botocore.vendored',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages.chardet',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages.urllib3',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages.urllib3.util',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages.urllib3.contrib',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages.urllib3.packages',
              'myenv.lib.python3.4.site-packages.botocore.vendored.requests.packages.urllib3.packages.ssl_match_hostname',
              'myenv.lib.python3.4.site-packages.colorama', 'myenv.lib.python3.4.site-packages.coverage',
              'myenv.lib.python3.4.site-packages.dateutil', 'myenv.lib.python3.4.site-packages.dateutil.tz',
              'myenv.lib.python3.4.site-packages.dateutil.zoneinfo', 'myenv.lib.python3.4.site-packages.docutils',
              'myenv.lib.python3.4.site-packages.docutils.utils',
              'myenv.lib.python3.4.site-packages.docutils.utils.math',
              'myenv.lib.python3.4.site-packages.docutils.parsers',
              'myenv.lib.python3.4.site-packages.docutils.parsers.rst',
              'myenv.lib.python3.4.site-packages.docutils.parsers.rst.languages',
              'myenv.lib.python3.4.site-packages.docutils.parsers.rst.directives',
              'myenv.lib.python3.4.site-packages.docutils.readers',
              'myenv.lib.python3.4.site-packages.docutils.writers',
              'myenv.lib.python3.4.site-packages.docutils.writers.xetex',
              'myenv.lib.python3.4.site-packages.docutils.writers.latex2e',
              'myenv.lib.python3.4.site-packages.docutils.writers.odf_odt',
              'myenv.lib.python3.4.site-packages.docutils.writers.s5_html',
              'myenv.lib.python3.4.site-packages.docutils.writers.pep_html',
              'myenv.lib.python3.4.site-packages.docutils.writers.html4css1',
              'myenv.lib.python3.4.site-packages.docutils.writers.html5_polyglot',
              'myenv.lib.python3.4.site-packages.docutils.languages',
              'myenv.lib.python3.4.site-packages.docutils.transforms', 'myenv.lib.python3.4.site-packages.jmespath',
              'myenv.lib.python3.4.site-packages.pyflakes', 'myenv.lib.python3.4.site-packages.pyflakes.test',
              'myenv.lib.python3.4.site-packages.pyflakes.scripts', 'myenv.lib.python3.4.site-packages.requests',
              'myenv.lib.python3.4.site-packages.requests.packages',
              'myenv.lib.python3.4.site-packages.requests.packages.idna',
              'myenv.lib.python3.4.site-packages.requests.packages.chardet',
              'myenv.lib.python3.4.site-packages.requests.packages.urllib3',
              'myenv.lib.python3.4.site-packages.requests.packages.urllib3.util',
              'myenv.lib.python3.4.site-packages.requests.packages.urllib3.contrib',
              'myenv.lib.python3.4.site-packages.requests.packages.urllib3.packages',
              'myenv.lib.python3.4.site-packages.requests.packages.urllib3.packages.backports',
              'myenv.lib.python3.4.site-packages.requests.packages.urllib3.packages.ssl_match_hostname',
              'myenv.lib.python3.4.site-packages.packaging', 'myenv.lib.python3.4.site-packages._markerlib',
              'myenv.lib.python3.4.site-packages.concurrent', 'myenv.lib.python3.4.site-packages.concurrent.futures',
              'myenv.lib.python3.4.site-packages.pytest_cov', 'myenv.lib.python3.4.site-packages.s3transfer',
              'myenv.lib.python3.4.site-packages.setuptools', 'myenv.lib.python3.4.site-packages.setuptools.tests',
              'myenv.lib.python3.4.site-packages.setuptools.command', 'database'],
    url='',
    license='',
    author='deathcoder007',
    author_email='chinmay.rakshit@gmail.com',
    description=''
)