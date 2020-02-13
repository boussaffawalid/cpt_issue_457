from conans import ConanFile, CMake


class FoobarConan(ConanFile):
    name = 'Foobar'
    version = '0.0.1'
    options = {
        'with_bar': [True, False],
        'shared': [True, False],
    }
    default_options= '''
        with_bar=True
        shared=True
    '''

    def source(self):
        pass

    def build(self):
        pass

    def package(self):
        pass
