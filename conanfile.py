from conans import ConanFile


class gslConan(ConanFile):
    name = "gsl"
    version = "0.0.1"
    license = "MIT"
    url = "https://github.com/kinddragon/conan-gsl"
    options = {}
    default_options = ""

    def requirements(self):
        pass

    def source(self):
       self.run("git clone https://github.com/Microsoft/GSL.git gsl")
       self.run("cd gsl && git reset --hard 8361aae39eba1bd3b41bd188baa4019aaa8317b1")

    def package(self):
        self.copy("*", dst="include/gsl", src="gsl/gsl")

    def package_info(self):
        pass
